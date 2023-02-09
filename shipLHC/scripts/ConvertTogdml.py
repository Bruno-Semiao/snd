import ROOT
from ROOT import TFile
from ROOT import TGeoManager
from argparse import ArgumentParser

f = ROOT.TFile.Open("/eos/experiment/sndlhc/MonteCarlo/FLUKA/neutrino_down_13TeV/SND_neutrinos_13TeV_down_19p95M_z481p22m.root")
geo = TGeoManager("Geo", "GeoT")
geo = f.Get("FAIRGeom")
geo.Export("SND_neutrinos_13TeV_down_19p95M_z481p22m_geofile.gdml")
