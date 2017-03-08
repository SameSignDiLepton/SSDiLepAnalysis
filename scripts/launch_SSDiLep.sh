#!/bin/bash

# inDS="mc15_13TeV.301017.PowhegPythia8EvtGen_AZNLOCTEQ6L1_DYee_4500M5000.merge.DAOD_EXOT12.e3649_s2576_s2132_r7772_r7676_p2952"
# sample="DAOD_EXOT12.10342742._000001.pool.root.1"

# inDS="mc15_13TeV.361106.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Zee.merge.DAOD_EXOT12.e3601_s2576_s2132_r7725_r7676_p2823"
# sample="DAOD_EXOT12.09520232._000002.pool.root.1"

inDS="mc15_13TeV.363490.Sherpa_221_NNPDF30NNLO_llll.merge.DAOD_EXOT12.e5332_s2726_r7772_r7676_p2949"
sample="DAOD_EXOT12.10711285._000038.pool.root.1"

# inDS="mc15_13TeV.306554.Pythia8EvtGen_A14NNPDF23LO_DCH1000.merge.DAOD_EXOT12.e5408_a766_a821_r7676_p2949"
# sample="DAOD_EXOT12.10655842._000001.pool.root.1"

# inDS="data16_13TeV.00298609.physics_Main.merge.DAOD_EXOT12.f698_m1594_p2950"
# sample="DAOD_EXOT12.10323328._000053.pool.root.1"

# inDS="data16_13TeV.00302380.physics_Main.merge.DAOD_EXOT19.f711_m1620_p2950"
# sample="DAOD_EXOT19.10324909._000047.pool.root.1"

infilepath="/afs/cern.ch/work/g/gorisek/miha/${inDS}/${sample}"

# ------------------------------------------------------------------------------------

# tokenize inDS using '.' as separator
#
tokens=(${inDS//./ })
configpath="$ROOTCOREBIN/user_scripts/SSDiLepAnalysis/jobOptions_SSDiLep_v3.py"
current_time="$(date +'%d-%m-%Y-%T')"
outdir=output_local_DxAOD-2015-13TeV_${tokens[2]}_${current_time}
nevents=1000

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

#valgrind --trace-children=yes --tool=memcheck --leak-check=yes --show-reachable=yes --num-callers=20 --track-fds=yes --track-origins=yes --log-file=valgrind.log SSDiLepAnalysis/scripts/launch_SSDiLep.sh
#valgrind --trace-children=yes --tool=memcheck --leak-check=yes --num-callers=20 --track-fds=yes --log-file=valgrind.log SSDiLepAnalysis/scripts/launch_SSDiLep.sh