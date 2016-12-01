#!/bin/bash


#inDS="data16_13TeV.00304494.physics_Main.merge.DAOD_EXOT12.f716_m1620_p2840"
#inDS="data16_13TeV.00304494.physics_Main.merge.DAOD_EXOT19.f716_m1620_p2840"
inDS="mc15_13TeV.301003.PowhegPythia8EvtGen_AZNLOCTEQ6L1_DYee_400M600.merge.DAOD_EXOT0.e3649_s2576_s2132_r7772_r7676_p2669"
#inDS="mc15_13TeV.301006.PowhegPythia8EvtGen_AZNLOCTEQ6L1_DYee_1000M1250.merge.DAOD_EXOT12.e3649_s2576_s2132_r7772_r7676_p2823"

#inDS="data15_13TeV.00284484.physics_Main.merge.DAOD_EXOT19.r7562_p2521_p2840"


#sample="DAOD_EXOT12.09582252._000005.pool.root.1"
#sample="DAOD_EXOT19.09582252._000010.pool.root.1"
sample="DAOD_EXOT0.08616868._000001.pool.root.1"
#sample="DAOD_EXOT12.09520314._000001.pool.root.1"

#sample="DAOD_EXOT19.09581433._000066.pool.root.1"


infilepath="/afs/cern.ch/work/g/gkramber/miha/testDxAOD/${inDS}/${sample}"

# ------------------------------------------------------------------------------------

# tokenize inDS using '.' as separator
#
tokens=(${inDS//./ })
configpath="$ROOTCOREBIN/user_scripts/SSDiLepAnalysis/jobOptions_SSDiLep_v2.py"
current_time="$(date +'%d-%m-%Y-%T')"
outdir=output_local_DxAOD-2015-13TeV_${tokens[2]}_${current_time}
nevents=200

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
