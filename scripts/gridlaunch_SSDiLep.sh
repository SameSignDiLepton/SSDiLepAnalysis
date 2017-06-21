#!/bin/bash

username=mmuskinj




# prodtag=EXOT12MC_v3nomina
prodtag=EX12MC.v3.sys.001
# prodtag=EX12MC.v3.nom.002



# infilepath="/afs/cern.ch/work/g/gorisek/miha/analysisFramework/SSDiLepAnalysis/doc/EXOT12MC_Feb2017.txt"
# infilepath="/afs/cern.ch/work/g/gorisek/miha/analysisFramework/SSDiLepAnalysis/doc/EXOT12MC_Feb2017_2.txt"
# infilepath="/afs/cern.ch/work/g/gorisek/miha/analysisFramework/SSDiLepAnalysis/doc/EXOT12MC_Feb2017_3.txt"
# infilepath="/afs/cern.ch/work/g/gorisek/miha/analysisFramework/SSDiLepAnalysis/doc/EXOT12MC_Feb2017_3.txt"
# infilepath="/afs/cern.ch/work/g/gorisek/miha/analysisFramework/SSDiLepAnalysis/doc/EXOT12MC_Feb2017_ttbar_sys.txt"
infilepath="/afs/cern.ch/work/g/gorisek/miha/analysisFramework/SSDiLepAnalysis/doc/EXOT12MC_RARE3.txt"
# infilepath="/afs/cern.ch/work/g/gorisek/miha/analysisFramework/SSDiLepAnalysis/doc/EXOT12MC_Feb2017_4.txt"
# infilepath="/afs/cern.ch/work/g/gorisek/miha/analysisFramework/SSDiLepAnalysis/doc/EXOT12MC_Feb2017_typ3.txt"
# infilepath="/afs/cern.ch/work/g/gorisek/miha/analysisFramework/SSDiLepAnalysis/doc/EXOT12MCsig_Feb2017.txt"
# infilepath="/afs/cern.ch/work/g/gorisek/miha/analysisFramework/SSDiLepAnalysis/doc/EXOT12MCsig_Feb2017_2.txt"
# infilepath="/afs/cern.ch/work/g/gorisek/miha/analysisFramework/SSDiLepAnalysis/doc/EXOT12MCsig_Feb2017_3.txt"
# infilepath="/afs/cern.ch/work/g/gorisek/miha/analysisFramework/SSDiLepAnalysis/doc/EXOT12MCsig_Feb2017_typ3.txt"
# infilepath="/afs/cern.ch/work/g/gorisek/miha/analysisFramework/SSDiLepAnalysis/doc/EXOT12MC_higgs.txt"
# infilepath="/afs/cern.ch/work/g/gorisek/miha/analysisFramework/SSDiLepAnalysis/doc/EXOT12Data_Feb2017.txt"
# infilepath="/afs/cern.ch/work/g/gorisek/miha/analysisFramework/SSDiLepAnalysis/doc/EXOT12Data_Feb2017_broken.txt"
# infilepath="/afs/cern.ch/work/g/gorisek/miha/analysisFramework/SSDiLepAnalysis/doc/EXOT19Data_Feb2017.txt"
# infilepath="/afs/cern.ch/work/g/gorisek/miha/analysisFramework/SSDiLepAnalysis/doc/EXOT19Data_Feb2017_broken.txt"
# infilepath="/afs/cern.ch/work/g/gorisek/miha/analysisFramework/SSDiLepAnalysis/doc/EXOT12MC_DCH_Feb2017.txt"




configpath="$ROOTCOREBIN/user_scripts/SSDiLepAnalysis/jobOptions_SSDiLep_v3.py"

current_time="$(date +'%d-%m-%Y-%T')"
outdir=output_grid_DxAOD-2015-13TeV_${current_time}


destSE=SIGNET_LOCALGROUPDISK


exclSE=FZK-LCG2,T1_DE_KIT,Arizona,DukeT3,T2_CN_Beijing,NDGF-T1,T2_US_Florida,HK-LCG2,UKI-SOUTHGRID-RALPP,SMU_HPC,ru-Moscow-FIAN-LCG2,UNICPH-NBI,OUHEP_OSG,UFlorida-HPC,Indiana,BEIJING-LCG2,OU_OCHEP_SWT2


gridDSname="user.${username}.SSDiLep.${prodtag}.%in:name[2]%.%in:name[3]%"


# xAH_run.py -vv --files ${infilepath} --config ${configpath} --inputList --inputRucio --submitDir ${outdir} prun --optGridMergeOutput=1 --optGridNFilesPerJob=1.0 --optGridOutputSampleName=${gridDSname} --optGridExcludedSite=${exclSE}
# xAH_run.py -vv --files ${infilepath} --config ${configpath} --inputList --inputRucio --submitDir ${outdir} prun --optGridMergeOutput=1 --optGridNFilesPerJob=1.0 --optGridOutputSampleName=${gridDSname} --optGridDestSE=${destSE} 
xAH_run.py -vv --files ${infilepath} --config ${configpath} --inputList --inputRucio --submitDir ${outdir} prun --optGridMergeOutput=1 --optGridNFilesPerJob=1.0 --optGridOutputSampleName=${gridDSname} --optGridExcludedSite=${exclSE} --optGridDestSE=${destSE} 





