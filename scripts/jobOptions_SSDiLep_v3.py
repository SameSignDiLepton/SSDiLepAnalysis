import ROOT

from xAH_config import xAH_config
import sys, os

sys.path.insert(0, os.environ['ROOTCOREBIN']+"/user_scripts/SSDiLepAnalysis/")

from config_v3 import *
from helperFunctions import generateElectronEfficiencyCorrector

c = xAH_config()

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
    c.setalg("ElectronEfficiencyCorrector", generateElectronEfficiencyCorrector(path_el_eff,ID,isol,trig) )
c.setalg("ElectronEfficiencyCorrector", generateElectronEfficiencyCorrector(path_el_eff,"TightLLH","","") )
c.setalg("ElectronEfficiencyCorrector", generateElectronEfficiencyCorrector(path_el_eff,"LooseAndBLayerLLH","_isolLoose","") )
SSDiLepTreeAlgoDict["m_elDetailStr"] = trigger_el_double_unrecommended + " " + trigger_el_double_recommended + " LooseAndBLayerLLH MediumLLH TightLLH isolNoRequirement isolLoose kinematic trigger isolation PID trackparams effSF"

c.setalg("TruthMatchAlgo", TruthMatchAlgoDict)
#c.setalg("XSAlgo", XSAlgoDict)
c.setalg("SSDiLepTreeAlgo", SSDiLepTreeAlgoDict)
