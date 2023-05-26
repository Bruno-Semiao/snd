import ROOT
import shipLHC_conf as sndDet_conf
import SndlhcGeo
import shipunit as u
from ShipGeoConfig import ConfigRegistry
from os.path import exists
from ROOT import TLorentzVector, TCanvas, TGraph
from array import array
from csv import reader

#Weights
WEvents = 0.0
WCorrectArea = 0.0
#INSIDE CORRECT AREA AND:
WMuonGen = 0.0
WMuonDet = 0.0
WMuonGenDet = 0.0
WFalsePositive = 0.0
WEfficiency = 0.0


#Read file
with open("EventsDataColC.csv", "r") as f:
    reader = reader(f)
    header = next(reader)       #Ignore header
    if header != None:
        for row in reader:
            WEvents+=float(row[0])
            WCorrectArea+=float(row[1])
            WMuonGen+=float(row[2])
            WMuonDet+=float(row[3])
            WEfficiency+=float(row[4])
            WFalsePositive+=float(row[5])


#Probabilities
PArea = WCorrectArea/WEvents
PMGen = WMuonGen/WCorrectArea
PMDet = WMuonDet/WCorrectArea
#PFalsePositive = WFalsePositive/WMuonDet
#Efficiency = WEfficiency/WMuonGen
PFalsePositive = WFalsePositive/WCorrectArea
Efficiency = WEfficiency/WCorrectArea


#print(f"Total: {WEvents}\nCorrect area: {WCorrectArea}\nMuon Gen: {WMuonGen}\nMuon Det: {WMuonDet}\n")
print(f"\n\nCorrect area = {100*PArea:.5} %\nInside the correct area:\n     Muon Gen = {100*PMGen:.5} %\n     Muon Detected = {100*PMDet:.5}\n     Efficiency for detecting muons = {100*Efficiency:.5} %\n     False positives = {100*PFalsePositive:.5} %")

'''
PFalsePositive = WFalsePositive/WCorrectArea
Efficiency = WEfficiency/WCorrectArea

PMGenIfDet = WMuonGenDet/WMuonDet
PMDetIfGen = WMuonGenDet/WMuonGen
PMDetIfNotGen = WMuonDetNotGen/(WCorrectArea-WMuonGen)


#Read file
with open("EventsData.csv", "r") as f:
    reader = reader(f)
    header = next(reader)       #Ignore header
    # Check file as empty
    if header != None:
        for row in reader:
            WEvents+=float(row[0])
            WCorrectArea+=float(row[1])


'''
