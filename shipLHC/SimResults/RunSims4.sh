#!/bin/bash

for i in {138..139}
do
  	cd /afs/cern.ch/user/b/bcaetano/private/SND/sndsw/shipLHC/SimResults/Neutrino_Muon_up_14TeV_18576/${i}00
        python ~/private/SND/sndsw/shipLHC/run_simSND.py --Genie 4 -f ~/private/SND/sndsw/shipLHC/SimResults/Neutrino_Muon_up_14TeV_18576/genie_events.gst.root -i ${i}00 -n 100
        python ~/private/SND/sndsw/shipLHC/run_digiSND.py -g geofile_full.Genie-TGeant4.root -f sndLHC.Genie-TGeant4.root
done

for i in {156..159}
do
        cd /afs/cern.ch/user/b/bcaetano/private/SND/sndsw/shipLHC/SimResults/Neutrino_Muon_up_14TeV_18576/${i}00
        python ~/private/SND/sndsw/shipLHC/run_simSND.py --Genie 4 -f ~/private/SND/sndsw/shipLHC/SimResults/Neutrino_Muon_up_14TeV_18576/genie_events.gst.root -i ${i}00 -n 100
        python ~/private/SND/sndsw/shipLHC/run_digiSND.py -g geofile_full.Genie-TGeant4.root -f sndLHC.Genie-TGeant4.root
done
