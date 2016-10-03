import ROOT

from xAH_config import xAH_config
import sys, os

sys.path.insert(0, os.environ['ROOTCOREBIN']+"/user_scripts/SSDiLepAnalysis/")

from config_EE import *

c = xAH_config()

# Here order matters!
#
# NB: here users can update values in the dictionaries before setting them to the algorithm
#
c.setalg("BasicEventSelection", BasicEventSelectionDict)
c.setalg("JetCalibrator", JetCalibratorDict)
c.setalg("MuonCalibrator", MuonCalibratorDict)
c.setalg("ElectronCalibrator", ElectronCalibratorDict)
c.setalg("JetSelector", JetSelectorDict)
c.setalg("MuonSelector", MuonSelectorDict)
c.setalg("ElectronSelector", ElectronSelectorDict)
##->c.setalg("TauSelector", TauSelectorDict)
c.setalg("METConstructor", METConstructorDict)
c.setalg("OverlapRemover", OverlapRemoverDict)
c.setalg("MuonEfficiencyCorrector", MuonEfficiencyCorrectorLooseDict)      
c.setalg("ElectronEfficiencyCorrector", ElectronEfficiencyCorrectorLooseDict)
c.setalg("ElectronEfficiencyCorrector", ElectronEfficiencyCorrectorLooseFCLDict)
c.setalg("ElectronEfficiencyCorrector", ElectronEfficiencyCorrectorLooseLTODict)
c.setalg("MuonEfficiencyCorrector", MuonEfficiencyCorrectorMediumDict)
c.setalg("ElectronEfficiencyCorrector", ElectronEfficiencyCorrectorMediumDict)
c.setalg("ElectronEfficiencyCorrector", ElectronEfficiencyCorrectorMediumGradientDict)
c.setalg("ElectronEfficiencyCorrector", ElectronEfficiencyCorrectorMediumLooseDict)
c.setalg("ElectronEfficiencyCorrector", ElectronEfficiencyCorrectorMediumLTODict)
c.setalg("MuonEfficiencyCorrector", MuonEfficiencyCorrectorTightDict)
c.setalg("ElectronEfficiencyCorrector", ElectronEfficiencyCorrectorTightDict)
c.setalg("ElectronEfficiencyCorrector", ElectronEfficiencyCorrectorTightGradientDict)
c.setalg("ElectronEfficiencyCorrector", ElectronEfficiencyCorrectorTightLooseDict)
c.setalg("ElectronEfficiencyCorrector", ElectronEfficiencyCorrectorTightLTODict)
c.setalg("ElectronEfficiencyCorrector", ElectronEfficiencyCorrectorTightTightDict)
c.setalg("TruthMatchAlgo", TruthMatchAlgoDict)
c.setalg("SSDiLepTreeAlgo", SSDiLepTreeAlgoDict)