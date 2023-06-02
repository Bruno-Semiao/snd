# SND@LHC
Follow the instructions at [SND@LHC github](https://github.com/SND-LHC/sndsw) to install the software.

All files mentioned are either in the collaboration software or in this repository.


## Setting up

First connect to the server and type the password.
```
ssh bcaetano@lxplus.cern.ch
```

### Building the Environment (Run this the first time!) 

Run the following commands to build the environment.

```
bash /afs/cern.ch/work/b/bcaetano/private/snd/startAliBuild.sh
```

### Regular (Run this everytime connecting to the server!)

```
bash /afs/cern.ch/work/b/bcaetano/private/snd/startup.sh
```



## Running/Generating Simulations
### Basic Simulations

To simulate a proton colliding with the detector: (pID = 2212)
```
python /afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/run_simSND.py --PG --pID 2212 -n 10 --Estart 10.0 --Eend 11.0 --EVx -26.0 --EVy 34.0 --EVz 280
```

Then digitize the data:
```
python /afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/run_digiSND.py -g [geoFile] -f [inputFile]
```

### More Complex Simulations

Generate Geofile; generate gdml file:
```
root [0] TFile * f = new TFile("/eos/experiment/sndlhc/convertedData/commissioning/TI18/geofile_sndlhc_TI18_V7_22November2022.root")
root [1] TGeoManager * geo = (TGeoManager*) f->Get("FAIRGeom")
root [2] geo->Export("geofile_sndlhc_TI18_V7.gdml")

```

Generate only muon neutrinos (-14,14) in the Muon System:
```
gevgen_fnal -f "/eos/experiment/sndlhc/MonteCarlo/FLUKA/neutrino_up_14TeV/SND_neutrinos_14TeV_20M_gsimple.root,,-14,14" -g /afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/SimResults/MoreResults_18kPlus/geofile_sndlhc_TI18_V7.gdml -t "+volMuFilter" -L "cm" -D "g_cm3" -e 2.0e18 -o genie_events --tune SNDG18_02a_01_000 --cross-sections /eos/experiment/sndlhc/MonteCarlo/Neutrinos/Genie/splines/genie_splines_GENIE_v32_SNDG18_02a_01_000.xml
```

Conversions:
```
gntpc -i genie_events.0.ghep.root -f gst -o genie_events.gst.root -c
addAuxiliaryToGST genie_events.0.ghep.root genie_events.gst.root
```

Run simulation:
```
python /afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/run_simSND.py --Genie 4 -f /afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/SimResults/genie_events.gst.root -i 0 -n 100
```

Digitize data:
```
python /afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/run_digiSND.py -g geofile_full.Genie-TGeant4.root -f sndLHC.Genie-TGeant4.root
```

[More information can be found here.](https://twiki.cern.ch/twiki/bin/viewauth/SndLHC/NeutrinoInteractionEventsWithGENIE)

## Getting Information

### Geo Information
To get geo information of the detector run:
```
python /afs/cern.ch/work/b/bcaetano/private/snd/sndsw/macro/getGeoInformation.py -g [Geometry file] -l [Level of detail]
```



## Calculating Efficiencies

Apply constraints in class Internships in file:
```
/afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/scripts/UpdatedSurvey-MufiScifi.py
```

To run simulations do:
```
/afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/scripts/GetWeightsForEff.sh
```

Finally use the file that was created to calculate the percentages, by running:
```
/afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/scripts/CalculateEfficiencies.py
```



## Plotting Events
Run:
```
python -i /afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/scripts/2dEventDisplay.py -p /afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/SimResults/00100/ -f sndLHC.Genie-TGeant4_dig.root -g /afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/SimResults/00100/geofile_full.Genie-TGeant4.root 
```
Then: (withHoughTrack - Hough Method; withTrack - Simple Tracking Method)
```
loopEvents(save=True, auto=True, start=0, withHoughTrack = 3, withTrack = 3)
```


To  copy plot to cumputer: (Read section Useful Methods->Exchanging files between Server and Local Cumputer)
```
rsync --rsh="sshpass -f /home/bruno/Documents/SND/cernP ssh -l bcaetano" lxplus.cern.ch:/afs/cern.ch/work/b/bcaetano/private/snd/sndsw/shipLHC/scripts/plots/00100 ~/Documents/images/ -a
```





## Useful Methods
### Exchanging files between Server and Local Cumputer

To easily copy things from your computer to the server we can use *rsync*.
In this example I'm copying all the files in scripts in my computer to the scripts folder in the server. The password to acess the server is stored in the file *cernP*. 

```
rsync --rsh="sshpass -f /home/bruno/Documents/SND/cernP ssh -l bcaetano" ~/Documents/SND/sndsw/shipLHC/scripts/* lxplus.cern.ch:~/private/SND/sndsw/shipLHC/scripts/
```

### Working on the server
To edit files directly on the server I'm using *Visual Studio* with the extension *Remote-SSH*.

Simply add the extension, access it via *Ctrl+Shift+P*, and connect to the server as usual.

## Deprecated Methods
### Automaticaly copying files Server <-> Local
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
