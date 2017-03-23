#!/bin/bash

# check downtime calendar for sites here:
# http://atlas-agis.cern.ch/agis/downtime/calendar/

username=fscutti

prodtag=nHIGG3D3_v9
#prodtag=EXOT12_pv8

#infilepath="/home/fscutti/SSDiLepAnalysis/doc/all_pv2_EXOT12.txt"
#infilepath="/home/fscutti/SSDiLepAnalysis/doc/all_v8_HIGG3D3.txt"
#infilepath="/home/fscutti/SSDiLepAnalysis/doc/jetjet_HIGG3D3.txt"
#infilepath="/home/fscutti/SSDiLepAnalysis/doc/all_v9_HIGG3D3.txt"

infilepath="/home/fscutti/SSDiLepAnalysis/doc/failed_jobs.txt"

configpath="$ROOTCOREBIN/user_scripts/SSDiLepAnalysis/jobOptions_SSDiMu_v3.py"

current_time="$(date +'%d-%m-%Y-%T')"
outdir=output_grid_DxAOD-2016-13TeV_${current_time}

exclSE=OUHEP_OSG,OU_OCHEP_SWT2,ru-Moscow-FIAN-LCG2,CSCS-LCG2,FZK-LCG2,UKI-SOUTHGRID-RALPP,UKI-SCOTGRID-GLASGOW

gridDSname="user.${username}.SSDiLep.${prodtag}.%in:name[2]%.%in:name[3]%"

xAH_run.py -vv --files ${infilepath} --config ${configpath} --inputList --inputDQ2 --submitDir ${outdir} prun --optGridMergeOutput=1 --optGridNFilesPerJob=1.0 --optGridOutputSampleName=${gridDSname} --optGridExcludedSite=${exclSE} 





