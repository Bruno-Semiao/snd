#!/bin/bash

cd /afs/cern.ch/work/b/bcaetano/private/snd;
source source /cvmfs/sndlhc.cern.ch/SNDLHC-2023/Jan22/setUp.sh;   #/cvmfs/sndlhc.cern.ch/SNDLHC-2022/July14/setUp.sh;
aliBuild build sndsw -c $SNDDIST --always-prefer-system;
alienv enter sndsw/latest;
