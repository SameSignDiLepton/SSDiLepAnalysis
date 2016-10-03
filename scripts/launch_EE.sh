#!/bin/bash

#inDS="mc15_13TeV.361063.Sherpa_CT10_llll.merge.DAOD_EXOT12.e3836_s2608_s2183_r7725_r7676_p2666"
inDS="public"

#sample="DAOD_EXOT12.08647446._000005.pool.root.1" #p2666
sample="DAOD_EXOT12.test_size_MC_Zee_nightlyRel0_bkgElExtraVariables_20160922.pool.root" #p2666

#infilepath="/afs/cern.ch/work/g/gorisek/miha/DxAOD_EXOT12/${inDS}/${sample}"
infilepath="/afs/cern.ch/work/p/pleskot/${inDS}/${sample}"


# ------------------------------------------------------------------------------------

# tokenize inDS using '.' as separator
#
tokens=(${inDS//./ })
configpath="$ROOTCOREBIN/user_scripts/SSDiLepAnalysis/jobOptions_EE.py"
current_time="$(date +'%d-%m-%Y-%T')"
outdir=output_local_DxAOD-2015-13TeV_${tokens[2]}_${current_time}
nevents=100

echo ""
echo "Input file path :"
echo ""
echo ${infilepath}
echo ""
echo "Configuring job with :"
echo ""
echo ${configpath}
echo ""
echo "Output will be stored in :"
echo ""
echo ${outdir}
echo ""

xAH_run.py -vv --files ${infilepath} --config ${configpath} --submitDir ${outdir} --nevents ${nevents} direct
