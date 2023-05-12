# SND@LHC
Follow the instructions at [SND@LHC github](https://github.com/SND-LHC/sndsw) to install the software.


## Setting up

First connect to the server and type the password.
```
ssh bcaetano@lxplus.cern.ch
```

### First time or editing "source" files

Run the following commands to build the environment.

```
source ~/private/SND/startAliBuild.sh && Run
```

### Regular

OLD WAY: Run the following commands to setup the environment (alienv).
```
source ~/private/SND/startup.sh && Run
```
NEW WAY:
```
source /cvmfs/sndlhc.cern.ch/SNDLHC-2023/Jan22/setUp.sh
alienv enter sndsw/latest
```


### Keeping things up to date

To easily copy things from your computer to the server we can use *rsync*.
In this example I'm copying all the files in scripts in my computer to the scripts folder in the server. The password to acess the server is stored in the file *cernP*. 

```
rsync --rsh="sshpass -f /home/bruno/Documents/SND/cernP ssh -l bcaetano" ~/Documents/SND/sndsw/shipLHC/scripts/* lxplus.cern.ch:~/private/SND/sndsw/shipLHC/scripts/
```

To keep this automated we can use *crontab*. To copy every 5 seconds run
```
crontab -e
```
And paste the following code:
```
* * * * * rsync --rsh="sshpass -f /home/bruno-semions/Documents/cernP ssh -l bcaetano" ~/Documents/sndsw/shipLHC/scripts/Internship.py lxplus.cern.ch:~/private/SND/sndsw/shipLHC/scripts/

* * * * * sleep 5; rsync --rsh="sshpass -f /home/bruno-semions/Documents/cernP ssh -l bcaetano" ~/Documents/sndsw/shipLHC/scripts/Internship.py lxplus.cern.ch:~/private/SND/sndsw/shipLHC/scripts/

* * * * * sleep 10; rsync --rsh="sshpass -f /home/bruno-semions/Documents/cernP ssh -l bcaetano" ~/Documents/sndsw/shipLHC/scripts/Internship.py lxplus.cern.ch:~/private/SND/sndsw/shipLHC/scripts/

* * * * * sleep 15; rsync --rsh="sshpass -f /home/bruno-semions/Documents/cernP ssh -l bcaetano" ~/Documents/sndsw/shipLHC/scripts/Internship.py lxplus.cern.ch:~/private/SND/sndsw/shipLHC/scripts/

* * * * * sleep 20; rsync --rsh="sshpass -f /home/bruno-semions/Documents/cernP ssh -l bcaetano" ~/Documents/sndsw/shipLHC/scripts/Internship.py lxplus.cern.ch:~/private/SND/sndsw/shipLHC/scripts/

* * * * * sleep 25; rsync --rsh="sshpass -f /home/bruno-semions/Documents/cernP ssh -l bcaetano" ~/Documents/sndsw/shipLHC/scripts/Internship.py lxplus.cern.ch:~/private/SND/sndsw/shipLHC/scripts/

* * * * * sleep 30; rsync --rsh="sshpass -f /home/bruno-semions/Documents/cernP ssh -l bcaetano" ~/Documents/sndsw/shipLHC/scripts/Internship.py lxplus.cern.ch:~/private/SND/sndsw/shipLHC/scripts/

* * * * * sleep 35; rsync --rsh="sshpass -f /home/bruno-semions/Documents/cernP ssh -l bcaetano" ~/Documents/sndsw/shipLHC/scripts/Internship.py lxplus.cern.ch:~/private/SND/sndsw/shipLHC/scripts/

* * * * * sleep 40; rsync --rsh="sshpass -f /home/bruno-semions/Documents/cernP ssh -l bcaetano" ~/Documents/sndsw/shipLHC/scripts/Internship.py lxplus.cern.ch:~/private/SND/sndsw/shipLHC/scripts/

* * * * * sleep 45; rsync --rsh="sshpass -f /home/bruno-semions/Documents/cernP ssh -l bcaetano" ~/Documents/sndsw/shipLHC/scripts/Internship.py lxplus.cern.ch:~/private/SND/sndsw/shipLHC/scripts/

* * * * * sleep 50; rsync --rsh="sshpass -f /home/bruno-semions/Documents/cernP ssh -l bcaetano" ~/Documents/sndsw/shipLHC/scripts/Internship.py lxplus.cern.ch:~/private/SND/sndsw/shipLHC/scripts/

* * * * * sleep 55; rsync --rsh="sshpass -f /home/bruno-semions/Documents/cernP ssh -l bcaetano" ~/Documents/sndsw/shipLHC/scripts/Internship.py lxplus.cern.ch:~/private/SND/sndsw/shipLHC/scripts/
```


## Running Basic Simulations

To simulate a proton colliding with the detector: (pID = 2212)
```
python ../run_simSND.py --PG --pID 2212 -n 10 --Estart 10.0 --Eend 11.0 --EVx -26.0 --EVy 34.0 --EVz 280
```

Then digitize the data:
```
python ../run_digiSND.py -g [geoFile] -f [inputFile]
```



## Getting Information

### Geo Information
To get geo information of the detector run:
```
python /macro/getGeoInformation.py -g [Geometry file] -l [Level of detail]
```

Currently using this geofile:
```
/afs/cern.ch/user/b/bcaetano/private/SND/sndsw/shipLHC/SimResults/Neutrino_Muon_up_14TeV_18576/00000/geofile_full.Genie-TGeant4.root
```

### Track Information
Class defining the tracks can be found [here](https://github.com/SND-LHC/sndsw/blob/master/shipdata/ShipMCTrack.h).




## Calculating Efficiencies

Apply constraints in class Internships in file:
```
/afs/cern.ch/user/b/bcaetano/private/SND/sndsw/shipLHC/scripts/UpdatedSurvey-MufiScifi.py
```

To run simulations do:
```
/afs/cern.ch/user/b/bcaetano/private/SND/sndsw/shipLHC/scripts/GetWeightsForEff.sh
```

Finally use the file created in:
```
/afs/cern.ch/user/b/bcaetano/private/SND/sndsw/shipLHC/scripts/DataDump/EventsData.csv
```

to calculate the percentages, code in file:
```
/afs/cern.ch/user/b/bcaetano/private/SND/sndsw/shipLHC/scripts/CalculateEfficiencies.py
```

## Generating Simulations

Generate Geofile; generate gdml file:
```
root [0] TFile * f = new TFile("/eos/experiment/sndlhc/convertedData/commissioning/TI18/geofile_sndlhc_TI18_V7_22November2022.root")
root [1] TGeoManager * geo = (TGeoManager*) f->Get("FAIRGeom")
root [2] geo->Export("geofile_sndlhc_TI18_V7.gdml")

```

```
gevgen_fnal -f "/eos/experiment/sndlhc/MonteCarlo/FLUKA/neutrino_up_14TeV/SND_neutrinos_14TeV_20M_gsimple.root,,-14,14" -g /afs/cern.ch/user/b/bcaetano/private/SND/sndsw/shipLHC/SimResults/geofile_sndlhc_TI18_V7.gdml -t "+volMuFilter" -L "cm" -D "g_cm3" -e 2.0e17 -o genie_events --tune SNDG18_02a_01_000 --cross-sections /eos/experiment/sndlhc/MonteCarlo/Neutrinos/Genie/splines/genie_splines_GENIE_v32_SNDG18_02a_01_000.xml
```

Conversions:
```
gntpc -i genie_events.0.ghep.root -f gst -o genie_events.gst.root -c
addAuxiliaryToGST genie_events.0.ghep.root genie_events.gst.root
```

Run simulation:
```
python ~/private/SND/sndsw/shipLHC/run_simSND.py --Genie 4 -f ~/private/SND/sndsw/shipLHC/SimResults/genie_events.gst.root -i 0 -n 100
```

Digitize data:
```
python ~/private/SND/sndsw/shipLHC/run_digiSND.py -g geofile_full.Genie-TGeant4.root -f sndLHC.Genie-TGeant4.root
```

## Plotting Events
Run:
```
python -i /afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/scripts/2dEventDisplay.py -p /afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/SimResults/00100/ -f sndLHC.Genie-TGeant4_dig.root -g /afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/SimResults/00100/geofile_full.Genie-TGeant4.root 
```
Then: (withHoughTrack - New Method; withTrack - Old Method)
```
loopEvents(save=True, auto=True, start=0, withHoughTrack = 3, withTrack = 3)
```


To  copy plot to cumputer:
```
rsync --rsh="sshpass -f /home/bruno/Documents/SND/cernP ssh -l bcaetano" lxplus.cern.ch:/afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/scripts/plots/00100 ~/Documents/images/ -a
```

