#### import the simple module from the paraview
from paraview.simple import *
import os
import numpy as np
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()
C = 2
pstar = 0.05
qs = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
ss = np.arange(0.025, 1.025, 0.025)
g = 0.7
pathp = '/home/gabriel/Repositories/colloidal_membranes_v2/vtk_results/Round9_byellipse'
pathexp = '/home/gabriel/Repositories/colloidal_membranes_v2/data_viz/extracted_data/single_pore_ellipse'

EnergyData = [["s", "q","Energy"]]

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

for i,s in enumerate(ss):
    for q in qs:
        pathc = pathp+f"/q={q} g={0.3}"
        ldocs = os.listdir(pathc)
        maxiter = 0
        for st in ldocs:
            if "_" in st:
                st = st.split("_")[1]
                iter = int(st.replace(".vtk", ""))
                if iter > maxiter:
                    maxiter = iter
        ss=round(s,3)
        if q==0.0 or q==1.0 or q==2.0: qq = round(q)
        else: qq=q

        # create a new 'Legacy VTK Reader'
        activeSource = LegacyVTKReader(registrationName='SinglePore.vtk*', FileNames=[pathc+f'/SinglePoreq={qq}s={ss:.3f}.vtk'])

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

        
        if q==0.3:
            porebndlens = [0.281513, 0.563026, 0.844539, 1.126053, 1.407566, 1.689079, 1.970592, 2.252105, 2.533618, 2.815132, 3.096645, 3.378158, 3.659671, 3.941184, 4.222697, 4.504211, 4.785724, 5.067237, 5.34875, 5.630263, 5.911776, 6.19329, 6.474803, 6.756316, 7.037829, 7.319342, 7.600855, 7.882369, 8.163882, 8.445395, 8.726908, 9.008421, 9.289934, 9.571448, 9.852961, 10.134474, 10.415987, 10.6975, 10.979013, 11.260527]
        elif q==0.4:
            porebndlens = [0.277931, 0.555863, 0.833794, 1.111726, 1.389657, 1.667589, 1.94552, 2.223451, 2.501383, 2.779314, 3.057246, 3.335177, 3.613109, 3.89104, 4.168971, 4.446903, 4.724834, 5.002766, 5.280697, 5.558629, 5.83656, 6.114491, 6.392423, 6.670354, 6.948286, 7.226217, 7.504149, 7.78208, 8.060011, 8.337943, 8.615874, 8.893806, 9.171737, 9.449669, 9.7276, 10.005531, 10.283463, 10.561394, 10.839326, 11.117257]
        elif q==0.5:
            porebndlens = [0.271767, 0.543535, 0.815302, 1.08707, 1.358837, 1.630605, 1.902372, 2.17414, 2.445907, 2.717675, 2.989442, 3.26121, 3.532977, 3.804745, 4.076512, 4.34828, 4.620047, 4.891814, 5.163582, 5.435349, 5.707117, 5.978884, 6.250652, 6.522419, 6.794187, 7.065954, 7.337722, 7.609489, 7.881257, 8.153024, 8.424792, 8.696559, 8.968327, 9.240094, 9.511861, 9.783629, 10.055396, 10.327164, 10.598931, 10.870699]
        elif q==0.6:
            porebndlens = [0.269349, 0.538698, 0.808047, 1.077396, 1.346745, 1.616094, 1.885443, 2.154792, 2.424141, 2.69349, 2.962839, 3.232188, 3.501538, 3.770887, 4.040236, 4.309585, 4.578934, 4.848283, 5.117632, 5.386981, 5.65633, 5.925679, 6.195028, 6.464377, 6.733726, 7.003075, 7.272424, 7.541773, 7.811122, 8.080471, 8.34982, 8.619169, 8.888518, 9.157867, 9.427216, 9.696565, 9.965914, 10.235263, 10.504613, 10.773962]
        elif q==0.7:
            porebndlens = [0.323603, 0.647206, 0.970809, 1.294412, 1.618015, 1.941619, 2.265222, 2.588825, 2.912428, 3.236031, 3.559634, 3.883237, 4.20684, 4.530443, 4.854046, 5.177649, 5.501252, 5.824856, 6.148459, 6.472062, 6.795665, 7.119268, 7.442871, 7.766474, 8.090077, 8.41368, 8.737283, 9.060886, 9.384489, 9.708093, 10.031696, 10.355299, 10.678902, 11.002505, 11.326108, 11.649711, 11.973314, 12.296917, 12.62052, 12.944123]
        elif q==0.8:
            porebndlens = [0.355201, 0.710402, 1.065603, 1.420805, 1.776006, 2.131207, 2.486408, 2.841609, 3.19681, 3.552011, 3.907212, 4.262414, 4.617615, 4.972816, 5.328017, 5.683218, 6.038419, 6.39362, 6.748821, 7.104023, 7.459224, 7.814425, 8.169626, 8.524827, 8.880028, 9.235229, 9.59043, 9.945632, 10.300833, 10.656034, 11.011235, 11.366436, 11.721637, 12.076838, 12.432039, 12.787241, 13.142442, 13.497643, 13.852844, 14.208045]


        EdgeEnergy = g*porebndlens[i]
            

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
        calculator8.Function = f'1/2*(splay + (ny*nyx - nz*nxz)^2 + (nz*nzy - nx*nyx)^2 + (nx*nxz - ny*nzy)^2 + (nx*nzy + ny*nxz + nz*nyx - {q})^2) + 1/2*{C}*(1-nz^2)'

        # create a new 'Pass Arrays'
        passArrays2 = PassArrays(registrationName='PassArrays2', Input=calculator8)

        # Properties modified on passArrays1
        passArrays2.CellDataArrays = ['TotalEnergy']

        # create a new 'Integrate Variables'
        integrateVariables1 = IntegrateVariables(registrationName='IntegrateVariables1', Input=passArrays2)


        ss_data = paraview.servermanager.Fetch(integrateVariables1)    
        NemEnergy = ss_data.GetCellData().GetArray('TotalEnergy').GetValue(0)
        Area = ss_data.GetCellData().GetArray('Area').GetValue(0)
        Pressure = Area*pstar
            
        EnergyData.append([str(ss), str(qq), str(NemEnergy + Pressure + EdgeEnergy)])

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

        Delete(activeSource)
        del activeSource


f = open(pathexp+f"/EnergyDataEllipseg={g}.txt", "w")
for i in range(0, len(EnergyData)):
    f.write(', '.join(EnergyData[i])+'\n')









