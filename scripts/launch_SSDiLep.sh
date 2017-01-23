#!/bin/bash

infilepath = "/afs/cern.ch/work/g/gorisek/miha/mc15_13TeV.410000.PowhegPythiaEvtGen_P2012_ttbar_hdamp172p5_nonallhad.merge.DAOD_EXOT12.e3698_s2608_s2183_r7725_r7676_p2823/DAOD_EXOT12.09520689._000053.pool.root.1"


# ------------------------------------------------------------------------------------

# tokenize inDS using '.' as separator
#
tokens=(${inDS//./ })
configpath="$ROOTCOREBIN/user_scripts/SSDiLepAnalysis/jobOptions_SSDiLep_v2.py"
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
