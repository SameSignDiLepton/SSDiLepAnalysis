#!/usr/bin/env python
import ROOT
import os
from optparse import OptionParser

from xAH_config import xAH_config

# Hack to force just-in-time libraries to load,
# needed for Muon quality enum. Ask gstark@cern.ch for questions.
#
alg = ROOT.xAH.Algorithm()
del alg

do_HIGG3D3 = True
kernel = "HIGG3D3Kernel"
use_truth_mu_cont = True

if not do_HIGG3D3:
  kernel = "EXOT12Kernel"
  use_truth_mu_cont = False


# electron triggers
trig_el = []

# muon triggers
trig_single_mu = []
trig_single_mu.append('HLT_mu20_L1MU15')
trig_single_mu.append('HLT_mu24')
trig_single_mu.append('HLT_mu24_L1MU15')
trig_single_mu.append('HLT_mu24_imedium')     # new trigger !
trig_single_mu.append('HLT_mu26_imedium')
trig_single_mu.append('HLT_mu26_ivarmedium')
trig_single_mu.append('HLT_mu50')

trig_di_mu = []
trig_di_mu.append('HLT_2mu14')
#trig_di_mu.append('HLT_mu22_mu8noL1')

single_mu_triglist = ",".join(trig_single_mu)
di_mu_triglist = ",".join(trig_di_mu)

# all triggers
all_triggers = trig_el + trig_single_mu + trig_di_mu
triglist = ",".join(all_triggers)


# muon corrections
mu_trig_corr = []
mu_trig_corr.append("HLT_mu14")
mu_trig_corr.append("HLT_mu22")
mu_trig_corr.append("HLT_mu24")
mu_trig_corr.append("HLT_mu8noL1")
mu_trig_corr.append("HLT_mu50")
mu_trig_corr.append("HLT_mu26_imedium")
mu_trig_corr.append("HLT_mu26_imedium_OR_HLT_mu50")
mu_trig_corr.append("HLT_mu26_ivarmedium")
mu_trig_corr.append("HLT_mu26_ivarmedium_OR_HLT_mu50")
mu_trig_corr.append("HLT_mu24_imedium")
mu_trig_corr.append("HLT_mu24_imedium_OR_HLT_mu50")


mu_reco_corr = []
#mu_reco_corr.append("Loose")
mu_reco_corr.append("Medium")

mu_iso_corr = []
#mu_iso_corr.append("Loose")
mu_iso_corr.append("Gradient")
#mu_iso_corr.append("GradientLoose")
mu_iso_corr.append("FixedCutTightTrackOnly")

# build list
trig_branches = []
for t in mu_trig_corr:
  for r in mu_reco_corr:
    for i in mu_iso_corr:
      trig_branches.append("_".join([t,"Reco%s"%r,"Iso%s"%i]))



# list of years for configuring 
# the trigger scale factor tool

mutrigeffYears = "2015,2016"

# This is just a RootCore path!!!
path_ext = "$ROOTCOREBIN/data/SSDiLepAnalysis/External"

# ------------------------------------------------------------------------------------
# GRLs:
#      https://twiki.cern.ch/twiki/bin/view/AtlasProtected/GoodRunListsForAnalysisRun2
# ------------------------------------------------------------------------------------
GRL_list = []
GRL_list.append(os.path.join(path_ext,"data15_13TeV.periodAllYear_DetStatus-v79-repro20-02_DQDefects-00-02-02_PHYS_StandardGRL_All_Good_25ns.xml"))
#GRL_list.append(os.path.join(path_ext,"data16_13TeV.periodAllYear_DetStatus-v83-pro20-15_DQDefects-00-02-04_PHYS_StandardGRL_All_Good_25ns.xml"))
GRL_list.append(os.path.join(path_ext,"data16_13TeV.periodAllYear_DetStatus-v88-pro20-21_DQDefects-00-02-04_PHYS_StandardGRL_All_Good_25ns.xml"))
GRL_config = ",".join(GRL_list)


# ------------------
# Lumi config
# ------------------
LUMICALC_files = []
LUMICALC_files.append(os.path.join(path_ext,"ilumicalc_histograms_None_276262-284484_OflLumi-13TeV-005.root"))
LUMICALC_files.append(os.path.join(path_ext,"ilumicalc_histograms_None_297730-311481_OflLumi-13TeV-005.root"))
LUMICALC_config = ','.join(LUMICALC_files)

BasicEventSelectionDict = {"m_name"                       : "SSDiLep",
                           "m_debug"                      : False,
                           "m_applyGRLCut"                : True,
                           "m_GRLxml"                     : GRL_config,
                           "m_doPUreweighting"            : True,
                           "m_reweightSherpa22"           : True,
                           "m_PRWFileNames"               : "dev/PileupReweighting/mc15c_v2_defaults.NotRecommended.prw.root",
                           "m_lumiCalcFileNames"          : LUMICALC_config,
                           "m_useMetaData"                : True,
                           "m_derivationName"             : kernel,
                           "m_applyPrimaryVertexCut"      : True,
                           "m_vertexContainerName"        : "PrimaryVertices",
                           #"m_PVNTrack"                   : 0,  #### remove the legacy run-1 cut
                           "m_applyEventCleaningCut"      : True,
                           "m_truthLevelOnly"             : False,
                           "m_applyCoreFlagsCut"          : True,
                           "m_checkDuplicatesData"        : True,
                           "m_checkDuplicatesMC"          : True,
                           "m_applyTriggerCut"            : False,
                           "m_triggerSelection"           : triglist,
                           "m_storeTrigDecisions"         : True,
                           "m_storePassHLT"               : True,
                           }
                                                          
#https://twiki.cern.ch/twiki/bin/view/AtlasProtected/ApplyJetCalibration2016
JetCalibratorDict =      { "m_name"                       : "jetCalib_AntiKt4EMTopo",
                           "m_debug"                      : False,
                           "m_inContainerName"            : "AntiKt4EMTopoJets",
                           "m_jetAlgo"                    : "AntiKt4EMTopo",
                           "m_outContainerName"           : "AntiKt4EMTopoJets_Calib",
                           "m_outputAlgo"                 : "JetCalibrator_Syst",
                           "m_sort"                       : True,
                           "m_calibSequence"              : "JetArea_Residual_Origin_EtaJES_GSC",
                           "m_calibConfigAFII"            : "JES_MC15Prerecommendation_AFII_June2015.config",
                           "m_calibConfigFullSim"         : "JES_data2016_data2015_Recommendation_Dec2016.config",
                           "m_calibConfigData"            : "JES_data2016_data2015_Recommendation_Dec2016.config",
                           "m_JESUncertConfig"            : "$ROOTCOREBIN/data/JetUncertainties/JES_2016/Moriond2017/JES2016_AllNuisanceParameters.config",
                           "m_JESUncertMCType"            : "MC15",
                           "m_JERUncertConfig"            : "JetResolution/Prerec2015_xCalib_2012JER_ReducedTo9NP_Plots_v2.root",
                           "m_JERApplyNominal"            : False,
                           "m_JERFullSys"                 : False,
                           "m_jetCleanCutLevel"           : "LooseBad",
                           "m_jetCleanUgly"               : False,
                           "m_cleanParent"                : False,
                           "m_saveAllCleanDecisions"      : True,
                           "m_redoJVT"                    : True
                         }
                                                          
                                                          
MuonCalibratorDict =     { "m_name"                       : "muonCalib",
                           "m_debug"                      : False,
                           "m_forceDataCalib"             : True,
                           "m_inContainerName"            : "Muons",
                           "m_outContainerName"           : "Muons_Calib",
                           "m_inputAlgoSystNames"         : "",
                           "m_outputAlgoSystNames"        : "MuonCalibrator_Syst",
                           "m_systName"                   : "All",
                           "m_systVal"                    : 1.0,
                           "m_Years"                      : "Data16,Data15",
                           "m_do_sagittaCorr"             : True,
                           "m_sagittaRelease"             : "sagittaBiasDataAll_06_02_17",
                           "m_do_sagittaMCDistortion"     : False,
                         }
"""                                                          
ElectronCalibratorDict = { "m_name"                       : "electronCalib",
                           "m_debug"                      : False,
                           "m_inContainerName"            : "Electrons",
                           "m_outContainerName"           : "Electrons_Calib",
                           "m_inputAlgoSystNames"         : "",
                           "m_outputAlgoSystNames"        : "ElectronCalibrator_Syst",
                           "m_esModel"                    : "es2016PRE",               
                           "m_decorrelationModel"         : "FULL_v1",
                           "m_systName"                   : "",
                           "m_systVal"                    : 0.0,
                         }                                
"""                                                          
                                                          
JetSelectorDict =        { "m_name"                       :  "jetSelect_selection",
                           "m_debug"                      :  False,
                           "m_inContainerName"            :  "AntiKt4EMTopoJets_Calib",
                           "m_jetScaleType"               :  "JetLCScaleMomentum", # EM scale removed from EXOT12
                           "m_outContainerName"           :  "AntiKt4EMTopoJets_Selected",
                           "m_inputAlgo"                  :  "",
                           "m_outputAlgo"                 :  "JetSelector_Syst",
                           "m_createSelectedContainer"    :  True,
                           "m_decorateSelectedObjects"    :  True,
                           "m_useCutFlow"                 :  True,
                           "m_pT_min"                     :  20e3,
                           "m_eta_max"                    :  2.5,
                           "m_doJVT"                      :  True,
                           "m_pt_max_JVT"                 :  60e3,
                           "m_eta_max_JVT"                :  2.4,
                           "m_JVTCut"                     :  0.59,
                           "m_doBTagCut"                  :  False,
                           "m_operatingPt"                :  "FixedCutBEff_77",
                           "m_cleanJets"                  :  False, ####  we have to perform event cleaning after OR (in ntuples)
                                                                    ####  https://twiki.cern.ch/twiki/bin/view/AtlasProtected/HowToCleanJets2016
                         }
                                                          
                                                          
MuonSelectorDict =       { "m_name"                       : "muonSelect_selection",
                           "m_debug"                      : False,
                           "m_inContainerName"            : "Muons_Calib",
                           "m_outContainerName"           : "Muons_Selected",
                           "m_inputAlgoSystNames"         : "MuonCalibrator_Syst",
                           "m_outputAlgoSystNames"        : "MuonSelector_Syst",
                           "m_createSelectedContainer"    : True,
                           "m_decorateSelectedObjects"    : True,
                           "m_pass_min"                   : 0,
                           "m_pass_max"                   : 1000,
                           "m_pT_min"                     : 20e3, # min pT of derivations
                           "m_eta_max"                    : 2.5,
                           "m_muonQualityStr"             : "Medium",
                           "m_d0sig_max"                  : 10.0,
                           "m_z0sintheta_max"             : 10.0,
                           "m_MinIsoWPCut"                : "",
                           "m_IsoWPList"                  : ",".join(mu_iso_corr),
                           "m_CaloIsoEff"                 : "0.1*x",
                           "m_TrackIsoEff"                : "0.1*x",
                           "m_CaloBasedIsoType"           : "topoetcone20",
                           "m_TrackBasedIsoType"          : "ptvarcone30",
                           "m_singleMuTrigChains"         : single_mu_triglist,
                         }
                                                          
"""                                                          
ElectronSelectorDict =   { "m_name"                       : "electronSelect_selection",
                           "m_debug"                      : False,
                           "m_inContainerName"            : "Electrons_Calib",
                           "m_outContainerName"           : "Electrons_Selected",
                           "m_inputAlgoSystNames"         : "ElectronCalibrator_Syst",
                           "m_outputAlgoSystNames"        : "ElectronSelector_Syst",
                           "m_createSelectedContainer"    : True,
                           "m_decorateSelectedObjects"    : True,
                           "m_pass_min"                   : 0,
                           "m_pass_max"                   : 1000,
                           "m_pT_min"                     : 10e3,
                           "m_eta_max"                    : 2.47,
                           "m_vetoCrack"                  : True,
                           "m_d0sig_max"                  : 10.0,
                           "m_z0sintheta_max"             : 2.0,
                           "m_doAuthorCut"                : True,
                           "m_doOQCut"                    : True, 
                           "m_doBLTrackQualityCut"        : True, # set this to True if reading ID flags from DAOD
                           "m_readIDFlagsFromDerivation"  : True,
                           "m_doLHPIDcut"                 : True, 
                           "m_LHOperatingPoint"           : "Loose", # for loose ID, use "LooseAndBLayer" if NOT reading ID flags from DAOD
                           "m_doCutBasedPIDcut"           : False,
                           "m_CutBasedOperatingPoint"     : "Loose",
                           "m_IsoWPList"                  : "Loose,GradientLoose,Gradient,FixedCutLoose,FixedCutTight,FixedCutTightTrackOnly,UserDefinedCut",
                           "m_CaloIsoEff"                 : "0.05*x",
                           "m_TrackIsoEff"                : "0.05*x",
                           "m_CaloBasedIsoType"           : "topoetcone20",
                           "m_TrackBasedIsoType"          : "ptvarcone20",
                           #"m_ElTrigChains"               : "HLT_2e12_lhloose_L12EM10VH",
                           #"m_ElTrigChains"               : "",
                         }                                
"""                                                          

METConstructorDict =     { "m_name"                       : "met",
                           "m_debug"                      : False,
                           "m_referenceMETContainer"      : "MET_Reference_AntiKt4EMTopo",
                           "m_mapName"                    : "METAssoc_AntiKt4EMTopo",
                           "m_coreName"                   : "MET_Core_AntiKt4EMTopo",
                           "m_outputContainer"            : "RefFinal_SSDiLep",
                           #"m_doPhotonCuts"               : True,
                           "m_useCaloJetTerm"             : True,
                           "m_useTrackJetTerm"            : False,
                           #"m_inputElectrons"             : "Electrons_Selected",
                           #"m_inputPhotons"               : "Photons",
                           "m_inputMuons"                 : "Muons_Selected",
                           #"m_inputJets"                  : "AntiKt4EMTopoJets_Calib",
                           "m_inputJets"                  : "AntiKt4EMTopoJets_Selected",
                           "m_doJVTCut"                   : True,
                         }


OverlapRemoverDict =     { "m_name"                       : "overlap_removal_SSDiLep",
                           "m_debug"                      : False,
                           "m_useCutFlow"                 : True,
                           "m_createSelectedContainers"   : True,
                           "m_decorateSelectedObjects"    : True,
                           "m_useSelected"                : True,
                           "m_inContainerName_Muons"      : "Muons_Selected",
                           "m_outContainerName_Muons"     : "Muons_OR",
                           "m_inputAlgoMuons"             : "MuonCalibrator_Syst",
                           #"m_inContainerName_Electrons"  : "Electrons_Selected",
                           #"m_outContainerName_Electrons" : "Electrons_OR",
                           #"m_inputAlgoElectrons"         : "ElectronCalibrator_Syst",
                           "m_inContainerName_Jets"       : "AntiKt4EMTopoJets_Selected",
                           "m_outContainerName_Jets"      : "AntiKt4EMTopoJets_OR",
                           "m_inputAlgoJets"              : "",
                           "m_inputAlgoTaus"              : "",
                         }

# --------------------
# muon corrections
# --------------------

# name of config: reco+id wp

MuonEfficiencyCorrectorMediumGradientDict = {  "m_name"                  : "muonEfficiencyCorrectorMediumGradient",
                                      "m_debug"                 : False,
                                      "m_inContainerName"       : "Muons_OR",
                                      "m_inputAlgoSystNames"    : "MuonSelector_Syst",
                                      "m_systNameReco"          : "All",
                                      "m_systNameIso"           : "All",
                                      "m_systNameTrig"          : "All",
                                      "m_systNameTTVA"          : "All",
                                      "m_systValReco"           : 1.0,
                                      "m_systValIso"            : 1.0,
                                      "m_systValTrig"           : 1.0,
                                      "m_systValTTVA"           : 1.0,
                                      "m_useRandomRunNumber"    : True,
                                      "m_AllowZeroSF"           : True,
                                      "m_Years"                 : mutrigeffYears,
                                      "m_outputSystNamesReco"   : "MuonEfficiencyCorrector_RecoSyst",
                                      "m_outputSystNamesIso"    : "MuonEfficiencyCorrector_IsoSyst",
                                      "m_outputSystNamesTrig"   : "MuonEfficiencyCorrector_TrigSyst",
                                      "m_outputSystNamesTTVA"   : "MuonEfficiencyCorrector_TTVASyst",
                                      "m_calibRelease"          : "160928_PostICHEP",
                                      "m_WorkingPointReco"      : "Medium",
                                      "m_WorkingPointIso"       : "Gradient",
                                      "m_WorkingPointRecoTrig"  : "Medium",
                                      "m_WorkingPointIsoTrig"   : "Gradient",
                                      "m_WorkingPointTTVA"      : "TTVA",
                                      "m_MuTrigLegs"            : ",".join(mu_trig_corr),
                                    }


MuonEfficiencyCorrectorMediumFixedCutTightTrackOnlyDict = {  "m_name"                  : "muonEfficiencyCorrectorMediumFixedCutTightTrackOnly",
                                      "m_debug"                 : False,
                                      "m_inContainerName"       : "Muons_OR",
                                      "m_inputAlgoSystNames"    : "MuonSelector_Syst",
                                      "m_systNameReco"          : "All",
                                      "m_systNameIso"           : "All",
                                      "m_systNameTrig"          : "All",
                                      "m_systNameTTVA"          : "All",
                                      "m_systValReco"           : 1.0,
                                      "m_systValIso"            : 1.0,
                                      "m_systValTrig"           : 1.0,
                                      "m_systValTTVA"           : 1.0,
                                      "m_useRandomRunNumber"    : True,
                                      "m_AllowZeroSF"           : True,
                                      "m_Years"                 : mutrigeffYears,
                                      "m_outputSystNamesReco"   : "MuonEfficiencyCorrector_RecoSyst",
                                      "m_outputSystNamesIso"    : "MuonEfficiencyCorrector_IsoSyst",
                                      "m_outputSystNamesTrig"   : "MuonEfficiencyCorrector_TrigSyst",
                                      "m_outputSystNamesTTVA"   : "MuonEfficiencyCorrector_TTVASyst",
                                      "m_calibRelease"          : "160928_PostICHEP",
                                      "m_WorkingPointReco"      : "Medium",
                                      "m_WorkingPointIso"       : "FixedCutTightTrackOnly",
                                      "m_WorkingPointRecoTrig"  : "Medium",
                                      "m_WorkingPointIsoTrig"   : "FixedCutTightTrackOnly",
                                      "m_WorkingPointTTVA"      : "TTVA",
                                      "m_MuTrigLegs"            : ",".join(mu_trig_corr),
                                    }

# Truth matching info just for muons
TruthMatchAlgoDict       = { "m_name"                           : "truthMatching",
                             "m_debug"                          : False,
                             #"m_inContainerName_Electrons"      : "Electrons_OR",
                             "m_inContainerName_Muons"          : "Muons_OR",
                             "m_doMuonTruthContMatching"        : use_truth_mu_cont,
                           }

XSAlgoDict               = { "m_name"                           : "xsalgo",
                             "m_debug"                          : False,
                           }


SSDiLepTreeAlgoDict      = { "m_name"                   : "physics",
                             "m_debug"                 : False,
                             "m_muContainerName"       : "Muons_OR",
                             #"m_elContainerName"       : "Electrons_OR",
                             "m_jetContainerName"      : "AntiKt4EMTopoJets_OR",
                             "m_METContainerName"      : "RefFinal_SSDiLep",
                             "m_outHistDir"            : False,
                             "m_evtDetailStr"          : "pileup",
                             "m_trigDetailStr"         : "basic passTriggers menuKeys",
                             "m_muDetailStr"           : "kinematic trigger isolation quality trackparams effSF " + " ".join(trig_branches) + " Reco" + " Reco".join(mu_reco_corr) + " Iso" + " Iso".join(mu_iso_corr) + " isoEff_sysNames recoEff_sysNames trigEff_sysNames ttvaEff_sysNames",
                             #"m_elDetailStr"           : "kinematic trigger isolation PID trackparams effSF",
                             "m_jetDetailStr"          : "kinematic energy flavorTag sfFTagFix77 truth",
                             "m_METDetailStr"          : "RefEle RefGamma Muons RefJet RefJetTrk SoftClus PVSoftTrk",
                           }

