#!/usr/bin/env python
import ROOT
import os
from optparse import OptionParser

from xAH_config import xAH_config

#This config file has been used for v1 ntuple submission ---> For EXOT12 and EXOT19!


# ROOT config files like ilumicalc, PRW and GRLs are kept here:
# https://www.dropbox.com/sh/19kljimhoo1ntjd/AADjOdx7xDK5YaHQywtuD6x2a?dl=0


# Hack to force just-in-time libraries to load,
# needed for Muon quality enum. Ask gstark@cern.ch for questions.
#
alg = ROOT.xAH.Algorithm()
del alg

# electron triggers
trig_el = []
trig_el.append('HLT_e24_lhmedium_L1EM20VH')   
trig_el.append('HLT_e24_lhmedium_L1EM18VH')   
trig_el.append('HLT_e60_lhmedium')   
trig_el.append('HLT_e120_lhloose')   
trig_el.append('HLT_2e17_lhloose')   
#Trigger added for other studies
trig_el.append('HLT_e26_lhtight_nod0_ivarloos')
trig_el.append('HLT_e60_lhmedium_nod0')
trig_el.append('HLT_e140_lhloose_nod0')
trig_el.append('HLT_2e17_lhvloose_nod0')
trigellist = ",".join(trig_el)

# muon triggers
trig_mu = []
trig_mu.append('HLT_mu26_imedium')
trig_mu.append('HLT_mu50')
#Trigger added for other studies
trig_mu.append('HLT_mu26_ivarmedium')
trigmulist = ",".join(trig_mu)

trig_mumu = []
trig_mumu.append('HLT_2mu14')
trig_mumu.append('HLT_mu22_mu8noL1')
trigmumulist = ",".join(trig_mumu)

#dilepton emu triggers
trig_emu = [] 
trig_emu.append('HLT_e17_lhloose_nod0_mu14')
trig_emu.append('HLT_e26_lhmedium_nod0_L1EM22VHI_mu8noL1')
trig_emu.append('HLT_e7_lhmedium_nod0_mu24')
trigemulist=",".join(trig_emu)

trigMuMuEMulist=",".join(trig_emu+trig_mumu)

# all triggers
all_triggers = trig_el + trig_mu + trig_emu + trig_mumu
triglist = ",".join(all_triggers)


# list of years for configuring 
# the trigger scale factor tool

mutrigeffYears = "2015,2016"

# This is just a RootCore path!!!
path_ext = "$ROOTCOREBIN/data/SSDiLepAnalysis/ExternalMerged"

# merged
GRL_file = os.path.join(path_ext,
    "merged_GRL_2015_2016.xml")

# 2015
#GRL_file = os.path.join(path_ext,
#   "data15_13TeV.periodAllYear_DetStatus-v79-repro20-02_DQDefects-00-02-02_PHYS_StandardGRL_All_Good_25ns.xml")

# 2016
#GRL_file = os.path.join(path_ext,
#    "data16_13TeV.periodAllYear_DetStatus-v81-pro20-10_DQDefects-00-02-02_PHYS_StandardGRL_All_Good_25ns.xml")


#-------------------
# PileUp reweighting
#-------------------
# One should not pass these files 
# as an external reading of directories

LUMICALC_files = []

# ------
# merged
# ------
LUMICALC_files.append("ilumicalc_histograms_None_276262-304494_OflLumi-13TeV-005.root")

# prescaled
#LUMICALC_files.append("ilumicalc_histograms_HLT_mu20_L1MU15_276262-304494_OflLumi-13TeV-005.root:HLT_mu20_L1MU15")
#LUMICALC_files.append("ilumicalc_histograms_HLT_mu24_276262-304494_OflLumi-13TeV-005.root:HLT_mu24")

# unprescaled
LUMICALC_files.append("ilumicalc_histograms_HLT_mu26_imedium_276262-304494_OflLumi-13TeV-005.root:HLT_mu26_imedium")
LUMICALC_files.append("ilumicalc_histograms_HLT_mu50_276262-304494_OflLumi-13TeV-005.root:HLT_mu50")


# ------
# 2015
# ------
#LUMICALC_files.append("ilumicalc_histograms_None_276262-284484_OflLumi-13TeV-005.root")

# prescaled
#LUMICALC_files.append("ilumicalc_histograms_HLT_mu20_L1MU15_276262-284484_OflLumi-13TeV-005.root:HLT_mu20_L1MU15")
#LUMICALC_files.append("ilumicalc_histograms_HLT_mu24_276262-284484_OflLumi-13TeV-005.root:HLT_mu24")

# unprescaled
#LUMICALC_files.append("ilumicalc_histograms_HLT_mu26_imedium_276262-284484_OflLumi-13TeV-005.root:HLT_mu26_imedium")
#LUMICALC_files.append("ilumicalc_histograms_HLT_mu50_276262-284484_OflLumi-13TeV-005.root:HLT_mu50")


# ------
# 2016
# ------
#LUMICALC_files.append("ilumicalc_histograms_None_297730-304494_OflLumi-13TeV-005.root")

# prescaled
#LUMICALC_files.append("ilumicalc_histograms_HLT_mu20_L1MU15_297730-304494_OflLumi-13TeV-005.root:HLT_mu20_L1MU15")
#LUMICALC_files.append("ilumicalc_histograms_HLT_mu24_297730-304494_OflLumi-13TeV-005.root:HLT_mu24")

# unprescaled
#LUMICALC_files.append("ilumicalc_histograms_HLT_mu50_297730-304494_OflLumi-13TeV-005.root:HLT_mu26_imedium")
#LUMICALC_files.append("ilumicalc_histograms_HLT_mu26_imedium_297730-304494_OflLumi-13TeV-005.root:HLT_mu50")


for idx,file in enumerate(LUMICALC_files):
  LUMICALC_files[idx] = os.path.join(path_ext,file)
LUMICALC_config = ','.join(LUMICALC_files)


PRW_files = []
PRW_files.append("PRW_mc15c_410000_ttbar_nonallhad.root") 


for idx,file in enumerate(PRW_files):
    PRW_files[idx] = os.path.join(path_ext,file)
PRW_config = ','.join(PRW_files)

##path_el_eff = "ElectronEfficiencyCorrection/2015_2016/rel20.7/ICHEP_June2016_v3/"

BasicEventSelectionDict = {"m_name"                       : "SSDiLep", 
                           "m_debug"                      : False,
                           "m_applyGRLCut"                : True,
                           "m_GRLxml"                     : GRL_file,
                           "m_doPUreweighting"            : True,
                           "m_PU_default_channel"         : 410000,
                           "m_lumiCalcFileNames"          : LUMICALC_config,
                           "m_PRWFileNames"               : PRW_config,
                           "m_useMetaData"                : True, 
                           "m_derivationName"             : "EXOT12Kernel",
                           "m_vertexContainerName"        : "PrimaryVertices", 
                           "m_PVNTrack"                   : 3,
                           "m_applyPrimaryVertexCut"      : True,
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
                                                          
                                                          
JetCalibratorDict =      { "m_name"                       : "jetCalib_AntiKt4EMTopo",
                           "m_debug"                      : False,
                           "m_inContainerName"            : "AntiKt4EMTopoJets",
                           "m_jetAlgo"                    : "AntiKt4EMTopo",
                           "m_outContainerName"           : "AntiKt4EMTopoJets_Calib",
                           "m_outputAlgo"                 : "JetCalibrator_Syst",
                           "m_sort"                       : True,
                           "m_calibSequence"              : "JetArea_Residual_Origin_EtaJES_GSC",
                           "m_calibConfigAFII"            : "JES_MC15Prerecommendation_AFII_June2015.config",
                           "m_calibConfigFullSim"         : "JES_MC15cRecommendation_May2016.config",
                           "m_calibConfigData"            : "JES_MC15cRecommendation_May2016.config",
                           "m_JESUncertConfig"            : "$ROOTCOREBIN/data/JetUncertainties/JES_2015/ICHEP2016/JES2015_AllNuisanceParameters.config",
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
                           "m_release"                    : "Recs2016_08_07", 
                           "m_systName"                   : "",
                           "m_systVal"                    : 0.0,
                         }                                
                                                          
                                                          
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
                           "m_pT_min"                     :  25e3,
                           "m_eta_max"                    :  2.5,
                           "m_doJVT"                      :  True,
                           "m_pt_max_JVT"                 :  50e3,
                           "m_eta_max_JVT"                :  2.4,
                           "m_JVTCut"                     :  0.64,
                           "m_doBTagCut"                  :  False,
                           "m_operatingPt"                :  "FixedCutBEff_77",
                         }                                
                                                          
                                                          
MuonSelectorDict =       { "m_name"                       : "muonSelect_selection",
                           "m_debug"                      : True,
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
                           "m_muonType"                   : "Combined",
                           "m_muonQualityStr"             : "Loose",
                           "m_d0sig_max"                  : 20.0,
                           "m_z0sintheta_max"             : 20.0,
                           "m_MinIsoWPCut"                : "",
                           "m_IsoWPList"                  : "Loose,GradientLoose,Gradient,FixedCutTightTrackOnly,UserDefinedCut",
                           "m_CaloIsoEff"                 : "0.1*x",
                           "m_TrackIsoEff"                : "0.1*x",
                           "m_CaloBasedIsoType"           : "topoetcone20",
                           "m_TrackBasedIsoType"          : "ptvarcone30",
                           "m_singleMuTrigChains"         : trigmulist,
                           "m_diMuTrigChains"             : trigMuMuEMulist,
                         }                                
                                                          
                                                          
ElectronSelectorDict = { "m_name"                      : "electronSelect_selection",
                         "m_debug"                     :  True,
                         "m_inContainerName"           : "Electrons_Calib",
                         "m_outContainerName"          : "Electrons_Selected",
                         "m_inputAlgoSystNames"        : "ElectronCalibrator_Syst",
                         "m_outputAlgoSystNames"       : "ElectronSelector_Syst",
                         "m_createSelectedContainer"   : True,
                         "m_decorateSelectedObjects"   : True,
                         "m_pass_min"                  : 0,
                         "m_pT_min"                    : 10e3,
                         "m_eta_max"                   : 2.47,
                         "m_vetoCrack"                 : True,
                         "m_d0sig_max"                 : 10.0,
                         "m_z0sintheta_max"            : 2.0,
                         "m_doAuthorCut"               : False,
                         "m_doOQCut"                   : False,
                         "m_doBLTrackQualityCut"       : True, # set this to True if reading ID flags from DAOD
                         "m_readIDFlagsFromDerivation" : True,
                         "m_confDirPID"                : "mc15_20160113",
                         "m_doLHPIDcut"                : True,
                         "m_LHOperatingPoint"          : "Loose", # for loose ID, use "LooseAndBLayer" if NOT reading ID flags from DAOD
                         "m_doCutBasedPIDcut"          : False,
                         "m_CutBasedOperatingPoint"    : "IsEMLoose",
                         "m_CutBasedConfigYear"        : "",
                         "m_IsoWPList"                 : "LooseTrackOnly,Loose,GradientLoose,Gradient,FixedCutLoose,FixedCutTight,FixedCutTightTrackOnly,Tight",
                         "m_CaloIsoEff"                : "0.05*x",
                         "m_TrackIsoEff"               : "0.05*x",
                         "m_CaloBasedIsoType"          : "topoetcone20",
                         "m_TrackBasedIsoType"         : "ptvarcone20",
                         "m_singleElTrigChains"        : "HLT_e24_lhmedium_L1EM20VH,HLT_e24_lhmedium_L1EM18VH,HLT_e60_lhmedium,HLT_e120_lhloose,HLT_e26_lhtight_nod0_ivarloose,HLT_e60_lhmedium_nod0 ,HLT_e140_lhloose_nod0",
                         "m_diElTrigChains"            : "HLT_2e12_lhloose_L12EM10VH,HLT_2e15_lhvloose_nod0_L12EM13VH,HLT_2e17_lhloose,HLT_2e17_lhvloose_nod0,HLT_e17_lhloose_nod0_mu14,HLT_e26_lhmedium_nod0_L1EM22VHI_mu8noL1,HLT_e7_lhmedium_nod0_mu24",
                         }                               
                                                          
                                                          
                                                          
METConstructorDict =     { "m_name"                       : "met",
                           "m_debug"                      : False,
                           "m_referenceMETContainer"      : "MET_Reference_AntiKt4EMTopo",
                           "m_mapName"                    : "METAssoc_AntiKt4EMTopo",
                           "m_coreName"                   : "MET_Core_AntiKt4EMTopo",
                           "m_outputContainer"            : "RefFinal_SSDiLep",
                           "m_doPhotonCuts"               : True,
                           "m_useCaloJetTerm"             : True,
                           "m_useTrackJetTerm"            : False,                     
                           "m_inputElectrons"             : "Electrons_Selected",     
                           "m_inputPhotons"               : "Photons",                 
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
                           "m_inputAlgoMuons"             : "",
                           "m_inContainerName_Electrons"  : "Electrons_Selected",
                           "m_outContainerName_Electrons" : "Electrons_OR",
                           "m_inputAlgoElectrons"         : "",
                           "m_inContainerName_Jets"       : "AntiKt4EMTopoJets_Selected",
                           "m_outContainerName_Jets"      : "AntiKt4EMTopoJets_OR",
                           "m_inputAlgoJets"              : "",
                           "m_inputAlgoTaus"              : "",
                         }

# --------------------
# muon corrections
# --------------------

# name of config: reco+id wp

MuonEfficiencyCorrectorLooseLooseDict = {  "m_name"                  : "muonEfficiencyCorrectorLooseLoose",
                                      "m_debug"                 : False,
                                      "m_inContainerName"       : "Muons_OR",
                                      "m_inputAlgoSystNames"    : "MuonSelector_Syst",
                                      "m_systNameReco"          : "",
                                      "m_systNameIso"           : "",
                                      "m_systNameTrig"          : "",
                                      "m_systNameTTVA"          : "",
                                      "m_useRandomRunNumber"    : True,
                                      "m_Years"                 : mutrigeffYears,
                                      "m_outputSystNamesReco"   : "MuonEfficiencyCorrector_RecoSyst",
                                      "m_outputSystNamesIso"    : "MuonEfficiencyCorrector_IsoSyst",
                                      "m_outputSystNamesTrig"   : "MuonEfficiencyCorrector_TrigSyst",
                                      "m_outputSystNamesTTVA"   : "MuonEfficiencyCorrector_TTVASyst",
                                      "m_calibRelease"          : "160624_ICHEP",
                                      "m_WorkingPointReco"      : "Loose",
                                      "m_WorkingPointIso"       : "Loose",
                                      "m_WorkingPointRecoTrig"  : "Loose",
                                      "m_WorkingPointIsoTrig"   : "Loose",
                                      "m_WorkingPointTTVA"      : "TTVA",
                                      "m_SingleMuTrig"          : "HLT_mu26_imedium_OR_HLT_mu50",
                                      "m_DiMuTrig"              : "",
                                    }


MuonEfficiencyCorrectorLooseGradientDict = {  "m_name"                  : "muonEfficiencyCorrectorLooseGradient",
                                      "m_debug"                 : False,
                                      "m_inContainerName"       : "Muons_OR",
                                      "m_inputAlgoSystNames"    : "MuonSelector_Syst",
                                      "m_systNameReco"          : "",
                                      "m_systNameIso"           : "",
                                      "m_systNameTrig"          : "",
                                      "m_systNameTTVA"          : "",
                                      "m_useRandomRunNumber"    : True,
                                      "m_Years"                 : mutrigeffYears,
                                      "m_outputSystNamesReco"   : "MuonEfficiencyCorrector_RecoSyst",
                                      "m_outputSystNamesIso"    : "MuonEfficiencyCorrector_IsoSyst",
                                      "m_outputSystNamesTrig"   : "MuonEfficiencyCorrector_TrigSyst",
                                      "m_outputSystNamesTTVA"   : "MuonEfficiencyCorrector_TTVASyst",
                                      "m_calibRelease"          : "160624_ICHEP",
                                      "m_WorkingPointReco"      : "Loose",
                                      "m_WorkingPointIso"       : "Gradient",
                                      "m_WorkingPointRecoTrig"  : "Loose",
                                      "m_WorkingPointIsoTrig"   : "Gradient",
                                      "m_WorkingPointTTVA"      : "TTVA",
                                      "m_SingleMuTrig"          : "HLT_mu26_imedium_OR_HLT_mu50",
                                      "m_DiMuTrig"              : "",
                                    }


MuonEfficiencyCorrectorMediumGradientDict = {  "m_name"                  : "muonEfficiencyCorrectorMediumGradient",
                                      "m_debug"                 : False,
                                      "m_inContainerName"       : "Muons_OR",
                                      "m_inputAlgoSystNames"    : "MuonSelector_Syst",
                                      "m_systNameReco"          : "",
                                      "m_systNameIso"           : "",
                                      "m_systNameTrig"          : "",
                                      "m_systNameTTVA"          : "",
                                      "m_useRandomRunNumber"    : True,
                                      "m_Years"                 : mutrigeffYears,
                                      "m_outputSystNamesReco"   : "MuonEfficiencyCorrector_RecoSyst",
                                      "m_outputSystNamesIso"    : "MuonEfficiencyCorrector_IsoSyst",
                                      "m_outputSystNamesTrig"   : "MuonEfficiencyCorrector_TrigSyst",
                                      "m_outputSystNamesTTVA"   : "MuonEfficiencyCorrector_TTVASyst",
                                      "m_calibRelease"          : "160624_ICHEP",
                                      "m_WorkingPointReco"      : "Medium",
                                      "m_WorkingPointIso"       : "Gradient",
                                      "m_WorkingPointRecoTrig"  : "Medium",
                                      "m_WorkingPointIsoTrig"   : "Gradient",
                                      "m_WorkingPointTTVA"      : "TTVA",
                                      "m_SingleMuTrig"          : "HLT_mu26_imedium_OR_HLT_mu50",
                                      "m_DiMuTrig"              : "",
                                    }


MuonEfficiencyCorrectorLooseFixedCutTightTrackOnlyDict = {  "m_name"                  : "muonEfficiencyCorrectorLooseFixedCutTightTrackOnly",
                                      "m_debug"                 : False,
                                      "m_inContainerName"       : "Muons_OR",
                                      "m_inputAlgoSystNames"    : "MuonSelector_Syst",
                                      "m_systNameReco"          : "",
                                      "m_systNameIso"           : "",
                                      "m_systNameTrig"          : "",
                                      "m_systNameTTVA"          : "",
                                      "m_useRandomRunNumber"    : True,
                                      "m_Years"                 : mutrigeffYears,
                                      "m_outputSystNamesReco"   : "MuonEfficiencyCorrector_RecoSyst",
                                      "m_outputSystNamesIso"    : "MuonEfficiencyCorrector_IsoSyst",
                                      "m_outputSystNamesTrig"   : "MuonEfficiencyCorrector_TrigSyst",
                                      "m_outputSystNamesTTVA"   : "MuonEfficiencyCorrector_TTVASyst",
                                      "m_calibRelease"          : "160624_ICHEP",
                                      "m_WorkingPointReco"      : "Loose",
                                      "m_WorkingPointIso"       : "FixedCutTightTrackOnly",
                                      "m_WorkingPointRecoTrig"  : "Loose",
                                      "m_WorkingPointIsoTrig"   : "FixedCutTightTrackOnly",
                                      "m_WorkingPointTTVA"      : "TTVA",
                                      "m_SingleMuTrig"          : "HLT_mu26_imedium_OR_HLT_mu50",
                                      "m_DiMuTrig"              : "",
                                    }


MuonEfficiencyCorrectorMediumFixedCutTightTrackOnlyDict = {  "m_name"                  : "muonEfficiencyCorrectorMediumFixedCutTightTrackOnly",
                                      "m_debug"                 : False,
                                      "m_inContainerName"       : "Muons_OR",
                                      "m_inputAlgoSystNames"    : "MuonSelector_Syst",
                                      "m_systNameReco"          : "",
                                      "m_systNameIso"           : "",
                                      "m_systNameTrig"          : "",
                                      "m_systNameTTVA"          : "",
                                      "m_useRandomRunNumber"    : True,
                                      "m_Years"                 : mutrigeffYears,
                                      "m_outputSystNamesReco"   : "MuonEfficiencyCorrector_RecoSyst",
                                      "m_outputSystNamesIso"    : "MuonEfficiencyCorrector_IsoSyst",
                                      "m_outputSystNamesTrig"   : "MuonEfficiencyCorrector_TrigSyst",
                                      "m_outputSystNamesTTVA"   : "MuonEfficiencyCorrector_TTVASyst",
                                      "m_calibRelease"          : "160624_ICHEP",
                                      "m_WorkingPointReco"      : "Medium",
                                      "m_WorkingPointIso"       : "FixedCutTightTrackOnly",
                                      "m_WorkingPointRecoTrig"  : "Medium",
                                      "m_WorkingPointIsoTrig"   : "FixedCutTightTrackOnly",
                                      "m_WorkingPointTTVA"      : "TTVA",
                                      "m_SingleMuTrig"          : "HLT_mu26_imedium_OR_HLT_mu50",
                                      "m_DiMuTrig"              : "",
                                    }


MuonEfficiencyCorrectorLooseGradientLooseDict = {  "m_name"                  : "muonEfficiencyCorrectorLooseGradientLoose",
                                      "m_debug"                 : False,
                                      "m_inContainerName"       : "Muons_OR",
                                      "m_inputAlgoSystNames"    : "MuonSelector_Syst",
                                      "m_systNameReco"          : "",
                                      "m_systNameIso"           : "",
                                      "m_systNameTrig"          : "",
                                      "m_systNameTTVA"          : "",
                                      "m_useRandomRunNumber"    : True,
                                      "m_Years"                 : mutrigeffYears,
                                      "m_outputSystNamesReco"   : "MuonEfficiencyCorrector_RecoSyst",
                                      "m_outputSystNamesIso"    : "MuonEfficiencyCorrector_IsoSyst",
                                      "m_outputSystNamesTrig"   : "MuonEfficiencyCorrector_TrigSyst",
                                      "m_outputSystNamesTTVA"   : "MuonEfficiencyCorrector_TTVASyst",
                                      "m_calibRelease"          : "160624_ICHEP",
                                      "m_WorkingPointReco"      : "Loose",
                                      "m_WorkingPointIso"       : "GradientLoose",
                                      "m_WorkingPointRecoTrig"  : "Loose",
                                      "m_WorkingPointIsoTrig"   : "GradientLoose",
                                      "m_WorkingPointTTVA"      : "TTVA",
                                      "m_SingleMuTrig"          : "HLT_mu26_imedium_OR_HLT_mu50",
                                      "m_DiMuTrig"              : "",
                                    }


MuonEfficiencyCorrectorMediumGradientLooseDict = {  "m_name"                  : "muonEfficiencyCorrectorMediumGradientLoose",
                                      "m_debug"                 : False,
                                      "m_inContainerName"       : "Muons_OR",
                                      "m_inputAlgoSystNames"    : "MuonSelector_Syst",
                                      "m_systNameReco"          : "",
                                      "m_systNameIso"           : "",
                                      "m_systNameTrig"          : "",
                                      "m_systNameTTVA"          : "",
                                      "m_useRandomRunNumber"    : True,
                                      "m_Years"                 : mutrigeffYears,
                                      "m_outputSystNamesReco"   : "MuonEfficiencyCorrector_RecoSyst",
                                      "m_outputSystNamesIso"    : "MuonEfficiencyCorrector_IsoSyst",
                                      "m_outputSystNamesTrig"   : "MuonEfficiencyCorrector_TrigSyst",
                                      "m_outputSystNamesTTVA"   : "MuonEfficiencyCorrector_TTVASyst",
                                      "m_calibRelease"          : "160624_ICHEP",
                                      "m_WorkingPointReco"      : "Medium",
                                      "m_WorkingPointIso"       : "GradientLoose",
                                      "m_WorkingPointRecoTrig"  : "Medium",
                                      "m_WorkingPointIsoTrig"   : "GradientLoose",
                                      "m_WorkingPointTTVA"      : "TTVA",
                                      "m_SingleMuTrig"          : "HLT_mu26_imedium_OR_HLT_mu50",
                                      "m_DiMuTrig"              : "",
                                    }


# --------------------
# electron corrections
# --------------------

path_el_eff = "ElectronEfficiencyCorrection/2015_2016/rel20.7/ICHEP_June2016_v3/"
trigger_el_eff = "DI_E_2015_e17_lhloose_2016_e17_lhloose"

# LooseAndBLayerLLH PID 
# ---------------------

### no isolation
ElectronEfficiencyCorrectorLooseDict = { "m_name"                  : "electronEfficiencyCorrectorLoose",
                                    "m_debug"                 : False,
                                    "m_inContainerName"       : "Electrons_OR",
                                    "m_inputAlgoSystNames"    : "ElectronSelector_Syst",
                                    "m_systNameReco"          : "",
                                    "m_systNameIso"           : "",
                                    "m_systNamePID"           : "",
                                    "m_systNameTrig"          : "",
                                    "m_systNameTrigMCEff"     : "",
                                    "m_outputSystNamesReco"   : "ElectronEfficiencyCorrector_RecoSyst",
                                    "m_outputSystNamesPID"    : "ElectronEfficiencyCorrector_PIDSyst",
                                    "m_outputSystNamesIso"    : "",
                                    "m_outputSystNamesTrig"   : "ElectronEfficiencyCorrector_TrigSyst",
                                    "m_outputSystNamesTrigMCEff"   : "ElectronEfficiencyCorrector_TrigMCEffSyst",
                                    "m_corrFileNameReco"      : path_el_eff + "offline/efficiencySF.offline.RecoTrk.root",
                                    "m_corrFileNamePID"       : path_el_eff + "offline/efficiencySF.offline.LooseAndBLayerLLH_d0z0_v11.root",
                                    "m_corrFileNameIso"       : "",
                                    "m_corrFileNameTrig"      : path_el_eff + "trigger/efficiencySF." + trigger_el_eff + ".LooseAndBLayerLLH_d0z0_v11.root",
                                    "m_corrFileNameTrigMCEff" : path_el_eff + "trigger/efficiency." + trigger_el_eff + ".LooseAndBLayerLLH_d0z0_v11.root",
                                   }

# FixedCutLoose isolation
ElectronEfficiencyCorrectorLooseFCLDict = { "m_name"                  : "electronEfficiencyCorrectorLooseFCL",
                                    "m_debug"                 : False,
                                    "m_inContainerName"       : "Electrons_OR",
                                    "m_inputAlgoSystNames"    : "ElectronSelector_Syst",
                                    "m_systNameReco"          : "",
                                    "m_systNameIso"           : "",
                                    "m_systNamePID"           : "",
                                    "m_systNameTrig"          : "",
                                    "m_systNameTrigMCEff"     : "",
                                    "m_outputSystNamesReco"   : "ElectronEfficiencyCorrector_RecoSyst",
                                    "m_outputSystNamesPID"    : "ElectronEfficiencyCorrector_PIDSyst",
                                    "m_outputSystNamesIso"    : "ElectronEfficiencyCorrector_IsoSyst",
                                    "m_outputSystNamesTrig"   : "ElectronEfficiencyCorrector_TrigSyst",
                                    "m_outputSystNamesTrigMCEff"   : "ElectronEfficiencyCorrector_TrigMCEffSyst",
                                    "m_corrFileNameReco"      : path_el_eff + "offline/efficiencySF.offline.RecoTrk.root",
                                    "m_corrFileNamePID"       : path_el_eff + "offline/efficiencySF.offline.LooseAndBLayerLLH_d0z0_v11.root",
                                    "m_corrFileNameIso"       : path_el_eff + "isolation/efficiencySF.Isolation.LooseAndBLayerLLH_d0z0_v11_isolFixedCutLoose.root", # comment if d0z0 cuts are NOT tight (TTVA)
                                    "m_corrFileNameTrig"      : path_el_eff + "trigger/efficiencySF." + trigger_el_eff + ".LooseAndBLayerLLH_d0z0_v11_isolFixedCutLoose.root",
                                    "m_corrFileNameTrigMCEff" : path_el_eff + "trigger/efficiency." + trigger_el_eff + ".LooseAndBLayerLLH_d0z0_v11_isolFixedCutLoose.root",
                                   }

# LooseTrackOnly isolation
ElectronEfficiencyCorrectorLooseLTODict = { "m_name"                    : "electronEfficiencyCorrectorLooseLTO",
                                    "m_debug"                 : False,
                                    "m_inContainerName"       : "Electrons_OR",
                                    "m_inputAlgoSystNames"    : "ElectronSelector_Syst",
                                    "m_systNameReco"          : "",
                                    "m_systNameIso"           : "",
                                    "m_systNamePID"           : "",
                                    "m_systNameTrig"          : "",
                                    "m_systNameTrigMCEff"     : "",
                                    "m_outputSystNamesReco"   : "ElectronEfficiencyCorrector_RecoSyst",
                                    "m_outputSystNamesPID"    : "ElectronEfficiencyCorrector_PIDSyst",
                                    "m_outputSystNamesIso"    : "ElectronEfficiencyCorrector_IsoSyst",
                                    "m_outputSystNamesTrig"   : "ElectronEfficiencyCorrector_TrigSyst",
                                    "m_outputSystNamesTrigMCEff"   : "ElectronEfficiencyCorrector_TrigMCEffSyst",
                                    "m_corrFileNameReco"      : path_el_eff + "offline/efficiencySF.offline.RecoTrk.root",
                                    "m_corrFileNamePID"       : path_el_eff + "offline/efficiencySF.offline.LooseAndBLayerLLH_d0z0_v11.root",
                                    "m_corrFileNameIso"       : path_el_eff + "isolation/efficiencySF.Isolation.LooseAndBLayerLLH_d0z0_v11_isolLooseTrackOnly.root", # comment if d0z0 cuts are NOT tight (TTVA)
                                    "m_corrFileNameTrig"      : path_el_eff + "trigger/efficiencySF." + trigger_el_eff + ".LooseAndBLayerLLH_d0z0_v11_isolLooseTrackOnly.root",
                                    "m_corrFileNameTrigMCEff" : path_el_eff + "trigger/efficiency." + trigger_el_eff + ".LooseAndBLayerLLH_d0z0_v11_isolLooseTrackOnly.root",
                                  }

# MediumLLH PID 
# -------------

### no isolation
ElectronEfficiencyCorrectorMediumDict = { "m_name"                  : "electronEfficiencyCorrectorMedium",
                                    "m_debug"                 : False,
                                    "m_inContainerName"       : "Electrons_OR",
                                    "m_inputAlgoSystNames"    : "ElectronSelector_Syst",
                                    "m_systNameReco"          : "",
                                    "m_systNameIso"           : "",
                                    "m_systNamePID"           : "",
                                    "m_systNameTrig"          : "",
                                    "m_systNameTrigMCEff"     : "",
                                    "m_outputSystNamesReco"   : "ElectronEfficiencyCorrector_RecoSyst",
                                    "m_outputSystNamesPID"    : "ElectronEfficiencyCorrector_PIDSyst",
                                    "m_outputSystNamesIso"    : "",
                                    "m_outputSystNamesTrig"   : "ElectronEfficiencyCorrector_TrigSyst",
                                    "m_outputSystNamesTrigMCEff"   : "ElectronEfficiencyCorrector_TrigMCEffSyst",
                                    "m_corrFileNameReco"      : path_el_eff + "offline/efficiencySF.offline.RecoTrk.root",
                                    "m_corrFileNamePID"       : path_el_eff + "offline/efficiencySF.offline.MediumLLH_d0z0_v11.root",
                                    "m_corrFileNameIso"       : "",
                                    "m_corrFileNameTrig"      : path_el_eff + "trigger/efficiencySF." + trigger_el_eff + ".MediumLLH_d0z0_v11.root",
                                    "m_corrFileNameTrigMCEff" : path_el_eff + "trigger/efficiency." + trigger_el_eff + ".MediumLLH_d0z0_v11.root",
                                   }

# gradient isolation
ElectronEfficiencyCorrectorMediumGradientDict = { "m_name"                  : "electronEfficiencyCorrectorMediumGradient",
                                    "m_debug"                 : False,
                                    "m_inContainerName"       : "Electrons_OR",
                                    "m_inputAlgoSystNames"    : "ElectronSelector_Syst",
                                    "m_systNameReco"          : "",
                                    "m_systNameIso"           : "",
                                    "m_systNamePID"           : "",
                                    "m_systNameTrig"          : "",
                                    "m_systNameTrigMCEff"     : "",
                                    "m_outputSystNamesReco"   : "ElectronEfficiencyCorrector_RecoSyst",
                                    "m_outputSystNamesPID"    : "ElectronEfficiencyCorrector_PIDSyst",
                                    "m_outputSystNamesIso"    : "ElectronEfficiencyCorrector_IsoSyst",
                                    "m_outputSystNamesTrig"   : "ElectronEfficiencyCorrector_TrigSyst",
                                    "m_outputSystNamesTrigMCEff"   : "ElectronEfficiencyCorrector_TrigMCEffSyst",
                                    "m_corrFileNameReco"      : path_el_eff + "offline/efficiencySF.offline.RecoTrk.root",
                                    "m_corrFileNamePID"       : path_el_eff + "offline/efficiencySF.offline.MediumLLH_d0z0_v11.root",
                                    "m_corrFileNameIso"       : path_el_eff + "isolation/efficiencySF.Isolation.MediumLLH_d0z0_v11_isolGradient.root", # comment if d0z0 cuts are NOT tight (TTVA)
                                    "m_corrFileNameTrig"      : path_el_eff + "trigger/efficiencySF." + trigger_el_eff + ".MediumLLH_d0z0_v11_isolGradient.root",
                                    "m_corrFileNameTrigMCEff" : path_el_eff + "trigger/efficiency." + trigger_el_eff + ".MediumLLH_d0z0_v11_isolGradient.root",
                                   }

# loose isolation
ElectronEfficiencyCorrectorMediumLooseDict = { "m_name"                  : "electronEfficiencyCorrectorMediumLoose",
                                    "m_debug"                 : False,
                                    "m_inContainerName"       : "Electrons_OR",
                                    "m_inputAlgoSystNames"    : "ElectronSelector_Syst",
                                    "m_systNameReco"          : "",
                                    "m_systNameIso"           : "",
                                    "m_systNamePID"           : "",
                                    "m_systNameTrig"          : "",
                                    "m_systNameTrigMCEff"     : "",
                                    "m_outputSystNamesReco"   : "ElectronEfficiencyCorrector_RecoSyst",
                                    "m_outputSystNamesPID"    : "ElectronEfficiencyCorrector_PIDSyst",
                                    "m_outputSystNamesIso"    : "ElectronEfficiencyCorrector_IsoSyst",
                                    "m_outputSystNamesTrig"   : "ElectronEfficiencyCorrector_TrigSyst",
                                    "m_outputSystNamesTrigMCEff"   : "ElectronEfficiencyCorrector_TrigMCEffSyst",
                                    "m_corrFileNameReco"      : path_el_eff + "offline/efficiencySF.offline.RecoTrk.root",
                                    "m_corrFileNamePID"       : path_el_eff + "offline/efficiencySF.offline.MediumLLH_d0z0_v11.root",
                                    "m_corrFileNameIso"       : path_el_eff + "isolation/efficiencySF.Isolation.MediumLLH_d0z0_v11_isolLoose.root", # comment if d0z0 cuts are NOT tight (TTVA)
                                    "m_corrFileNameTrig"      : path_el_eff + "trigger/efficiencySF." + trigger_el_eff + ".MediumLLH_d0z0_v11_isolLoose.root",
                                    "m_corrFileNameTrigMCEff" : path_el_eff + "trigger/efficiency." + trigger_el_eff + ".MediumLLH_d0z0_v11_isolLoose.root",
                                   }

# LooseTrackOnly isolation
ElectronEfficiencyCorrectorMediumLTODict = { "m_name"                    : "electronEfficiencyCorrectorMediumLTO",
                                    "m_debug"                 : False,
                                    "m_inContainerName"       : "Electrons_OR",
                                    "m_inputAlgoSystNames"    : "ElectronSelector_Syst",
                                    "m_systNameReco"          : "",
                                    "m_systNameIso"           : "",
                                    "m_systNamePID"           : "",
                                    "m_systNameTrig"          : "",
                                    "m_systNameTrigMCEff"     : "",
                                    "m_outputSystNamesReco"   : "ElectronEfficiencyCorrector_RecoSyst",
                                    "m_outputSystNamesPID"    : "ElectronEfficiencyCorrector_PIDSyst",
                                    "m_outputSystNamesIso"    : "ElectronEfficiencyCorrector_IsoSyst",
                                    "m_outputSystNamesTrig"   : "ElectronEfficiencyCorrector_TrigSyst",
                                    "m_outputSystNamesTrigMCEff"   : "ElectronEfficiencyCorrector_TrigMCEffSyst",
                                    "m_corrFileNameReco"      : path_el_eff + "offline/efficiencySF.offline.RecoTrk.root",
                                    "m_corrFileNamePID"       : path_el_eff + "offline/efficiencySF.offline.MediumLLH_d0z0_v11.root",
                                    "m_corrFileNameIso"       : path_el_eff + "isolation/efficiencySF.Isolation.MediumLLH_d0z0_v11_isolLooseTrackOnly.root", # comment if d0z0 cuts are NOT tight (TTVA)
                                    "m_corrFileNameTrig"      : path_el_eff + "trigger/efficiencySF." + trigger_el_eff + ".MediumLLH_d0z0_v11_isolLooseTrackOnly.root",
                                    "m_corrFileNameTrigMCEff" : path_el_eff + "trigger/efficiency." + trigger_el_eff + ".MediumLLH_d0z0_v11_isolLooseTrackOnly.root",
                                  }

# TightLLD PID 
# ------------

### no isolation
ElectronEfficiencyCorrectorTightDict = { "m_name"                  : "electronEfficiencyCorrectorTight",
                                    "m_debug"                 : False,
                                    "m_inContainerName"       : "Electrons_OR",
                                    "m_inputAlgoSystNames"    : "ElectronSelector_Syst",
                                    "m_systNameReco"          : "",
                                    "m_systNameIso"           : "",
                                    "m_systNamePID"           : "",
                                    "m_systNameTrig"          : "",
                                    "m_systNameTrigMCEff"     : "",
                                    "m_outputSystNamesReco"   : "ElectronEfficiencyCorrector_RecoSyst",
                                    "m_outputSystNamesPID"    : "ElectronEfficiencyCorrector_PIDSyst",
                                    "m_outputSystNamesIso"    : "",
                                    "m_outputSystNamesTrig"   : "ElectronEfficiencyCorrector_TrigSyst",
                                    "m_outputSystNamesTrigMCEff"   : "ElectronEfficiencyCorrector_TrigMCEffSyst",
                                    "m_corrFileNameReco"      : path_el_eff + "offline/efficiencySF.offline.RecoTrk.root",
                                    "m_corrFileNamePID"       : path_el_eff + "offline/efficiencySF.offline.TightLLH_d0z0_v11.root",
                                    "m_corrFileNameIso"       : "",
                                    "m_corrFileNameTrig"      : path_el_eff + "trigger/efficiencySF." + trigger_el_eff + ".TightLLH_d0z0_v11.root",
                                    "m_corrFileNameTrigMCEff" : path_el_eff + "trigger/efficiency." + trigger_el_eff + ".TightLLH_d0z0_v11.root",
                                   }

# gradient isolation
ElectronEfficiencyCorrectorTightGradientDict = { "m_name"                  : "electronEfficiencyCorrectorTightGradient",
                                    "m_debug"                 : False,
                                    "m_inContainerName"       : "Electrons_OR",
                                    "m_inputAlgoSystNames"    : "ElectronSelector_Syst",
                                    "m_systNameReco"          : "",
                                    "m_systNameIso"           : "",
                                    "m_systNamePID"           : "",
                                    "m_systNameTrig"          : "",
                                    "m_systNameTrigMCEff"     : "",
                                    "m_outputSystNamesReco"   : "ElectronEfficiencyCorrector_RecoSyst",
                                    "m_outputSystNamesPID"    : "ElectronEfficiencyCorrector_PIDSyst",
                                    "m_outputSystNamesIso"    : "ElectronEfficiencyCorrector_IsoSyst",
                                    "m_outputSystNamesTrig"   : "ElectronEfficiencyCorrector_TrigSyst",
                                    "m_outputSystNamesTrigMCEff"   : "ElectronEfficiencyCorrector_TrigMCEffSyst",
                                    "m_corrFileNameReco"      : path_el_eff + "offline/efficiencySF.offline.RecoTrk.root",
                                    "m_corrFileNamePID"       : path_el_eff + "offline/efficiencySF.offline.TightLLH_d0z0_v11.root",
                                    "m_corrFileNameIso"       : path_el_eff + "isolation/efficiencySF.Isolation.TightLLH_d0z0_v11_isolGradient.root", # comment if d0z0 cuts are NOT tight (TTVA)
                                    "m_corrFileNameTrig"      : path_el_eff + "trigger/efficiencySF." + trigger_el_eff + ".TightLLH_d0z0_v11_isolGradient.root",
                                    "m_corrFileNameTrigMCEff" : path_el_eff + "trigger/efficiency." + trigger_el_eff + ".TightLLH_d0z0_v11_isolGradient.root",
                                   }

# loose isolation
ElectronEfficiencyCorrectorTightLooseDict = { "m_name"                  : "electronEfficiencyCorrectorTightLoose",
                                    "m_debug"                 : False,
                                    "m_inContainerName"       : "Electrons_OR",
                                    "m_inputAlgoSystNames"    : "ElectronSelector_Syst",
                                    "m_systNameReco"          : "",
                                    "m_systNameIso"           : "",
                                    "m_systNamePID"           : "",
                                    "m_systNameTrig"          : "",
                                    "m_systNameTrigMCEff"     : "",
                                    "m_outputSystNamesReco"   : "ElectronEfficiencyCorrector_RecoSyst",
                                    "m_outputSystNamesPID"    : "ElectronEfficiencyCorrector_PIDSyst",
                                    "m_outputSystNamesIso"    : "ElectronEfficiencyCorrector_IsoSyst",
                                    "m_outputSystNamesTrig"   : "ElectronEfficiencyCorrector_TrigSyst",
                                    "m_outputSystNamesTrigMCEff"   : "ElectronEfficiencyCorrector_TrigMCEffSyst",
                                    "m_corrFileNameReco"      : path_el_eff + "offline/efficiencySF.offline.RecoTrk.root",
                                    "m_corrFileNamePID"       : path_el_eff + "offline/efficiencySF.offline.TightLLH_d0z0_v11.root",
                                    "m_corrFileNameIso"       : path_el_eff + "isolation/efficiencySF.Isolation.TightLLH_d0z0_v11_isolLoose.root", # comment if d0z0 cuts are NOT tight (TTVA)
                                    "m_corrFileNameTrig"      : path_el_eff + "trigger/efficiencySF." + trigger_el_eff + ".TightLLH_d0z0_v11_isolLoose.root",
                                    "m_corrFileNameTrigMCEff" : path_el_eff + "trigger/efficiency." + trigger_el_eff + ".TightLLH_d0z0_v11_isolLoose.root",
                                   }

# LooseTrackOnly isolation
ElectronEfficiencyCorrectorTightLTODict = { "m_name"                    : "electronEfficiencyCorrectorTightLTO",
                                    "m_debug"                 : False,
                                    "m_inContainerName"       : "Electrons_OR",
                                    "m_inputAlgoSystNames"    : "ElectronSelector_Syst",
                                    "m_systNameReco"          : "",
                                    "m_systNameIso"           : "",
                                    "m_systNamePID"           : "",
                                    "m_systNameTrig"          : "",
                                    "m_systNameTrigMCEff"     : "",
                                    "m_outputSystNamesReco"   : "ElectronEfficiencyCorrector_RecoSyst",
                                    "m_outputSystNamesPID"    : "ElectronEfficiencyCorrector_PIDSyst",
                                    "m_outputSystNamesIso"    : "ElectronEfficiencyCorrector_IsoSyst",
                                    "m_outputSystNamesTrig"   : "ElectronEfficiencyCorrector_TrigSyst",
                                    "m_outputSystNamesTrigMCEff"   : "ElectronEfficiencyCorrector_TrigMCEffSyst",
                                    "m_corrFileNameReco"      : path_el_eff + "offline/efficiencySF.offline.RecoTrk.root",
                                    "m_corrFileNamePID"       : path_el_eff + "offline/efficiencySF.offline.TightLLH_d0z0_v11.root",
                                    "m_corrFileNameIso"       : path_el_eff + "isolation/efficiencySF.Isolation.TightLLH_d0z0_v11_isolLooseTrackOnly.root", # comment if d0z0 cuts are NOT tight (TTVA)
                                    "m_corrFileNameTrig"      : path_el_eff + "trigger/efficiencySF." + trigger_el_eff + ".TightLLH_d0z0_v11_isolLooseTrackOnly.root",
                                    "m_corrFileNameTrigMCEff" : path_el_eff + "trigger/efficiency." + trigger_el_eff + ".TightLLH_d0z0_v11_isolLooseTrackOnly.root",
                                  }

# tight isolation
ElectronEfficiencyCorrectorTightTightDict = { "m_name"                    : "electronEfficiencyCorrectorTightTight",
                                    "m_debug"                 : False,
                                    "m_inContainerName"       : "Electrons_OR",
                                    "m_inputAlgoSystNames"    : "ElectronSelector_Syst",
                                    "m_systNameReco"          : "",
                                    "m_systNameIso"           : "",
                                    "m_systNamePID"           : "",
                                    "m_systNameTrig"          : "",
                                    "m_systNameTrigMCEff"     : "",
                                    "m_outputSystNamesReco"   : "ElectronEfficiencyCorrector_RecoSyst",
                                    "m_outputSystNamesPID"    : "ElectronEfficiencyCorrector_PIDSyst",
                                    "m_outputSystNamesIso"    : "ElectronEfficiencyCorrector_IsoSyst",
                                    "m_outputSystNamesTrig"   : "ElectronEfficiencyCorrector_TrigSyst",
                                    "m_outputSystNamesTrigMCEff"   : "ElectronEfficiencyCorrector_TrigMCEffSyst",
                                    "m_corrFileNameReco"      : path_el_eff + "offline/efficiencySF.offline.RecoTrk.root",
                                    "m_corrFileNamePID"       : path_el_eff + "offline/efficiencySF.offline.TightLLH_d0z0_v11.root",
                                    "m_corrFileNameIso"       : path_el_eff + "isolation/efficiencySF.Isolation.TightLLH_d0z0_v11_isolTight.root", # comment if d0z0 cuts are NOT tight (TTVA)
                                    "m_corrFileNameTrig"      : path_el_eff + "trigger/efficiencySF." + trigger_el_eff + ".TightLLH_d0z0_v11_isolTight.root",
                                    "m_corrFileNameTrigMCEff" : path_el_eff + "trigger/efficiency." + trigger_el_eff + ".TightLLH_d0z0_v11_isolTight.root",
                                  }

# Truth matching info just for muons
TruthMatchAlgoDict       = { "m_name"                           : "truthMatching",
                             "m_debug"                          : False,
                             "m_inContainerName_Electrons"      : "Electrons_OR",
                             "m_inContainerName_Muons"          : "Muons_OR",
                             "m_doMuonTruthContMatching"        : False,
                           }


SSDiLepTreeAlgoDict      = { "m_name"                  : "physics",
                             "m_debug"                 : False,
                             "m_muContainerName"       : "Muons_OR",
                             "m_elContainerName"       : "Electrons_OR",
                             "m_jetContainerName"      : "AntiKt4EMTopoJets_OR",
                             "m_METContainerName"      : "RefFinal_SSDiLep",
                             "m_outHistDir"            : False,
                             ######"m_evtDetailStr"          : "pileup truth",
                             "m_evtDetailStr"          : "pileup",
                             "m_trigDetailStr"         : "basic passTriggers menuKeys",
                             "m_muDetailStr"           : "kinematic trigger isolation quality trackparams effSF",
                             "m_elDetailStr"           : "kinematic trigger isolation PID trackparams effSF",
                             #"m_tauDetailStr"          : "kinematic",
                             "m_jetDetailStr"          : "kinematic energy flavorTag sfFTagFix77 truth",
                             "m_METDetailStr"          : "RefEle RefGamma Muons RefJet RefJetTrk SoftClus PVSoftTrk",
                           }

