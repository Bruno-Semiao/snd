#!/bin/bash

dir=/afs/cern.ch/user/b/bcaetano/private/SND/sndsw/shipLHC/SimResults/Neutrino_Muon_up_14TeV_18576


rm EventsData.csv

for d in $dir/*
{
        python /afs/cern.ch/user/b/bcaetano/private/SND/sndsw/shipLHC/scripts/UpdatedSurvey-MufiScifi.py -f "$d/sndLHC.Genie-TGeant4_dig.root" -c Internship -g "$dir/00000/geofile_full.Genie-TGeant4.root" -r -1 -i $d
}
