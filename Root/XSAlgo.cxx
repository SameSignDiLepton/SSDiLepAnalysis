/****************************************************************************************
 *
 * An algorithm that performs truth matching and truth-match classification for leptons
 *
 ****************************************************************************************/

// c++ include(s):
#include <iostream>
#include <typeinfo>
#include <sstream>

// EL include(s):
#include <EventLoop/Job.h>
#include <EventLoop/StatusCode.h>
#include <EventLoop/Worker.h>

// EDM include(s):
#include "xAODEventInfo/EventInfo.h"

// package include(s):
#include "SSDiLepAnalysis/XSAlgo.h"
#include "xAODAnaHelpers/HelperClasses.h"
#include "xAODAnaHelpers/HelperFunctions.h"
#include <xAODAnaHelpers/tools/ReturnCheck.h>
#include <xAODAnaHelpers/tools/ReturnCheckConfig.h>

#include "LPXKfactorTool/LPXKfactorTool.h"

// ROOT include(s):
#include "TEnv.h"
#include "TFile.h"
#include "TSystem.h"


// this is needed to distribute the algorithm to the workers
ClassImp(XSAlgo)


XSAlgo :: XSAlgo () :
  m_cutflowHist(nullptr),
  m_cutflowHistW(nullptr)
{
  // Here you put any code for the base initialization of variables,
  // e.g. initialize all pointers to 0.  Note that you should only put
  // the most basic initialization here, since this method will be
  // called on both the submission and the worker node.  Most of your
  // initialization code will go into histInitialize() and
  // initialize().

  Info("XSAlgo()", "Calling constructor");

  m_systNameKfactorTool = "";
  m_systValKfactorTool = 0.0;

  m_doSomething   = false;
}

XSAlgo::~XSAlgo() {}


EL::StatusCode XSAlgo :: setupJob (EL::Job& job)
{
  // Here you put code that sets up the job on the submission object
  // so that it is ready to work with your algorithm, e.g. you can
  // request the D3PDReader service or add output files.  Any code you
  // put here could instead also go into the submission script.  The
  // sole advantage of putting it here is that it gets automatically
  // activated/deactivated when you add/remove the algorithm from your
  // job, which may or may not be of value to you.

  Info("setupJob()", "Calling setupJob");

  job.useXAOD ();
  xAOD::Init( "XSAlgo" ).ignore(); // call before opening first file

  return EL::StatusCode::SUCCESS;
}



EL::StatusCode XSAlgo :: histInitialize ()
{
  // Here you do everything that needs to be done at the very
  // beginning on each worker node, e.g. create histograms and output
  // trees.  This method gets called before any input files are
  // connected.

  Info("histInitialize()", "Calling histInitialize");

  return EL::StatusCode::SUCCESS;
}



EL::StatusCode XSAlgo :: fileExecute ()
{
  // Here you do everything that needs to be done exactly once for every
  // single file, e.g. collect a list of all lumi-blocks processed

  Info("fileExecute()", "Calling fileExecute");

  // Get the MetaData tree once a new file is opened,
  // and check if file is from a DxAOD
  //
  TTree *MetaData = dynamic_cast<TTree*>( wk()->inputFile()->Get("MetaData") );
  if ( !MetaData ) {
    Error("fileExecute()", "MetaData not found! Exiting.");
    return EL::StatusCode::FAILURE;
  }
  MetaData->LoadTree(0);

  m_isDerivation = !MetaData->GetBranch("StreamAOD");

  return EL::StatusCode::SUCCESS;
}



EL::StatusCode XSAlgo :: changeInput (bool /*firstFile*/)
{
  // Here you do everything you need to do when we change input files,
  // e.g. resetting branch addresses on trees.  If you are using
  // D3PDReader or a similar service this method is not needed.

  Info("changeInput()", "Calling changeInput");

  return EL::StatusCode::SUCCESS;
}


EL::StatusCode XSAlgo :: initialize ()
{
  // Here you do everything that you need to do after the first input
  // file has been connected and before the first event is processed,
  // e.g. create additional histograms based on which variables are
  // available in the input files.  You can also create all of your
  // histograms and trees in here, but be aware that this method
  // doesn't get called if no events are processed.  So any objects
  // you create here won't be available in the output if you have no
  // input events.

  Info("initialize()", "Initializing  XSAlgo Interface...");

  m_event = wk()->xaodEvent();
  m_store = wk()->xaodStore();

  const xAOD::EventInfo* eventInfo(nullptr);
  RETURN_CHECK("XSAlgo::execute()", HelperFunctions::retrieve(eventInfo, "EventInfo", m_event, m_store, m_verbose) , "");

  m_isMC = ( eventInfo->eventType( xAOD::EventInfo::IS_SIMULATION ) );

  if ( m_useCutFlow ) {
    TFile *file = wk()->getOutputFile("cutflow");
    m_cutflowHist  = (TH1D*)file->Get("cutflow");
    m_cutflowHistW = (TH1D*)file->Get("cutflow_weighted");
    m_cutflow_bin  = m_cutflowHist->GetXaxis()->FindBin(m_name.c_str());
    m_cutflowHistW->GetXaxis()->FindBin(m_name.c_str());
  }

  Info("initialize()", "Number of events: %lld ", m_event->getEntries() );

  m_numEvent            = 0;
  m_numObject           = 0;
  m_numEventPass        = 0;
  m_weightNumEventPass  = 0;
  m_numObjectPass       = 0;
  
  // decorators
  m_xsDecor        = nullptr ;   m_xsDecor        = new SG::AuxElement::Decorator< double >("xsection");
  m_FiltEffDecor   = nullptr ;   m_FiltEffDecor   = new SG::AuxElement::Decorator< double >("FiltEff");
  m_KFactorDecor   = nullptr ;   m_KFactorDecor   = new SG::AuxElement::Decorator< std::vector<double> >("KfactorWeightXSAlgo");
  m_KFactorDecorSys= nullptr ;   m_KFactorDecorSys= new SG::AuxElement::Decorator< std::vector<std::string> >("KfactorWeightXSAlgoSysNames");
  
  // accessors 
  m_mcEvtWeightAcc = nullptr ;   m_mcEvtWeightAcc = new SG::AuxElement::Accessor< float >("mcEventWeight");
  
  m_p_kfactorTool = new LPXKfactorTool("LPXKfactorTool");
  RETURN_CHECK( "::initialize()", m_p_kfactorTool->setProperty("isMC15",true), "Failed to set MC15 property of LPXKfactorTool" );
  RETURN_CHECK( "::initialize()", m_p_kfactorTool->initialize(), "Failed to properly initialize LPXKfactorTool" );

  // sys
  CP::SystematicSet affectSystsKfactorTool = m_p_kfactorTool->affectingSystematics();
  for ( const auto& syst_it : affectSystsKfactorTool ) { Info("initialize()","XSAlgo can be affected by kfactorTool systematic: %s", (syst_it.name()).c_str()); }

  const CP::SystematicSet SystsKfactorTool = m_p_kfactorTool->recommendedSystematics();
  m_systListKfactorTool = HelperFunctions::getListofSystematics( SystsKfactorTool, m_systNameKfactorTool, m_systValKfactorTool, m_debug );

  Info("initialize()","Will be using XSAlgo systematic:");
  for ( const auto& syst_it : m_systListKfactorTool ) {
    if ( m_systNameKfactorTool.empty() ) {
    Info("initialize()","\t Running w/ nominal configuration only!");
    break;
    }
    Info("initialize()","\t %s", (syst_it.name()).c_str());
  }

  Info("initialize()", " Interface succesfully initialized!" );

  return EL::StatusCode::SUCCESS;
}


EL::StatusCode XSAlgo :: execute ()
{
  // Here you do everything that needs to be done on every single
  // events, e.g. read input variables, apply cuts, and fill
  // histograms and trees.  This is where most of your actual analysis
  // code will go.

  if ( m_debug ) { Info("execute()", "Applying XSAlgo ..."); }

  // retrieve event
  //
  const xAOD::EventInfo* eventInfo(nullptr);
  RETURN_CHECK("XSAlgo::execute()", HelperFunctions::retrieve(eventInfo, "EventInfo", m_event, m_store, m_verbose) , "");


  (*m_xsDecor)( *eventInfo ) = -999.;
  (*m_FiltEffDecor)( *eventInfo ) = -999.;

  std::vector<double> dummyVec;
  dummyVec.push_back(-999);
  (*m_KFactorDecor)( *eventInfo ) = dummyVec;

  std::vector<std::string> dummyVecString;
  dummyVecString.push_back(std::string("empty"));
  (*m_KFactorDecorSys)( *eventInfo ) = dummyVecString;

  //Apply the tool only if we are running on MC..
  if( m_isMC ) {
    std::vector<double> kfactorVec;
    std::vector<std::string> kfactorVecSys;
    static SG::AuxElement::Accessor< double > KfactorWeightAcc("KfactorWeight");
    for ( const auto& syst_it : m_systListKfactorTool ) {
      if ( m_p_kfactorTool->applySystematicVariation(syst_it) != CP::SystematicCode::Ok ) {
        Error("execute()", "Failed to configure XSAlgo for systematic %s", syst_it.name().c_str());
        return EL::StatusCode::FAILURE;
      }
      // KFactor decoration is performed here 
      m_p_kfactorTool->execute();
      if ( KfactorWeightAcc.isAvailable( *eventInfo ) )   {
        kfactorVec.push_back(KfactorWeightAcc( *eventInfo ));
        kfactorVecSys.push_back(syst_it.name());
      }
      else { 
        kfactorVec.push_back(-999.);
        kfactorVecSys.push_back("NotAvailable");
      }
      // convert the xs from the tool in pb
      if ( !syst_it.name().compare("") ) {
        (*m_xsDecor)( *eventInfo ) = m_p_kfactorTool->getMCCrossSection() * 1000.;
        (*m_FiltEffDecor)( *eventInfo ) = m_p_kfactorTool->getMCFilterEfficiency();
      }
    }
    if(kfactorVec.size()>0) {
      (*m_KFactorDecor)( *eventInfo ) = kfactorVec;
      (*m_KFactorDecorSys)( *eventInfo ) = kfactorVecSys;
    }
  }
  
  // MC event weight
  //
  float mcEvtWeight(1.0);
  if ( ! (*m_mcEvtWeightAcc).isAvailable( *eventInfo ) ) {
    Error("execute()", "mcEventWeight is not available as decoration! Aborting" );
    return EL::StatusCode::FAILURE;
  }
  mcEvtWeight = (*m_mcEvtWeightAcc)( *eventInfo );

  m_numEvent++;
  m_numEventPass++;
  m_weightNumEventPass += mcEvtWeight;

  return EL::StatusCode::SUCCESS;
}

EL::StatusCode XSAlgo :: postExecute ()
{
  // Here you do everything that needs to be done after the main event
  // processing.  This is typically very rare, particularly in user
  // code.  It is mainly used in implementing the NTupleSvc.

  if ( m_debug ) { Info("postExecute()", "Calling postExecute"); }

  return EL::StatusCode::SUCCESS;
}

EL::StatusCode XSAlgo :: finalize ()
{
  // This method is the mirror image of initialize(), meaning it gets
  // called after the last event has been processed on the worker node
  // and allows you to finish up any objects you created in
  // initialize() before they are written to disk.  This is actually
  // fairly rare, since this happens separately for each worker node.
  // Most of the time you want to do your post-processing on the
  // submission node after all your histogram outputs have been
  // merged.  This is different from histFinalize() in that it only
  // gets called on worker nodes that processed input events.

  Info("finalize()", "Deleting pointers...");

  delete m_xsDecor;        m_xsDecor = nullptr     ;
  delete m_FiltEffDecor;   m_FiltEffDecor = nullptr;
  delete m_KFactorDecor;   m_KFactorDecor = nullptr;
                                                       
  if ( m_useCutFlow ) {
    Info("finalize()", "Filling cutflow");
    m_cutflowHist ->SetBinContent( m_cutflow_bin, m_numEventPass        );
    m_cutflowHistW->SetBinContent( m_cutflow_bin, m_weightNumEventPass  );
  }

  return EL::StatusCode::SUCCESS;
}

EL::StatusCode XSAlgo :: histFinalize ()
{
  // This method is the mirror image of histInitialize(), meaning it
  // gets called after the last event has been processed on the worker
  // node and allows you to finish up any objects you created in
  // histInitialize() before they are written to disk.  This is
  // actually fairly rare, since this happens separately for each
  // worker node.  Most of the time you want to do your
  // post-processing on the submission node after all your histogram
  // outputs have been merged.  This is different from finalize() in
  // that it gets called on all worker nodes regardless of whether
  // they processed input events.

  Info("histFinalize()", "Calling histFinalize");

  return EL::StatusCode::SUCCESS;
}





