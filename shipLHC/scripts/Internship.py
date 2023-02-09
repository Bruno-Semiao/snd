import ROOT
import shipLHC_conf as sndDet_conf
import SndlhcGeo
import shipunit as u
from ShipGeoConfig import ConfigRegistry
from os.path import exists
from ROOT import TLorentzVector, TCanvas, TGraph
from array import array

#__________EDIT THIS__________#
is_histograms = 0 #Want histograms?
print_type = 1 #-1 - Don't print; 0-All particles; 1-Get effeciency for muon neutrinos; 2-check coordinates for mID = -1 or 0; 3 - get FLUKA weights; 4 - MID == 0 o r-1; 5 - Detector Hit ID
zmin = 358.4387
#zmax = 574.4321 #volMuFilter
zmax = 468.4558#First 4 Fe blocks
#geometry_file_location = "/afs/cern.ch/user/b/bcaetano/public/SND/sndsw/shipLHC/SimResults/geofile_full.Pythia8-TGeant4.root"
#input_file = "/afs/cern.ch/user/b/bcaetano/public/SND/sndsw/shipLHC/SimResults/sndLHC.Pythia8-TGeant4_dig.root"

#geometry_file_location = "/afs/cern.ch/user/b/bcaetano/private/SND/sndsw/shipLHC/SimResults/neutrino_up_14TeV_restrains_Z/geofile_full.Genie-TGeant4.root"
#input_folders_path     = "/afs/cern.ch/user/b/bcaetano/private/SND/sndsw/shipLHC/SimResults/neutrino_up_14TeV_restrains_Z/"

geometry_file_location = "/afs/cern.ch/user/b/bcaetano/private/SND/sndsw/shipLHC/SimResults/Neutrino_Muon_up_14TeV_18576/00000/geofile_full.Genie-TGeant4.root"
input_folders_path     = "/afs/cern.ch/user/b/bcaetano/private/SND/sndsw/shipLHC/SimResults/Neutrino_Muon_up_14TeV_18576/"
gst_file               = "/afs/cern.ch/user/b/bcaetano/private/SND/sndsw/shipLHC/SimResults/Neutrino_Muon_up_14TeV_18576/genie_events.gst.root"

input_file_name        = "sndLHC.Genie-TGeant4_dig.root"
data_dump_filename     = "neutrino_up_14TeV_FirstInteraction"
NEventsToCheck = 100
n_files_to_read = 1 #input files
#_____________________________#

#Geo file
if not exists(geometry_file_location):
        print("\n\nGeometry file not found!\n\n")
        exit()

snd_geo = SndlhcGeo.GeoInterface(geometry_file_location)
#snd_geo = ConfigRegistry.loadpy("$SNDSW_ROOT/geometry/sndLHC_geom_config.py")
#print(f"start = {snd_geo.MuFilter.Iron1Dy}; End = {snd_geo.MuFilter.Iron5Dy + snd_geo.MuFilter.FeZ + 1*u.m * 0.5/39}")


#Input file
cbmsim = ROOT.TChain("cbmsim")
n_files_read = 0
for i in range(n_files_to_read):
    print(i)
    if i == 0:
        file_name = f"{input_folders_path}00000/{input_file_name}"
    elif i < 10:
        file_name = f"{input_folders_path}00{100*i}/{input_file_name}"
    elif i < 100:
        file_name = f"{input_folders_path}0{100*i}/{input_file_name}"
    else:
        file_name = f"{input_folders_path}{100*i}/{input_file_name}"
    if not exists(file_name):
        print("\n\nInput file not found!\n\n")
        continue
    this_read = cbmsim.Add(file_name)
    if this_read > 0 :
        print(file_name+" added.")
        n_files_read += 1


#print("\n\n\n")
#cbmsim.Print()
#print("\n\n\n")

#cbmsim.Print()


#Writeable file
try:
    data = open(f"{data_dump_filename}.txt", "x")
except:
    print(f"Overwrite {data_dump_filename}.txt? (y/n)")
    if 'y' in input() or 'Y' in input():
        data = open(f"{data_dump_filename}.txt", "w")
    else:
        print("\nAborting... Change 'data_dump_filename' at shipLHC/scripts/Internships.py\n")
        exit()



#Print information on the particles
is_break = 0
if print_type == 0:#print all particles
    for eventID, event in enumerate(cbmsim):
            print(f"Event number: {eventID}")
            print("--------------------------------------------------------------------------------------------------------------")
            print(f"index |     pID |  mID |    E (GeV) |            StartVertex xyz         |           Momentum xyz\n")

            data.write(f"Event number: {eventID}\n")
            data.write("--------------------------------------------------------------------------------------------------------------\n")
            data.write(f"index |     pID |  mID |    E (GeV) |            StartVertex xyz         |           Momentum xyz\n")

            for index, particle in enumerate(event.MCTrack):
                #TParticle = TLorentzVector(particle.GetEnergy(), particle.GetPx(), particle.GetPy(), particle.GetPz()) #Then you can print
                #if(index>100): break
                print(f"{index:4}  |   {particle.GetPdgCode():5} | {particle.GetMotherId():4} |  {particle.GetEnergy():8.3f}  |  ({particle.GetStartX():9.3f}, {particle.GetStartY():9.3f}, {particle.GetStartZ():9.3f}) |  ({particle.GetPx():9.3f}, {particle.GetPy():9.3f}, {particle.GetPz():9.3f})")
                data.write(f"{index:4}  |   {particle.GetPdgCode():5} | {particle.GetMotherId():4} |  {particle.GetEnergy():8.3f}  |  ({particle.GetStartX():9.3f}, {particle.GetStartY():9.3f}, {particle.GetStartZ():9.3f}) |  ({particle.GetPx():9.3f}, {particle.GetPy():9.3f}, {particle.GetPz():9.3f})\n")
            print("--------------------------------------------------------------------------------------------------------------\n\n")
            data.write("--------------------------------------------------------------------------------------------------------------\n\n")
            if eventID==NEventsToCheck-1: break
elif print_type == 1:
    NEvents = 0
    NCorrectArea = 0
    NMuonGen = 0
    WEvents = 0.0
    WCorrectArea = 0.0
    WMuonGen = 0.0
    if not exists(gst_file):
        print("\n\ngst file not found!\n\n")
        exit()
    gstsim = ROOT.TChain("gst")
    gstsim.Add(gst_file)

    eventID = array( 'f' )
    efficiency = array( 'f' )

    for event, eventGST in zip(cbmsim, gstsim):
        is_break = 0
        NEvents+=1
        WEvents+=eventGST.FLUKA_weight
        if event.MCTrack[0].GetStartZ() >= zmin and event.MCTrack[0].GetStartZ() <= zmax: #Check if in correct area
            NCorrectArea+=1
            WCorrectArea+=eventGST.FLUKA_weight
            for index, particle in enumerate(event.MCTrack): #Check if muon is created
                if (particle.GetPdgCode() == 13 or particle.GetPdgCode() == -13) and particle.GetMotherId() == 0:
                    break
                if index >= 30:
                    is_break = 1
                    break
            if is_break == 1:
                eventID.append(NEvents)
                if WCorrectArea == 0:
                    efficiency.append(0)
                else:
                    efficiency.append(100*WMuonGen/WCorrectArea)
                continue

            NMuonGen+=1
            WMuonGen+=eventGST.FLUKA_weight
        eventID.append(NEvents)
        if WCorrectArea == 0:
            efficiency.append(0)
        else:
            efficiency.append(100*WMuonGen/WCorrectArea)


        if NEvents==NEventsToCheck: break

    #Efficiency with iterations
    EffVsItt_c = ROOT.TCanvas( '"EffVsItt"', '"EffVsItt"', 10, 40, 800, 600 )
    #EffVsItt_c.Range( 0, 0, 100, 18000 )
    print(f"Entries {cbmsim.GetEntries()} Events {len(eventID)} Eff {str(len(efficiency))}")
    EffVsItt_g = ROOT.TGraph(cbmsim.GetEntries(), eventID, efficiency)


    EffVsItt_g.Draw("P")
    EffVsItt_c.Print("EfficiencyVsItt.png")

elif print_type == 2:
    TotNEvents = 0
    NumberOfEvents = 0
    for eventID, event in enumerate(cbmsim):
        TotNEvents+=1
        for index, particle in enumerate(event.MCTrack):
            if (particle.GetStartZ() >= zmin and particle.GetStartZ() <= zmax) and (particle.GetMotherId() == -1):
                NumberOfEvents+=1

                #print(f"Event number: {eventID}")
                #print("--------------------------------------------------------------------------------------------------------------")
                #print(f"index |     pID |  mID |    E (GeV) |            StartVertex xyz         |           Momentum xyz\n")

                #data.write(f"Event number: {eventID}\n")
                #data.write("--------------------------------------------------------------------------------------------------------------\n")
                #data.write(f"index |     pID |  mID |    E (GeV) |            StartVertex xyz         |           Momentum xyz\n")
                #TParticle = TLorentzVector(particle.GetEnergy(), particle.GetPx(), particle.GetPy(), particle.GetPz()) #Then you can print
                #if(index>100): break
                #print(f"{index:4}  |   {particle.GetPdgCode():5} | {particle.GetMotherId():4} |  {particle.GetEnergy():8.3f}  |  ({particle.GetStartX():9.3f}, {particle.GetStartY():9.3f}, {particle.GetStartZ():9.3f}) |  ({particle.GetPx():9.3f}, {particle.GetPy():9.3f}, {particle.GetPz():9.3f})")
                #data.write(f"{index:4}  |   {particle.GetPdgCode():5} | {particle.GetMotherId():4} |  {particle.GetEnergy():8.3f}  |  ({particle.GetStartX():9.3f}, {particle.GetStartY():9.3f}, {particle.GetStartZ():9.3f}) |  ({particle.GetPx():9.3f}, {particle.GetPy():9.3f}, {particle.GetPz():9.3f})\n")
                #print("--------------------------------------------------------------------------------------------------------------\n\n")
                #data.write("--------------------------------------------------------------------------------------------------------------\n\n")

        if eventID==NEventsToCheck-1: break
elif print_type == 3:
    if not exists(gst_file):
        print("\n\ngst file not found!\n\n")
        exit()
    gstsim = ROOT.TChain("gst")
    gstsim.Add(gst_file)
    for eventID, event in enumerate(gstsim):
            print(event.FLUKA_weight)
            if eventID==NEventsToCheck-1: break
elif print_type == 4:#print all particles
    for eventID, event in enumerate(cbmsim):
            print(f"Event number: {eventID}")
            print("--------------------------------------------------------------------------------------------------------------")
            print(f"index |     pID |  mID |    E (GeV) |            StartVertex xyz         |           Momentum xyz\n")

            data.write(f"Event number: {eventID}\n")
            data.write("--------------------------------------------------------------------------------------------------------------\n")
            data.write(f"index |     pID |  mID |    E (GeV) |            StartVertex xyz         |           Momentum xyz\n")

            for index, particle in enumerate(event.MCTrack):
                if particle.GetMotherId() == 0 or particle.GetMotherId() == -1:
                    #TParticle = TLorentzVector(particle.GetEnergy(), particle.GetPx(), particle.GetPy(), particle.GetPz()) #Then you can print
                    #if(index>100): break
                    print(f"{index:4}  |   {particle.GetPdgCode():5} | {particle.GetMotherId():4} |  {particle.GetEnergy():8.3f}  |  ({particle.GetStartX():9.3f}, {particle.GetStartY():9.3f}, {particle.GetStartZ():9.3f}) |  ({particle.GetPx():9.3f}, {particle.GetPy():9.3f}, {particle.GetPz():9.3f})")
                    data.write(f"{index:4}  |   {particle.GetPdgCode():5} | {particle.GetMotherId():4} |  {particle.GetEnergy():8.3f}  |  ({particle.GetStartX():9.3f}, {particle.GetStartY():9.3f}, {particle.GetStartZ():9.3f}) |  ({particle.GetPx():9.3f}, {particle.GetPy():9.3f}, {particle.GetPz():9.3f})\n")
            print("--------------------------------------------------------------------------------------------------------------\n\n")
            data.write("--------------------------------------------------------------------------------------------------------------\n\n")
            if eventID==NEventsToCheck-1: break
elif print_type==5:
    for eventID, event in enumerate(cbmsim):
        data.write("\n")
        for hit in event.Digi_MuFilterHits:
            data.write(str(hit.GetDetectorID())+"\n")
        if eventID==NEventsToCheck-1: break


data.close()
if print_type == 2:
    print(f"\nNumber of events in interval: {NumberOfEvents}\nTotal number of events: {TotNEvents}\nPercentage: {100*NumberOfEvents/TotNEvents}\n")
if print_type ==1:
    print(f"\n\nEvents:\n     Total = {NEvents}\n     In correct area = {NCorrectArea}\n     In this area and generated a muon = {NMuonGen}\n")
    print(f"\nWeights:\n     Total = {WEvents:.9}\n     In correct area = {WCorrectArea:.9}\n     In this area and generated a muon = {WMuonGen:.9}\n")
    print(f"\nEfficiencies (%):\n     Correct area = {100*WCorrectArea/WEvents:.7}\n     Muon generated = {100*WMuonGen/WCorrectArea:.7}\n     Correct area and Muon Generated = {100*WMuonGen/WEvents:.7}\n\n")
#gst.FLUKA_weight

if is_histograms==1:
    #Create histogram on Starting Vertex
    detector_x_range = [-88.0188, 3.6492]
    detector_y_range = [-2.3017, 71.5810]
    target_z_range   = [358.4387, 574.4321]

    n_bins = 200
    mc_lumi = 150 #* n_files_read       #luminosity of each file; 150 is total lumi
    target_lumi = 150                   #Scale lumi to 400
    lumi_weight = target_lumi/mc_lumi

    # XY projection
    h_vertex_xy = ROOT.TH2D("h_vertex_xy", "Neutrino interaction vertices;x [cm];y [cm]", n_bins, detector_x_range[0], detector_x_range[1], n_bins, detector_y_range[0], detector_y_range[1])
    # ZY projection
    h_vertex_zy = ROOT.TH2D("h_vertex_zy", "Neutrino interaction vertices;z [cm];y [cm]", n_bins, target_z_range[0], target_z_range[1], n_bins, detector_y_range[0], detector_y_range[1])
    # ZY projection
    h_vertex_zx = ROOT.TH2D("h_vertex_zx", "Neutrino interaction vertices;z [cm];x [cm]", n_bins, target_z_range[0], target_z_range[1], n_bins, detector_x_range[0], detector_x_range[1])

    # Loop over events
    for i_event, event in enumerate(cbmsim) :
        if i_event % 100 == 0 :
            print("Reading event number {0}".format(i_event))

        # Get the first track
        incoming_nu = event.MCTrack[0]

        # Fill the histograms
        h_vertex_xy.Fill(incoming_nu.GetStartX(), incoming_nu.GetStartY(), lumi_weight)
        h_vertex_zy.Fill(incoming_nu.GetStartZ(), incoming_nu.GetStartY(), lumi_weight)
        h_vertex_zx.Fill(incoming_nu.GetStartZ(), incoming_nu.GetStartX(), lumi_weight)


    print("Done filling histograms")

    # Remove the ROOT stats box
    ROOT.gStyle.SetOptStat(0)

    c_vertex_xy = ROOT.TCanvas("c_vertex_xy")
    h_vertex_xy.Draw("COLZ")
    c_vertex_xy.Draw()
    c_vertex_xy.Print("c_vertex_xy.png")

    c_vertex_zy = ROOT.TCanvas("c_vertex_zy")
    h_vertex_zy.Draw("COLZ")
    c_vertex_zy.Draw()
    c_vertex_zy.Print("c_vertex_zy.png")

    c_vertex_zx = ROOT.TCanvas("c_vertex_zx")
    h_vertex_zx.Draw("COLZ")
    c_vertex_zx.Draw()
    c_vertex_zx.Print("c_vertex_zx.png")











'''
elif print_type == 1:
    for eventID, event in enumerate(cbmsim):
            print(f"Event number: {eventID}")
            for index, particle in enumerate(event.MCTrack):
                    #if(index>100): break
                    if particle.GetMotherId()==0 or particle.GetMotherId()==-1:
                        print(f"{index}:   {particle.GetPdgCode()};    E = {particle.GetEnergy()} GeV;    MotherID = {particle.GetMotherId()}")
                    if index==0:
                            TProton = TLorentzVector(particle.GetEnergy(), particle.GetPx(), particle.GetPy(), particle.GetPz())
                            #print(str(particle.GetStartX()) + "," + str(particle.GetStartY()) + "," + str(particle.GetStartZ()))
                            continue
            print("\n\n")
            if eventID==0: break
'''



'''
for eventID, event in enumerate(cbmsim):
        print("Event number: " + str(eventID))
        if eventID>10: break
        for index, particle in enumerate(event.MCTrack):
                if(index>100): break
        #	print(str(index) + "  " + str(particle.GetPdgCode()))
                if index==0:
                        TProton = TLorentzVector(particle.GetEnergy(), particle.GetPx(), particle.GetPy($
                        #print("energy = " + str(particle.GetEnergy()) + " GeV")
                        print(str(particle.GetStartX()) + "," + str(particle.GetStartY()) + "," + str(pa$
                        continue
                if particle.GetMotherId()==0:
                        print("HI")
#print("energy = " + str(particle.GetEnergy()) + " GeV")
                        print(str(particle.GetStartX()) + "," + str(particle.GetStartY()) + "," + str(pa$

                #print("MID: " + str(particle.GetMotherId()))
        hitsList = []
        for hits in event.Digi_MuFilterHits:
                Detector = hits.GetDetectorID()
        if Detector not in hitsList: hitsList.append(Detector)
        print(hitsList)
'''
