# trace generated using paraview version 5.13.0-484-g690fb3847e
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'

import numpy as np
def lengthoverpoints(ptlst):
    pts = ptlst
    tdis = 0
    mid = 0
    hide = 0
    for h in range(0,len(pts)):
        iid = mid        
        mid = (iid+1) % len(pts)
        
        while mid==hide or mid==iid: mid = (mid+1) % len(pts) 
        md = np.sqrt((pts[iid][0] - pts[mid][0])**2 + (pts[iid][1] - pts[mid][1])**2)  
        for i in range(0,len(pts)): 
            if i==iid or i==hide or i==mid: continue
            dis = np.sqrt((pts[iid][0] - pts[i][0])**2 + (pts[iid][1] - pts[i][1])**2)     
            if dis < md:
                md = dis
                mid = i
#        print(md)
#        print(mid)              
        tdis += md
#        print(tdis)
        hide = iid
    return tdis

        
    

paraview.simple._DisableFirstRenderCameraReset()
qstar = 1
C = 2
gstar = 1
# find source
activeSource = GetActiveSource()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

data = paraview.servermanager.Fetch(activeSource)  
#  
#N = data.GetPoints().GetNumberOfPoints()
#allpoints = [[data.GetPoints().GetPoint(i)[0],data.GetPoints().GetPoint(i)[1]] for i in range(0, N)]
#
# create a new 'Extract Cells By Region'
#extractCellsByRegion1 = ExtractCellsByRegion(registrationName='ExtractCellsByRegion1', Input=activeSource)
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

edgeidxs =  [590, 591, 592, 593, 594, 668, 669, 741, 742, 812, 813, 882, 883, 952, 953, 1022, 1023, 1092, 1093, 1162, 1163, 1233, 1234, 1306, 1307, 1308, 1309, 1384, 1385, 1386]
edgepoints = [[data.GetPoints().GetPoint(i)[0],data.GetPoints().GetPoint(i)[1]] for i in edgeidxs]


print(lengthoverpoints(edgepoints))
    

