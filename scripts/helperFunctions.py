# tool for generating the ElectronEfficiencyCorrector dictionary 
#___________________________________________________________________
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
