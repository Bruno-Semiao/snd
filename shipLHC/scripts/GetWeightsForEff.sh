#!/bin/bash

#-------------------------------------My Simulations-------------------------------------

dir=/afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/SimResults/


#rm EventsCatCol.csv
#rm EventsDataCol.csv

for d in $dir/*
{
        python /afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/scripts/UpdatedSurvey-MufiScifi.py -f "$d/sndLHC.Genie-TGeant4_dig.root" -c Internship -g "$d/geofile_full.Genie-TGeant4.root" -r -1 -i $dir/genie_events.gst.root
}


#python /afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/scripts/UpdatedSurvey-MufiScifi.py -f "/afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/SimResults/00200/sndLHC.Genie-TGeant4_dig.root" -c GetBadParticles -g "/afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/SimResults/00200/geofile_full.Genie-TGeant4.root" -r -1 -i /afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/SimResults/

#python /afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/scripts/UpdatedSurvey-MufiScifi.py -f "/afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/SimResults/00400/sndLHC.Genie-TGeant4_dig.root" -c Internship -g "/afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/scripts/UpdatedSurvey-MufiScifi.py -f "/afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/SimResults/00400/geofile_full.Genie-TGeant4.root" -r -1 -i $d

#python /afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/scripts/UpdatedSurvey-MufiScifi.py -f "/eos/experiment/sndlhc/MonteCarlo/Neutrinos/Genie/sndlhc_13TeV_down_volMuFilter_20fb-1_SNDG18_02a_01_000/0/sndLHC.Genie-TGeant4_digCPP.root" -c Internship -g "/eos/experiment/sndlhc/MonteCarlo/Neutrinos/Genie/sndlhc_13TeV_down_volMuFilter_20fb-1_SNDG18_02a_01_000/0/geofile_full.Genie-TGeant4.root" -r -1 -i /eos/experiment/sndlhc/MonteCarlo/Neutrinos/Genie/sndlhc_13TeV_down_volMuFilter_20fb-1_SNDG18_02a_01_000/0/