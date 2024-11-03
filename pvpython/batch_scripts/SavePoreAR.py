# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
import os 
import numpy as np
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

ARData = [["g","p","q","pore_AR"]]


fs = [0.05]
qs = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 1.05, 1.1]
gs = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]
C = 2
pathp = r'/home/repos/colloidal_membranes_v2/vtk_results/Round9'
pathexp = r'/home/repos/colloidal_membranes_v2/data_viz/extracted_data/single_pore_round_9'
filename = '/PoreARData.txt'
for g in gs:
    for f in fs:
        for q in qs:
            pathc = pathp+f"/q={q} g={g}"
            ldocs = os.listdir(pathc)
            maxiter = 0
            for st in ldocs:
                if "_" in st:
                    st = st.split("_")[1]
                    iter = int(st.replace(".vtk", ""))
                    if iter > maxiter:
                        maxiter = iter

            if g==0.0 or g==1.0 or g==2.0: gg = round(g)
            else: gg=g
            if q==0.0 or q==1.0 or q==2.0: qq = round(q)
            else: qq=q
            if f==0.0 or f==1.0 or f==2.0: ff = round(f)
            else: ff=f
            # create a new 'Legacy VTK Reader'
            activeSource = LegacyVTKReader(registrationName='SinglePore.vtk*', FileNames=[pathc+f'/SinglePoreg{gg}p{ff}q{qq}_{maxiter}.vtk'])
            data = paraview.servermanager.Fetch(activeSource)
            edgeidxs = [590, 591, 592, 593, 594, 668, 669, 741, 742, 812, 813, 882, 883, 952, 953, 1022, 1023, 1092, 1093, 1162, 1163, 1233, 1234, 1306, 1307, 1308, 1309, 1384, 1385, 1386]
            edgeptsx= [data.GetPoints().GetPoint(i)[0] for i in edgeidxs]            
            edgeptsy = [data.GetPoints().GetPoint(i)[1] for i in edgeidxs]             
            width = (np.max(edgeptsx) -np.min(edgeptsx))
            hieght = (np.max(edgeptsy) - np.min(edgeptsy))
            AR = hieght/width

            ARData.append([str(gg), str(ff), str(qq), str(AR)])

            Delete(activeSource)
            del activeSource

print(ARData)

f = open(pathexp+filename, "w")
for i in range(0, len(ARData)):
    f.write(', '.join(ARData[i])+'\n')
