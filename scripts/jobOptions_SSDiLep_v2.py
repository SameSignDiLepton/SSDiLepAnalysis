import ROOT

from xAH_config import xAH_config
import sys, os

sys.path.insert(0, os.environ['ROOTCOREBIN']+"/user_scripts/SSDiLepAnalysis/")

from config_v2_182ifb import *

def generateElectronEfficiencyCorrector (path, PID, isol, trigger) :
  ElectronEfficiencyCorrector = { "m_name" : "EleEffCorr"+PID+isol+trigger,
  "m_debug"                 : False,
  "m_inContainerName"       : "Electrons_OR",
  "m_inputAlgoSystNames"    : "ElectronSelector_Syst",
  "m_systNameReco"          : "",
  "m_systNameIso"           : "",
  "m_systNamePID"           : "",
  "m_systNameTrig"          : "",
  "m_systNameTrigMCEff"     : "",
  "m_outputSystNamesReco"   : "EleEffCorr_RecoSyst",
  "m_outputSystNamesPID"    : "EleEffCorr_PIDSyst" ,
  "m_outputSystNamesIso"    : "EleEffCorr_IsoSyst" ,
  "m_outputSystNamesTrig"   : "EleEffCorr_TrigSyst",
  "m_outputSystNamesTrigMCEff"   : "EleEffCorr_TrigMCEffSyst",
  "m_corrFileNameReco"      : path + "offline/efficiencySF.offline.RecoTrk.root",
  "m_corrFileNamePID"       : path + "offline/efficiencySF.offline."         + PID + "_d0z0_v11.root" if len(PID)>0 else "",
  "m_corrFileNameIso"       : path + "isolation/efficiencySF.Isolation."     + PID + "_d0z0_v11" + isol + ".root" if len(isol)>0 else "",
  "m_corrFileNameTrig"      : path + "trigger/efficiencySF." + trigger + "." + PID + "_d0z0_v11" + isol + ".root" if len(trigger)>0 else "",
  "m_corrFileNameTrigMCEff" : path + "trigger/efficiency."   + trigger + "." + PID + "_d0z0_v11" + isol + ".root" if len(trigger)>0 else "",
  }
  return ElectronEfficiencyCorrector

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
c.setalg("OverlapRemover",      OverlapRemoverDict)

# ----------------
# muon corrections
# ----------------
c.setalg("MuonEfficiencyCorrector", MuonEfficiencyCorrectorLooseLooseDict)      
c.setalg("MuonEfficiencyCorrector", MuonEfficiencyCorrectorLooseGradientLooseDict)      
c.setalg("MuonEfficiencyCorrector", MuonEfficiencyCorrectorLooseGradientDict)      
c.setalg("MuonEfficiencyCorrector", MuonEfficiencyCorrectorLooseFixedCutTightTrackOnlyDict)      
c.setalg("MuonEfficiencyCorrector", MuonEfficiencyCorrectorMediumGradientDict)      
c.setalg("MuonEfficiencyCorrector", MuonEfficiencyCorrectorMediumFixedCutTightTrackOnlyDict)      
c.setalg("MuonEfficiencyCorrector", MuonEfficiencyCorrectorMediumGradientLooseDict)

# --------------------
# electron corrections
# --------------------

# save scale-factors only for two combinations of ID/isol WPs:
#  -) LooseAndBLayerLLH + no iso
#  -) MediumLLH         + isolLoose

path_el_eff = "ElectronEfficiencyCorrection/2015_2016/rel20.7/ICHEP_June2016_v3/"

el_IDWPs   = ["LooseAndBLayerLLH","MediumLLH" ]
el_isolWPs = [""                 ,"_isolLoose"]

trigger_el_single               = "SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0"
trigger_el_double_unrecommended = "DI_E_2015_e17_lhloose_2016_e17_lhloose"
trigger_el_double_recommended   = "DI_E_2015_e12_lhloose_L1EM10VH_2016_e17_lhvloose_nod0"

el_trigWPs = [trigger_el_single,trigger_el_double_unrecommended,trigger_el_double_recommended]

for ID,isol in zip(el_IDWPs,el_isolWPs):
  for trig in el_trigWPs:
    c.setalg("ElectronEfficiencyCorrector", generateElectronEfficiencyCorrector(path_el_eff,ID,isol,trig) )
c.setalg("ElectronEfficiencyCorrector", generateElectronEfficiencyCorrector(path_el_eff,"TightLLH","","") )
c.setalg("ElectronEfficiencyCorrector", generateElectronEfficiencyCorrector(path_el_eff,"LooseAndBLayerLLH","_isolLoose","") )

SSDiLepTreeAlgoDict["m_elDetailStr"] = trigger_el_single + " " + trigger_el_double_unrecommended + " " + trigger_el_double_recommended \
                                     + " LooseAndBLayerLLH MediumLLH TightLLH isolNoRequirement isolLoose kinematic trigger isolation PID trackparams effSF"

c.setalg("TruthMatchAlgo", TruthMatchAlgoDict)
c.setalg("XSAlgo", XSAlgoDict)
c.setalg("SSDiLepTreeAlgo", SSDiLepTreeAlgoDict)