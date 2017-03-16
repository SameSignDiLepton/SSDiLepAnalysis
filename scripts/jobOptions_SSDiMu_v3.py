import ROOT

from xAH_config import xAH_config
import sys, os

sys.path.insert(0, os.environ['ROOTCOREBIN']+"/user_scripts/SSDiLepAnalysis/")

from config_SSDiMu_v3 import *
from helperFunctions import generateElectronEfficiencyCorrector

c = xAH_config()

# Here order matters!
#
# NB: here users can update values in the dictionaries before setting them to the algorithm
#
c.setalg("BasicEventSelection", BasicEventSelectionDict)
c.setalg("JetCalibrator",       JetCalibratorDict)
c.setalg("MuonCalibrator",      MuonCalibratorDict)
c.setalg("JetSelector",         JetSelectorDict)
c.setalg("MuonSelector",        MuonSelectorDict)
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


c.setalg("TruthMatchAlgo", TruthMatchAlgoDict)
c.setalg("XSAlgo", XSAlgoDict)
c.setalg("SSDiLepTreeAlgo", SSDiLepTreeAlgoDict)
