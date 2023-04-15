import ROOT
import shipLHC_conf as sndDet_conf
import SndlhcGeo
import os
from ROOT import TLorentzVector
from ROOT import TVector
from ROOT import TFile

#geometry_file_location = "/eos/experiment/sndlhc/MonteCarlo/Neutrinos/Genie/sndlhc_13TeV_down_volTarget_100fb-1_SNDG18_02a_01_000/0/geofile_full.Genie-TGeant4.root"

#if not os.path.exists(geometry_file_location):
#  print("Oopsies")

#snd_geo = SndlhcGeo.GeoInterface(geometry_file_location)

cbmsim = ROOT.TChain("gst") #t tree for root files; gst tree for gst.root files


input_file = "~/private/SND/sndsw/shipLHC/SimResults/neutrino_up_14TeV/genie_events.gst.root"

if not os.path.exists(input_file):
  print("Oopsies input file for folder ")

cbmsim.Add(input_file)

print("TChain contains "+str(cbmsim.GetEntries())+" events.")

cbmsim.Print()