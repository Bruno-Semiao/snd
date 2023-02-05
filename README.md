# SND@LHC

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

Run the following commands to setup the environment (alienv).
```
source ~/private/SND/startup.sh && Run
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

### Track Information
Class defining the tracks can be found [here](https://github.com/SND-LHC/sndsw/blob/master/shipdata/ShipMCTrack.h).


