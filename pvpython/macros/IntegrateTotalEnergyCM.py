# trace generated using paraview version 5.13.0-484-g690fb3847e
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()
qstar = 1
C = 2
gstar = 1
pstar = 0.05

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


# find source

activeSource = GetActiveSource()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

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

edgeidxs = [590, 591, 592, 593, 594, 668, 669, 741, 742, 812, 813, 882, 883, 952, 953, 1022, 1023, 1092, 1093, 1162, 1163, 1233, 1234, 1306, 1307, 1308, 1309, 1384, 1385, 1386]
edgepoints = [[data.GetPoints().GetPoint(i)[0],data.GetPoints().GetPoint(i)[1]] for i in edgeidxs]


EdgeEnergy = gstar*lengthoverpoints(edgepoints)
    

#-----------------------------------------------Nematic and Tilt Energy-----------------------------------------------#

# create a new 'Extract Cells By Type'
extractCellsByType2 = ExtractCellsByType(registrationName='ExtractCellsByType2', Input=activeSource)

# Properties modified on extractCellsByType2
extractCellsByType2.CellTypes = ['Bezier Curve', 'Bezier Hexahedron', 'Bezier Pyramid', 'Bezier Quadrilateral', 'Bezier Tetrahedron', 'Bezier Triangle', 'Bezier Wedge', 'Bi-Quadratic Quadratic Hexahedron', 'Bi-Quadratic Quadratic Wedge', 'Bi-Quadratic Quadrilateral', 'Bi-Quadratic Triangle', 'Cubic Line', 'Hexagonal Prism', 'Hexahedron', 'Lagrange Curve', 'Lagrange Hexahedron', 'Lagrange Pyramid', 'Lagrange Quadrilateral', 'Lagrange Tetrahedron', 'Lagrange Triangle', 'Lagrange Wedge', 'Pentagonal Prism', 'Pixel', 'Polygon', 'Polyhedron', 'Polyline', 'Polyvertex', 'Pyramid', 'Quadratic Edge', 'Quadratic Hexahedron', 'Quadratic Linear Quadrilateral', 'Quadratic Linear Wedge', 'Quadratic Polygon', 'Quadratic Pyramid', 'Quadratic Quadrilateral', 'Quadratic Tetrahedron', 'Quadratic Triangle', 'Quadratic Wedge', 'Quadrilateral', 'Tetrahedron', 'Tri-Quadratic Hexahedron', 'Tri-Quadratic Pyramid', 'Triangle', 'Triangle Strip', 'Vertex', 'Voxel', 'Wedge']

# set active source
SetActiveSource(extractCellsByType2)

# create a new 'Compute Derivatives'
computeDerivatives1 = ComputeDerivatives(registrationName='ComputeDerivatives1', Input=extractCellsByType2)

# Properties modified on computeDerivatives2
computeDerivatives1.Scalars = ['POINTS', '']
computeDerivatives1.Vectors = ['POINTS', 'vectors']

# create a new 'Point Data to Cell Data'
pointDatatoCellData1 = PointDatatoCellData(registrationName='PointDatatoCellData1', Input=computeDerivatives1)

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=pointDatatoCellData1)
calculator1.AttributeType = 'Cell Data'

# Properties modified on calculator1
calculator1.ResultArrayName = 'nx'
calculator1.Function = 'vectors_X'

# create a new 'Calculator'
calculator2 = Calculator(registrationName='Calculator2', Input=calculator1)
calculator2.AttributeType = 'Cell Data'

# Properties modified on calculator2
calculator2.ResultArrayName = 'ny'
calculator2.Function = 'vectors_Y'

# create a new 'Calculator'
calculator3 = Calculator(registrationName='Calculator3', Input=calculator2)
calculator3.AttributeType = 'Cell Data'

# Properties modified on calculator3
calculator3.ResultArrayName = 'nz'
calculator3.Function = 'vectors_Z'

# create a new 'Calculator'
calculator4 = Calculator(registrationName='Calculator4', Input=calculator3)
calculator4.AttributeType = 'Cell Data'

# Properties modified on calculator4
calculator4.ResultArrayName = 'nzy'
calculator4.Function = '"VectorGradient_7"-"VectorGradient_5"'

# create a new 'Calculator'
calculator5 = Calculator(registrationName='Calculator5', Input=calculator4)
calculator5.AttributeType = 'Cell Data'

# Properties modified on calculator5
calculator5.ResultArrayName = 'nxz'
calculator5.Function = '"VectorGradient_3"-"VectorGradient_6"'


# create a new 'Calculator'
calculator6 = Calculator(registrationName='Calculator6', Input=calculator5)
calculator6.AttributeType = 'Cell Data'

# Properties modified on calculator6
calculator6.ResultArrayName = 'nyx'
calculator6.Function = '"VectorGradient_3" - "VectorGradient_1"'


# create a new 'Calculator'
calculator7 = Calculator(registrationName='Calculator7', Input=calculator6)
calculator7.AttributeType = 'Cell Data'

# Properties modified on calculator7
calculator7.ResultArrayName = 'splay'
calculator7.Function = '("VectorGradient_0"+"VectorGradient_4"+"VectorGradient_8")^2'

# create a new 'Pass Arrays'
passArrays1 = PassArrays(registrationName='PassArrays1', Input=calculator7)

# Properties modified on passArrays2
passArrays1.CellDataArrays = ['nx', 'nxz', 'ny', 'nyx', 'nz', 'nzy', 'splay']

# create a new 'Calculator'
calculator8 = Calculator(registrationName='Calculator8', Input=passArrays1)
calculator8.AttributeType = 'Cell Data'

# Properties modified on calculator8
calculator8.ResultArrayName = 'TotalEnergy'
calculator8.Function = f'1/2*(splay + (ny*nyx - nz*nxz)^2 + (nz*nzy - nx*nyx)^2 + (nx*nxz - ny*nzy)^2 + (nx*nzy + ny*nxz + nz*nyx - {qstar})^2) + 1/2*{C}*(1-nz^2)'

twist = Calculator(registrationName='twist', Input=calculator8)
twist.AttributeType = 'Cell Data'

# Properties modified on calculator8
twist.ResultArrayName = 'twist'
twist.Function = f'1/2*((nx*nzy + ny*nxz + nz*nyx - {qstar})^2)'

tilt = Calculator(registrationName='tilt', Input=twist)
tilt.AttributeType = 'Cell Data'

# Properties modified on calculator8
tilt.ResultArrayName = 'tilt'
tilt.Function = f'1/2*{C}*(1-nz^2)'

splay = Calculator(registrationName='splay', Input=tilt)
splay.AttributeType = 'Cell Data'

# Properties modified on calculator8
splay.ResultArrayName = 'splay'
splay.Function = f'1/2*splay'

bend = Calculator(registrationName='bend', Input=splay)
bend.AttributeType = 'Cell Data'

# Properties modified on calculator8
bend.ResultArrayName = 'bend'
bend.Function = f'1/2*((ny*nyx - nz*nxz)^2 + (nz*nzy - nx*nyx)^2 + (nx*nxz - ny*nzy)^2)'


# create a new 'Pass Arrays'
passArrays2 = PassArrays(registrationName='PassArrays2', Input=bend)

# Properties modified on passArrays1
passArrays2.CellDataArrays = ['TotalEnergy', 'twist', 'splay', 'bend', 'tilt']

# create a new 'Integrate Variables'
integrateVariables1 = IntegrateVariables(registrationName='IntegrateVariables1', Input=passArrays2)


ss_data = paraview.servermanager.Fetch(integrateVariables1)    
NemEnergy = ss_data.GetCellData().GetArray('TotalEnergy').GetValue(0)
twistenergy = ss_data.GetCellData().GetArray('twist').GetValue(0)
splayenergy = ss_data.GetCellData().GetArray('splay').GetValue(0)
bendenergy = ss_data.GetCellData().GetArray('bend').GetValue(0)
tiltenergy = ss_data.GetCellData().GetArray('tilt').GetValue(0)
Area = ss_data.GetCellData().GetArray('Area').GetValue(0)
Pressure = Area*pstar

Delete(extractCellsByType2)
del extractCellsByType2

Delete(computeDerivatives1)
del computeDerivatives1

Delete(pointDatatoCellData1)
del pointDatatoCellData1

Delete(calculator1)
del calculator1

Delete(calculator2)
del calculator2

Delete(calculator3)
del calculator3

Delete(calculator4)
del calculator4

Delete(calculator5)
del calculator5

Delete(calculator6)
del calculator6

Delete(calculator7)
del calculator7

Delete(passArrays1)
del passArrays1

Delete(calculator8)
del calculator8

Delete(passArrays2)
del passArrays2

Delete(integrateVariables1)
del integrateVariables1

Delete(twist)
del twist

Delete(splay)
del splay

Delete(bend)
del bend

Delete(tilt)
del tilt
print(f"Energy: {NemEnergy + Pressure + EdgeEnergy} \n Pressure Term: {Pressure} \n Nematic + Tilt Term: {NemEnergy} \n Edge Tension Term: {EdgeEnergy} \n Twist Term: {twistenergy} \n Splay Term: {splayenergy} \n Bend Term: {bendenergy} \n Tilt Term: {tiltenergy}")

