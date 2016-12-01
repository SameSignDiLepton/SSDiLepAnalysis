#!/bin/bash

username=mmuskinj

#prodtag=EE_MUMU_failed3
#prodtag=HLT_2mu10
#prodtag=multitrig_V2
#prodtag=eemumu_failed3
#prodtag=eemumu_res_p2528
#prodtag=presc
#prodtag=allsingle
prodtag=v2ntuples_18232ifb

##infilepath="/home/fscutti/Analysis/SSDiLepAnalysis/doc/grid_input.txt"
##infilepath="/home/fscutti/Analysis/SSDiLepAnalysis/doc/single_grid_input.txt"
##infilepath="/home/fscutti/Analysis/SSDiLepAnalysis/doc/failed_jobs.txt"

## EE_MUMU
##infilepath="/home/fscutti/Analysis/SSDiLepAnalysis/doc/resubmit_grid_input.txt"
##infilepath="/home/fscutti/Analysis/SSDiLepAnalysis/doc/data15_13TeV_physics_Main_DAOD_EXOT12_p2436.txt"
##infilepath="/home/fscutti/Analysis/SSDiLepAnalysis/doc/failed_jobs.txt"
##infilepath="/home/fscutti/Analysis/SSDiLepAnalysis/doc/mc15_13TeV_DCH_DAOD_EXOT12_a810.txt"

## eemumu (uniform derivation tag on bkd and data+sig)
##infilepath="/home/fscutti/Analysis/SSDiLepAnalysis/doc/submit_p2495_p2436.txt"
## infilepath="/home/fscutti/Analysis/SSDiLepAnalysis/doc/submit_p2495_p2436_failed.txt"
## infilepath="/home/fscutti/Analysis/SSDiLepAnalysis/doc/data15_13TeV_physics_Main_DAOD_EXOT12_p2528.txt"

#infilepath="/home/fscutti/Analysis/SSDiLepAnalysis/doc/data_bkg_sig.txt"
infilepath="/afs/cern.ch/work/g/gorisek/miha/submitV2NtuplesMiha/SSDiLepAnalysis/doc/EXOT0_temp.txt"


configpath="$ROOTCOREBIN/user_scripts/SSDiLepAnalysis/jobOptions_SSDiLep_v2.py"

current_time="$(date +'%d-%m-%Y-%T')"
outdir=output_grid_DxAOD-2015-13TeV_${current_time}

#inSE=INFN-T1_DATADISK,MWT2_DATADISK

destSE=AUSTRALIA-ATLAS_LOCALGROUPDISK
#exclSE=ANALY_IHEP,ANALY_JINR,ANALY_IHEP_GLEXEC,ANALY_RRC-KI-HPC,ANALY_RRC-KI-T1,IHEP_MCORE,IHEP_PROD,RRC-KI-HPC2,RRC-KI-T1,RRC-KI-T1_MCORE,RRC-KI-T1_TEST,ANALY_MWT2_SL6,ANALY_PIC_SL6,ANALY_TRIUMF,ANALY_INFN-ROMA1,ANALY_INFN-NAPOLI,ANALY_BNL_SHORT,ANALY_BNL_LONG

#exclSE=ANALY_INFN-FRASCATI,ANALY_FREIBURG,ANALY_FZK,ANALY_FZK_HI,ANALY_FZK_SHORT,ANALY_LANCS_SL6,ANALY_ARNES,ANALY_GRIF-LPNHE,ANALY_IFIC,ANALY_NSC,ANALY_QMUL_HIMEM_SL6,ANALY_QMUL_SL6,ANALY_SiGNET,ANALY_UAM,ANALY_UIO   

##exclSE=ANALY_INFN-T1,ANALY_MWT2_SL6,ANALY_OU_OCHEP_SWT2,ANALY_SWT2_CPB,ANALY_BU_ATLAS_Tier2_SL6,ANALY_HU_ATLAS_Tier2,ANALY_PIC_SL6,ANALY_MANC_SL6,ANALY_OX_SL6,ANALY_DCSC,ANALY_LUNARC,ANALY_SCINET,ANALY_SLAC,RU-Protvino-IHEP


exclSE=OUHEP_OSG,INFN-ROMA2,ru-Moscow-FIAN-LCG2,UNI-DORTMUND,RRC-KI-T1,OU_OCHEP_SWT2,SFU-LCG2,PSNC,UKI-SCOTGRID-GLASGOW,UNI-FREIBURG,UNIBE-LHEP

##exclSE=RU-Protvino-IHEP

gridDSname="user.${username}.SSDiLep.${prodtag}.%in:name[2]%.%in:name[3]%"

#xAH_run.py -vv --files ${infilepath} --config ${configpath} --inputList --inputDQ2 --submitDir ${outdir} prun --optGridMergeOutput=1 --optGridNFilesPerJob=1.0 --optGridDestSE=${destSE} --optGridOutputSampleName=${gridDSname} --optGridExcludedSite=${exclSE} #--optGridSite=${inSE} 

xAH_run.py -vv --files ${infilepath} --config ${configpath} --inputList --inputDQ2 --submitDir ${outdir} prun --optGridMergeOutput=1 --optGridNFilesPerJob=1.0 --optGridOutputSampleName=${gridDSname} --optGridExcludedSite=${exclSE} 





