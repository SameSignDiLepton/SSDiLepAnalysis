#!/bin/bash

#inDS="mc15_13TeV.410000.PowhegPythiaEvtGen_P2012_ttbar_hdamp172p5_nonallhad.merge.DAOD_EXOT12.e3698_s2608_s2183_r7725_r7676_p2927"
#sample="DAOD_EXOT12.10140311._000073.pool.root.1" 

#inDS="data16_13TeV.00310863.physics_Main.merge.DAOD_EXOT12.f756_m1710_p2933"
#sample="DAOD_EXOT12.10154245._000237.pool.root.1" 



#inDS="data15_13TeV"
#sample="DAOD_HIGG3D3.08602173._000004.pool.root.1"
##sample="DAOD_HIGG3D3.08601488._000009.pool.root.1"
#sample="DAOD_HIGG3D3.08602705._000023.pool.root.1"
#sample="DAOD_EXOT12.08607164._000011.pool.root.1"

#inDS="data16_13TeV"
#sample="DAOD_HIGG3D3.08562588._000003.pool.root.1"
#sample="DAOD_EXOT12.09582167._000012.pool.root.1"
#sample="DAOD_EXOT12.09582167._000080.pool.root.1"

#inDS="data16_13TeV.00303817.physics_Main.merge.DAOD_HIGG3D3.f716_m1620_p2840"
#sample="merged.root"
#sample="DAOD_HIGG3D3.09581914._000003.pool.root.1"

#inDS="HIGG3D3test"
#sample="DAOD_HIGG3D3.08583139._000001.pool.root.1" #p2666

#inDS="EXOT12test"
#sample="DAOD_EXOT12.test_size_MC_ttbar.pool.root"
#sample="DAOD_EXOT12.test_size_data_EXOT12_slimmingSimilarToEXOT0.pool.root"
#sample="DAOD_EXOT12.08647446._000007.pool.root.1"
#sample="DAOD_EXOT12.08767284._000001.pool.root.1"
#sample="Sherpa_NNPDF30NNLO_Zmumu_Pt0_70_CVetoBVeto.root"

#inDS="EXOT0test"
#sample="DAOD_EXOT0.08613494._000007.pool.root.1"

#inDS="TOPQ1test"
#sample="DAOD_TOPQ1.08551887._000715.pool.root.1"

##inDS="TOPQ1unsktest"
##sample="DAOD_TOPQ1.08614728._000021.pool.root.1"

#inDS="EXOT12newtest"
#sample="DAOD_EXOT12.test_size_MC_DCH800_nightlyRel0_bkgElExtraVariables_20160921.pool.root"
#sample="DAOD_EXOT12.test_size_MC_ttbar_moreTruthInfo.pool.root"

#inDS="DxAODtest"
#sample="AOD.08536744._000001.pool.root.1" #p2666

inDS="mc15_13TeV"
#sample="DAOD_EXOT12.09529848._000001.pool.root.1"
sample="DAOD_EXOT12.09520445._000013.pool.root.1"
##sample="Zmumu.root"
#sample="DAOD_EXOT12.09520232._000002.pool.root.1"
#sample="ttbar_EXOT12_410000.root"

#sample="DAOD_HIGG3D3.09583262._000004.pool.root.1"
#sample="Wmunu_HIGG3D3_p2688.root"

infilepath="/data/fscutti/${inDS}/${sample}"


# ------------------------------------------------------------------------------------

# tokenize inDS using '.' as separator
#
tokens=(${inDS//./ })
#configpath="$ROOTCOREBIN/user_scripts/SSDiLepAnalysis/jobOptions_SSDiMu.py"
##configpath="$ROOTCOREBIN/user_scripts/SSDiLepAnalysis/jobOptions_SSDiLep_v2.py"
configpath="$ROOTCOREBIN/user_scripts/SSDiLepAnalysis/jobOptions_SSDiLep_v3.py"
current_time="$(date +'%d-%m-%Y-%T')"
outdir=output_local_DxAOD-2016-13TeV_${tokens[2]}_${current_time}
nevents=10

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
