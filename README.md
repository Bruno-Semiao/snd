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

### Track Information
Class defining the tracks can be found [here](https://github.com/SND-LHC/sndsw/blob/master/shipdata/ShipMCTrack.h).


