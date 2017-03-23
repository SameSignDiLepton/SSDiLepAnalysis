#ifndef SSDiLepAnalysis_SSDiLepTree_H
#define SSDiLepAnalysis_SSDiLepTree_H

// package include(s):
#include "xAODAnaHelpers/HelpTreeBase.h"

// EDM include(s):
#include "xAODEventInfo/EventInfo.h"
#include "xAODBase/IParticleContainer.h"
#include "xAODMuon/Muon.h"
#include "xAODEgamma/Electron.h"
#include "xAODJet/Jet.h"
#include "xAODTau/TauJet.h"
#include "xAODCaloEvent/CaloCluster.h"

// Infrastructure include(s):
#include "xAODRootAccess/TEvent.h"

// ROOT include(s):
#include "TTree.h"
#include "TFile.h"

typedef std::pair< std::pair<unsigned int,unsigned int>, char>     dielectron_trigmatch_pair;
typedef std::multimap< std::string, dielectron_trigmatch_pair >    dielectron_trigmatch_pair_map; 

class SSDiLepTree : public HelpTreeBase
{

  private:

    std::string       m_systName;

    /* event variables*/
    int              m_is_mc;
    float            m_KfactorWeight;
    float            m_XS;
    float            m_FiltEff;
    float            m_BornMass;
    std::vector<int>  m_HLpp_Daughters;
    std::vector<int>  m_HLmm_Daughters;
    std::vector<int>  m_HRpp_Daughters;
    std::vector<int>  m_HRmm_Daughters;

    std::vector<int>  m_status3_leptons;
    std::vector<float>       m_KfactorWeightXSAlgo;
    std::vector<std::string>  m_KfactorWeightXSAlgoSysNames;
    
    /* jet variables */
    std::vector<float> m_jet_m;
    std::vector<float> m_jet_isClean;
    std::vector< std::vector < float > > m_jet_jvtSF;

    /* muon variables */
    std::vector<int> m_muon_isTruthMatched;
    std::vector<int> m_muon_truthType;
    std::vector<int> m_muon_truthPdgId;
    std::vector<int> m_muon_truthOrigin;
    std::vector<int> m_muon_truthStatus;

    /* electron variables */
    //std::vector<int>   m_electron_isTruthMatched;
    //std::vector<int>   m_electron_truthPdgId;
    //std::vector<int>   m_electron_truthStatus;
    std::vector<int>   m_electron_truthType;
    std::vector<int>   m_electron_truthOrigin;    

    std::vector<int>   m_electron_bkgTruthType;
    std::vector<int>   m_electron_bkgTruthOrigin;
    std::vector<int>   m_electron_bkgMotherPdgId;
    std::vector<int>   m_electron_firstEgMotherTruthType;
    std::vector<int>   m_electron_firstEgMotherTruthOrigin;
    std::vector<int>   m_electron_firstEgMotherPdgId;

    dielectron_trigmatch_pair_map  m_diElectronTrigMatchPairMap;


  public:

    SSDiLepTree( TTree* tree, TFile* file, xAOD::TEvent* event, xAOD::TStore* store, const float units = 1e3, bool debug = false, bool DC14 = false, std::string systName = "" );
    ~SSDiLepTree();

    void AddEventUser(const std::string detailStrUser = "");
    void AddMuonsUser(const std::string detailStrUser = "");
    void AddElectronsUser(const std::string detailStrUser = "");
    void AddJetsUser(const std::string detailStrUser = "", const std::string = "jet" );

    virtual void ClearEventUser();
    virtual void ClearMuonsUser(const std::string );
    virtual void ClearElectronsUser(const std::string );
    virtual void ClearJetsUser( const std::string );

    virtual void FillEventUser( const xAOD::EventInfo* );
    virtual void FillMuonsUser( const xAOD::Muon*, const std::string );
    virtual void FillElectronsUser( const xAOD::Electron*, const std::string );
    virtual void FillJetsUser( const xAOD::Jet*, const std::string );
};
#endif
