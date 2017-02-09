#!/bin/bash

#/afs/cern.ch/work/g/gkramber/miha/mc15_13TeV.410000.PowhegPythiaEvtGen_P2012_ttbar_hdamp172p5_nonallhad.merge.DAOD_SUSY5.e3698_s2608_s2183_r7725_r7676_p2949

inDS="mc15_13TeV.361106.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Zee.merge.DAOD_EXOT12.e3601_s2576_s2132_r7725_r7676_p2823"

sample="DAOD_EXOT12.09520232._000002.pool.root.1"

#infilepath="/afs/cern.ch/work/g/gorisek/miha/DxAOD_EXOT12/${inDS}/${sample}"
#infilepath="/afs/cern.ch/work/p/pleskot/${inDS}/${sample}"
infilepath="/afs/cern.ch/work/g/gorisek/miha/${inDS}/${sample}"
#infilepath="/afs/cern.ch/work/g/gkramber/miha/${inDS}/${sample}"

# ------------------------------------------------------------------------------------

# tokenize inDS using '.' as separator
#
tokens=(${inDS//./ })
configpath="$ROOTCOREBIN/user_scripts/SSDiLepAnalysis/jobOptions_SSDiLep_v3.py"
current_time="$(date +'%d-%m-%Y-%T')"
outdir=output_local_DxAOD-2015-13TeV_${tokens[2]}_${current_time}
nevents=500

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
