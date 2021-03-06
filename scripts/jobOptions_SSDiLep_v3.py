import ROOT

from xAH_config import xAH_config
import sys, os

sys.path.insert(0, os.environ['ROOTCOREBIN']+"/user_scripts/SSDiLepAnalysis/")

from config_v3 import *
from helperFunctions import generateElectronEfficiencyCorrector

c = xAH_config()

# AFII on/off (needed for electron calib/eff algorithms, as the info is not
# read correctly from the derivations)
AFII = True
ElectronCalibratorDict["m_setAFII"] = AFII

# Turn systematics ON/OFF
SYS = True
METConstructorDict["m_runNominal"] = not SYS
calibratorList = [MuonCalibratorDict, ElectronCalibratorDict]
for calibrator in calibratorList:
  calibrator["m_systName"] = "All" if SYS else ""
  calibrator["m_systVal"]  =  1.0  if SYS else 0.0
muonEffCorrList = [MuonEfficiencyCorrectorMediumGradientDict, MuonEfficiencyCorrectorMediumFixedCutTightTrackOnlyDict]
for effCorr in muonEffCorrList:
  effCorr["m_systNameReco"] = "All" if SYS else ""
  effCorr["m_systNameIso" ] = "All" if SYS else ""
  effCorr["m_systNameTrig"] = "All" if SYS else ""
  effCorr["m_systNameTTVA"] = "All" if SYS else ""
  effCorr["m_systValReco" ] =  1.0  if SYS else 0.0
  effCorr["m_systValIso"  ] =  1.0  if SYS else 0.0
  effCorr["m_systValTrig" ] =  1.0  if SYS else 0.0
  effCorr["m_systValTTVA" ] =  1.0  if SYS else 0.0

# Set the derivation name. This is needed
# to read correctly the MetaData info.
derivation = "EXOT12Kernel"
BasicEventSelectionDict["m_derivationName"] = derivation

# Here order matters!
#
# NB: here users can update values in the dictionaries before setting them to the algorithm
#
c.setalg("BasicEventSelection", BasicEventSelectionDict)
c.setalg("JetCalibrator",       JetCalibratorDict)
c.setalg("MuonCalibrator",      MuonCalibratorDict)
c.setalg("ElectronCalibrator",  ElectronCalibratorDict)
c.setalg("JetSelector",         JetSelectorDict)
c.setalg("MuonSelector",        MuonSelectorDict)
c.setalg("ElectronSelector",    ElectronSelectorDict)
c.setalg("METConstructor",      METConstructorDict)

# --------------------
# jet corrections
# --------------------
c.setalg("BJetEfficiencyCorrector", BJetEfficiencyCorrectorDict)

c.setalg("OverlapRemover",      OverlapRemoverDict)


# ----------------
# muon corrections
# ----------------
c.setalg("MuonEfficiencyCorrector", MuonEfficiencyCorrectorMediumGradientDict)
c.setalg("MuonEfficiencyCorrector", MuonEfficiencyCorrectorMediumFixedCutTightTrackOnlyDict)


# --------------------
# electron corrections
# --------------------

# save scale-factors only for two combinations of ID/isol WPs:
#  -) LooseAndBLayerLLH + no iso
#  -) MediumLLH         + isolLoose

#https://twiki.cern.ch/twiki/bin/view/AtlasProtected/LatestRecommendationsElectronIDRun2
path_el_eff = "ElectronEfficiencyCorrection/2015_2016/rel20.7/Moriond_February2017_v1/"

el_IDWPs   = ["LooseAndBLayerLLH","MediumLLH" ]
el_isolWPs = [""                 ,"_isolLoose"]

trigger_el_single               = "SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0"
trigger_el_double_unrecommended = "DI_E_2015_e17_lhloose_2016_e17_lhloose"
trigger_el_double_recommended   = "DI_E_2015_e12_lhloose_L1EM10VH_2016_e17_lhvloose_nod0"

#el_trigWPs = [trigger_el_single,trigger_el_double_unrecommended,trigger_el_double_recommended]
el_trigWPs = [trigger_el_double_recommended,trigger_el_double_unrecommended]

for ID,isol in zip(el_IDWPs,el_isolWPs):
  for trig in el_trigWPs:
    c.setalg("ElectronEfficiencyCorrector", generateElectronEfficiencyCorrector(path_el_eff,ID,isol,trig,AFII,SYS) )
c.setalg("ElectronEfficiencyCorrector", generateElectronEfficiencyCorrector(path_el_eff,"TightLLH","","",AFII,SYS) )
c.setalg("ElectronEfficiencyCorrector", generateElectronEfficiencyCorrector(path_el_eff,"LooseAndBLayerLLH","_isolLoose","",AFII,SYS) )
SSDiLepTreeAlgoDict["m_elDetailStr"] = trigger_el_double_unrecommended + " " + trigger_el_double_recommended + " LooseAndBLayerLLH MediumLLH TightLLH isolNoRequirement isolLoose kinematic trigger isolation PID trackparams effSF"

c.setalg("TruthMatchAlgo", TruthMatchAlgoDict)
c.setalg("XSAlgo", XSAlgoDict)
c.setalg("SSDiLepTreeAlgo", SSDiLepTreeAlgoDict)
