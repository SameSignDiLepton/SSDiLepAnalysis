#!/bin/bash

username=mmuskinj




prodtag=EXOT12MC_v3nom




infilepath="/afs/cern.ch/work/g/gorisek/miha/analysisFramework/SSDiLepAnalysis/doc/EXOT12MC_Feb2017.txt"
# infilepath="/afs/cern.ch/work/g/gorisek/miha/analysisFramework/SSDiLepAnalysis/doc/EXOT12MC_Feb2017_2.txt"
# infilepath="/afs/cern.ch/work/g/gorisek/miha/analysisFramework/SSDiLepAnalysis/doc/EXOT12Data_Feb2017.txt"
# infilepath="/afs/cern.ch/work/g/gorisek/miha/analysisFramework/SSDiLepAnalysis/doc/EXOT12MC_DCH_Feb2017.txt"




configpath="$ROOTCOREBIN/user_scripts/SSDiLepAnalysis/jobOptions_SSDiLep_v3.py"

current_time="$(date +'%d-%m-%Y-%T')"
outdir=output_grid_DxAOD-2015-13TeV_${current_time}


destSE=SIGNET_LOCALGROUPDISK


exclSE=FZK-LCG2,HEPHY-UIBK,NDGF-T1,RAL-LCG2,SMU_HPC,ARGO,Indiana,ru-Moscow-FIAN-LCG2,OU_OCHEP_SWT2,CSCS-LCG2,T1_UK_RAL,UKI-SOUTHGRID-RALPP,UNICPH-NBI,OUHEP_OSG,IN2P3-CC-T3,ANLASC,T2_GR_Ioannina,CA-VICTORIA-WESTGRID-T2,T1_DE_KIT,SARA-MATRIX,T1_FR_CCIN2P3,RAL-Azure,RAL-LCG2-ECHO,IN2P3-CC,T1_RU_JINR,IAAS,UNI-FREIBURG

gridDSname="user.${username}.SSDiLep.${prodtag}.%in:name[2]%.%in:name[3]%"


xAH_run.py -vv --files ${infilepath} --config ${configpath} --inputList --inputRucio --submitDir ${outdir} prun --optGridMergeOutput=1 --optGridNFilesPerJob=1.0 --optGridOutputSampleName=${gridDSname} --optGridExcludedSite=${exclSE}
# xAH_run.py -vv --files ${infilepath} --config ${configpath} --inputList --inputRucio --submitDir ${outdir} prun --optGridMergeOutput=1 --optGridNFilesPerJob=1.0 --optGridOutputSampleName=${gridDSname} --optGridExcludedSite=${exclSE} --optGridDestSE=${destSE} 





