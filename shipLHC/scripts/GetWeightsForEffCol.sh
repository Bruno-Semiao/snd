#!/bin/bash

#-------------------------------------COLABORATION-------------------------------------

dir=/eos/experiment/sndlhc/MonteCarlo/Neutrinos/Genie/sndlhc_13TeV_down_volMuFilter_20fb-1_SNDG18_02a_01_000/

#rm EventsCatCol.csv
#rm EventsDataCol.csv

for d in $dir/*
{
        python /afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/scripts/UpdatedSurvey-MufiScifi.py -f "$d/sndLHC.Genie-TGeant4_digCPP.root" -c Internship -g "$d/geofile_full.Genie-TGeant4.root" -r -1 -i $d/sndlhc_+volMuFilter_0.1562e16_SNDG18_02a_01_000.0.gst.root
}

#-------------------------------------My Simulations-------------------------------------

#dir=/afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/SimResults/


#rm EventsCatCol.csv
#rm EventsDataCol.csv

#for d in $dir/*
#{
#        python /afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/scripts/UpdatedSurvey-MufiScifi.py -f "$d/sndLHC.Genie-TGeant4_dig.root" -c Internship2 -g "$d/geofile_full.Genie-TGeant4.root" -r -1 -i $dir/genie_events.gst.root
#}
