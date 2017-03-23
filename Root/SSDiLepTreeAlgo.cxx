#include <EventLoop/Job.h>
#include <EventLoop/StatusCode.h>
#include <EventLoop/Worker.h>
#include <EventLoop/OutputStream.h>
#include "xAODEventInfo/EventInfo.h"
#include <xAODJet/JetContainer.h>
#include <xAODTracking/VertexContainer.h>
#include <xAODEventInfo/EventInfo.h>
#include <AthContainers/ConstDataVector.h>

#include <SSDiLepAnalysis/SSDiLepTree.h>
#include <SSDiLepAnalysis/SSDiLepTreeAlgo.h>

#include <xAODAnaHelpers/TreeAlgo.h>
#include <xAODAnaHelpers/HelperFunctions.h>
#include <xAODAnaHelpers/tools/ReturnCheck.h>
#include <xAODAnaHelpers/tools/ReturnCheckConfig.h>

#include "LPXKfactorTool/LPXKfactorTool.h"

#include "TEnv.h"
#include "TSystem.h"

// this is needed to distribute the algorithm to the workers
ClassImp(SSDiLepTreeAlgo)

EL::StatusCode SSDiLepTreeAlgo :: initialize ()
{
  Info("initialize()", m_name.c_str());
  m_event = wk()->xaodEvent();
  m_store = wk()->xaodStore();

  const xAOD::EventInfo* eventInfo(nullptr);
  RETURN_CHECK("MuonEfficiencyCorrector::initialize()", HelperFunctions::retrieve(eventInfo, m_eventInfoContainerName, m_event, m_store, m_verbose) ,"");
  m_isMC = ( eventInfo->eventType( xAOD::EventInfo::IS_SIMULATION ) );
  
  m_numEvent      = 0;
  
  // get the file we created already
  TFile* treeFile = wk()->getOutputFile ("tree");
  treeFile->mkdir(m_name.c_str());
  treeFile->cd(m_name.c_str());
  
  return EL::StatusCode::SUCCESS;
}

EL::StatusCode SSDiLepTreeAlgo :: execute ()
{
  
  //m_numEvent++;

  if ( !m_isMC && m_replaceDataCont ) {
    m_muContainerName = m_muContainerNameData;
    m_elContainerName = m_elContainerNameData;

    m_muSystsVec  = ""; 
    m_elSystsVec  = ""; 
    m_metSystsVec = ""; 
  }

  // what systematics do we need to process for this event?
  // handle the nominal case (merge all) on every event, always
  std::vector<std::string> event_systNames({""});
  std::vector<std::string> muSystNames;
  std::vector<std::string> elSystNames;
  std::vector<std::string> jetSystNames;
  std::vector<std::string> metSystNames;
  //std::vector<std::string> photonSystNames;

  // this is a temporary pointer that gets switched around to check each of the systematics
  std::vector<std::string>* systNames(nullptr);

  // note that the way we set this up, none of the below ##SystNames vectors contain the nominal case
  // TODO: do we really need to check for duplicates? Maybe, maybe not.
  if(!m_muSystsVec.empty()){
    RETURN_CHECK("SSDiLepTreeAlgo::execute()", HelperFunctions::retrieve(systNames, m_muSystsVec, 0, m_store, m_verbose) ,"");
    for(const auto& systName: *systNames){
      muSystNames.push_back(systName);
      if (std::find(event_systNames.begin(), event_systNames.end(), systName) != event_systNames.end()) continue;
      event_systNames.push_back(systName);
    }
  }

  if(!m_elSystsVec.empty()){
    RETURN_CHECK("SSDiLepTreeAlgo::execute()", HelperFunctions::retrieve(systNames, m_elSystsVec, 0, m_store, m_verbose) ,"");
    for(const auto& systName: *systNames){
      elSystNames.push_back(systName);
      if (std::find(event_systNames.begin(), event_systNames.end(), systName) != event_systNames.end()) continue;
      event_systNames.push_back(systName);
    }
  }

  if(!m_jetSystsVec.empty()){
    RETURN_CHECK("SSDiLepTreeAlgo::execute()", HelperFunctions::retrieve(systNames, m_jetSystsVec, 0, m_store, m_verbose) ,"");
    for(const auto& systName: *systNames){
      jetSystNames.push_back(systName);
      if (std::find(event_systNames.begin(), event_systNames.end(), systName) != event_systNames.end()) continue;
      event_systNames.push_back(systName);
    }
  }
  
  if(!m_metSystsVec.empty()){
    RETURN_CHECK("SSDiLepTreeAlgo::execute()", HelperFunctions::retrieve(systNames, m_metSystsVec, 0, m_store, m_verbose) ,"");
    for(const auto& systName: *systNames){
      metSystNames.push_back(systName);
      if (std::find(event_systNames.begin(), event_systNames.end(), systName) != event_systNames.end()) continue;
      event_systNames.push_back(systName);
    }
  }

  TFile* treeFile = wk()->getOutputFile ("tree");

  // let's make the tdirectory and ttrees
  for(const auto& systName: event_systNames){
    // check if we have already created the tree
    if(m_trees.find(systName) != m_trees.end()) continue;
    std::string treeName = systName;
    if(systName.empty()) treeName = "nominal";

    Info("execute()", "Making tree %s/%s", m_name.c_str(), treeName.c_str());
    TTree * outTree = new TTree(treeName.c_str(),treeName.c_str());
    if ( !outTree ) {
      Error("execute()","Failed to instantiate output tree!");
      return EL::StatusCode::FAILURE;
    }

    //m_units = 1e0; // use MeV by default!

    m_trees[systName] = new SSDiLepTree( outTree, treeFile, m_event, m_store, m_units, m_debug, m_DC14, systName );
    SSDiLepTree* helpTree = dynamic_cast<SSDiLepTree*>(m_trees[systName]);

    // tell the tree to go into the file
    outTree->SetDirectory( treeFile->GetDirectory(m_name.c_str()) );
    // choose if want to add tree to same directory as ouput histograms
    if ( m_outHistDir ) {
      if(m_trees.size() > 1) Warning("execute()", "You're running systematics! You may find issues in writing all of the output TTrees to the output histogram file... Set `m_outHistDir = false` if you run into issues!");
      wk()->addOutput( outTree );
    }

    // initialize all branch addresses since we just added this tree
    helpTree->AddEvent( m_evtDetailStr );
    if ( !m_trigDetailStr.empty() )       {   helpTree->AddTrigger    (m_trigDetailStr);    }
    if ( !m_muContainerName.empty() )     {   helpTree->AddMuons      (m_muDetailStr);      }
    if ( !m_elContainerName.empty() )     {   helpTree->AddElectrons  (m_elDetailStr);      }
    if ( !m_jetContainerName.empty() )    {   helpTree->AddJets       (m_jetDetailStr, "jet");     }
    if ( !m_METContainerName.empty() )    {   helpTree->AddMET        (m_METDetailStr);     }
  }

  /* THIS IS WHERE WE START PROCESSING THE EVENT AND PLOTTING THINGS */

  // Get EventInfo and the PrimaryVertices
  const xAOD::EventInfo* eventInfo(nullptr);
  RETURN_CHECK("SSDiLepTreeAlgo::execute()", HelperFunctions::retrieve(eventInfo, m_eventInfoContainerName, m_event, m_store, m_verbose) ,"");
  const xAOD::VertexContainer* vertices(nullptr);
  RETURN_CHECK("SSDiLepTreeAlgo::execute()", HelperFunctions::retrieve(vertices, "PrimaryVertices", m_event, m_store, m_verbose) ,"");
  // get the primaryVertex
  const xAOD::Vertex* primaryVertex = HelperFunctions::getPrimaryVertex( vertices );

  for(const auto& systName: event_systNames){

    SSDiLepTree* helpTree = dynamic_cast<SSDiLepTree*>(m_trees[systName]);

    // assume the nominal container by default
    std::string muSuffix("");
    std::string elSuffix("");
    std::string jetSuffix("");
    std::string metSuffix("");
    //std::string photonSuffix("");
    /*
       if we find the systematic in the corresponding vector, we will use that container's systematic version instead of nominal version
        NB: since none of these contain the "" (nominal) case because of how I filter it, we handle the merging.. why?
        - in each loop to make the ##systNames vectors, we check to see if the systName exists in event_systNames which is initialized
        -   to {""} - the nominal case. If the systName exists, we do not add it to the corresponding ##systNames vector, otherwise, we do.
        -   This precludes the nominal case in all of the ##systNames vectors, which means the default will always be to run nominal.
    */
    if (std::find(muSystNames.begin(), muSystNames.end(), systName) != muSystNames.end()) muSuffix = systName; 
    if (std::find(elSystNames.begin(), elSystNames.end(), systName) != elSystNames.end()) elSuffix = systName; 
    if (std::find(jetSystNames.begin(), jetSystNames.end(), systName) != jetSystNames.end()) jetSuffix = systName; 
    if (std::find(metSystNames.begin(), metSystNames.end(), systName) != metSystNames.end()) metSuffix = systName; 

    helpTree->FillEvent( eventInfo, m_event );

    // Fill trigger information
    if ( !m_trigDetailStr.empty() )    {
      helpTree->FillTrigger( eventInfo );
    }


    // for the containers the were supplied, fill the appropriate vectors
    if ( !m_muContainerName.empty() && m_store->contains<xAOD::MuonContainer>( m_muContainerName+muSuffix ) ) {
      const xAOD::MuonContainer* inMuon(nullptr);
      if ( m_debug ) std::cout << "MuonContainer name: " << m_muContainerName+muSuffix << std::endl;
      RETURN_CHECK("SSDiLepTreeAlgo::execute()", HelperFunctions::retrieve(inMuon, m_muContainerName+muSuffix, m_event, m_store, m_verbose) ,"");
      // sort, and pass the reference to FillMuons()
      const xAOD::MuonContainer inMuonsSorted = HelperFunctions::sort_container_pt( inMuon );
      helpTree->FillMuons( &inMuonsSorted, primaryVertex );
    } else { continue; }
    
    if ( !m_elContainerName.empty() && m_store->contains<xAOD::ElectronContainer>( m_elContainerName+elSuffix ) ) {
      const xAOD::ElectronContainer* inElec(nullptr);
      if ( m_debug ) std::cout << "ElectronContainer name: " << m_elContainerName+elSuffix << std::endl;
      RETURN_CHECK("SSDiLepTreeAlgo::execute()", HelperFunctions::retrieve(inElec, m_elContainerName+elSuffix, m_event, m_store, m_verbose) ,"");
      // sort, and pass the reference to FillElectrons()
      const xAOD::ElectronContainer inElectronsSorted = HelperFunctions::sort_container_pt( inElec );
      helpTree->FillElectrons( &inElectronsSorted, primaryVertex );
    } else { continue; }
    
    if ( !m_jetContainerName.empty() && m_store->contains<xAOD::JetContainer>( m_jetContainerName+jetSuffix ) ) {
      const xAOD::JetContainer* inJets(nullptr);
      if ( m_debug ) std::cout << "JetContainer name: " << m_jetContainerName+jetSuffix << std::endl;
      RETURN_CHECK("SSDiLepTreeAlgo::execute()", HelperFunctions::retrieve(inJets, m_jetContainerName+jetSuffix, m_event, m_store, m_verbose) ,"");
      // sort, and pass the reference to FillJets()
      const xAOD::JetContainer inJetsSorted = HelperFunctions::sort_container_pt( inJets );
      helpTree->FillJets( &inJetsSorted );
    } else { continue; }
    
    if ( !m_METContainerName.empty() && m_store->contains<xAOD::MissingETContainer>( m_METContainerName+metSuffix  ) ) {
      const xAOD::MissingETContainer* inMETCont(nullptr);
      if ( m_debug ) std::cout << "METContainer name: " << m_METContainerName+metSuffix << std::endl;
      RETURN_CHECK("SSDiLepTreeAlgo::execute()", HelperFunctions::retrieve(inMETCont, m_METContainerName+metSuffix, m_event, m_store, m_debug) , "");
      helpTree->FillMET( inMETCont );
    } else { continue; }

    // fill the tree

    helpTree->Fill();

  }

  return EL::StatusCode::SUCCESS;

}
