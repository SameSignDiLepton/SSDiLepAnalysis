import ROOT

from xAH_config import xAH_config
import sys, os

sys.path.insert(0, os.environ['ROOTCOREBIN']+"/user_scripts/SSDiLepAnalysis/")

from config_SSDiMu_v2 import *

c = xAH_config()

# Here order matters!
#
# NB: here users can update values in the dictionaries before setting them to the algorithm
#
c.setalg("BasicEventSelection", BasicEventSelectionDict)
c.setalg("JetCalibrator", JetCalibratorDict)
c.setalg("MuonCalibrator", MuonCalibratorDict)
c.setalg("JetSelector", JetSelectorDict)
c.setalg("MuonSelector", MuonSelectorDict)
c.setalg("METConstructor", METConstructorDict)
c.setalg("OverlapRemover", OverlapRemoverDict)

c.setalg("MuonEfficiencyCorrector", MuonEfficiencyCorrectorMediumGradientDict)
c.setalg("MuonEfficiencyCorrector", MuonEfficiencyCorrectorMediumFixedCutTightTrackOnlyDict)

c.setalg("TruthMatchAlgo", TruthMatchAlgoDict)
c.setalg("XSAlgo", XSAlgoDict)
c.setalg("SSDiLepTreeAlgo", SSDiLepTreeAlgoDict)

