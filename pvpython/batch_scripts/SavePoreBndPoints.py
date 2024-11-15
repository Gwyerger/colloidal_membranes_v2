#### import the simple module from the paraview
from paraview.simple import *
import os
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()
C = 2
pstar = 0.05
qs = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 1.05, 1.1]
gs = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]
pathp = r'/home/gabriel/Repositories/colloidal_membranes_v2/vtk_results/Round9'
pathexp = '/home/gabriel/Repositories/colloidal_membranes_v2/data_viz/extracted_data/single_pore_round_9/PoreBndPoints'


import numpy as np
for g in gs:
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

        # create a new 'Legacy VTK Reader'
        activeSource = LegacyVTKReader(registrationName='SinglePore.vtk*', FileNames=[pathc+f'/SinglePoreg{gg}p{pstar}q{qq}_{maxiter}.vtk'])

        #-----------------------------------------------Line Tension-----------------------------------------------#

        data = paraview.servermanager.Fetch(activeSource)  
          
        #N = data.GetPoints().GetNumberOfPoints()
        #allpoints = [[data.GetPoints().GetPoint(i)[0],data.GetPoints().GetPoint(i)[1]] for i in range(0, N)]
        #
        # create a new 'Extract Cells By Region'
        #extractCellsByRegion1 = ExtractCellsByRegion(registrationName='ExtractCellsByRegion1', Input=extractCellsByType1)
        #
        # Properties modified on extractCellsByRegion1
        #extractCellsByRegion1.IntersectWith = 'Sphere'
        #
        # Properties modified on extractCellsByRegion1.IntersectWith
        #extractCellsByRegion1.IntersectWith.Center = [0.0, 0.0, 0.0]
        #extractCellsByRegion1.IntersectWith.Radius = 1.2
        #
        #data = paraview.servermanager.Fetch(extractCellsByRegion1)    
        #Np = data.GetPoints().GetNumberOfPoints()
        #edgepoints = [[data.GetPoints().GetPoint(i)[0],data.GetPoints().GetPoint(i)[1]] for i in range(0, Np)]
        #edgeidxs = []
        #
        #for i in range(0,N):
        #    if allpoints[i] in edgepoints:
        #        edgeidxs.append(i)
        #
        #print(edgeidxs)
        
        Pts = [["id", "x", "y"]]
        edgeidxs = [590, 591, 592, 593, 594, 668, 669, 741, 742, 812, 813, 882, 883, 952, 953, 1022, 1023, 1092, 1093, 1162, 1163, 1233, 1234, 1306, 1307, 1308, 1309, 1384, 1385, 1386] 
        for i in range(0, len(edgeidxs)):
            edgepoints = [data.GetPoints().GetPoint(edgeidxs[i])[0],data.GetPoints().GetPoint(edgeidxs[i])[1]]
            Pts.append([str(edgeidxs[i]),str(edgepoints[0]),str(edgepoints[1])])
        

        f = open(pathexp+f"/EdgePointDataq={qq}g={gg}.txt", "w")
        for i in range(0, len(Pts)):
            f.write(', '.join(Pts[i])+'\n')


        Delete(activeSource)
        del activeSource










