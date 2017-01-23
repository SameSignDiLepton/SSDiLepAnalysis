#!/bin/bash

#inDS="mc15_13TeV.410000.PowhegPythiaEvtGen_P2012_ttbar_hdamp172p5_nonallhad.merge.DAOD_EXOT12.e3698_s2608_s2183_r7725_r7676_p2927"
#sample="DAOD_EXOT12.10140311._000073.pool.root.1" 

#inDS="data16_13TeV.00310863.physics_Main.merge.DAOD_EXOT12.f756_m1710_p2933"
#sample="DAOD_EXOT12.10154245._000237.pool.root.1" 

inDS="data16_13TeV"
sample="DAOD_HIGG3D3.08562588._000003.pool.root.1"

infilepath="/data/fscutti/${inDS}/${sample}"

# ------------------------------------------------------------------------------------

# tokenize inDS using '.' as separator
#
tokens=(${inDS//./ })
configpath="$ROOTCOREBIN/user_scripts/SSDiLepAnalysis/jobOptions_SSDiLep.py"
current_time="$(date +'%d-%m-%Y-%T')"
outdir=output_local_DxAOD-2015-13TeV_${tokens[2]}_${current_time}
nevents=2000

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
