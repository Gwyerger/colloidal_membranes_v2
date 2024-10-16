#### import the simple module from the paraview
from paraview.simple import *
import os
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()
C = 2
pstar = 0.05
qs = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 1.05, 1.1]

pathp = r'/home/gabriel/Desktop/ProjectFiles/ColloidalMembranes/VTKMega/PiWall'
pathexp = '/home/gabriel/Desktop/ProjectFiles/ColloidalMembranes/CodeMega/DataAnalysis/PiWall'

EnergyData = [["p","q","Energy"]]

for q in qs:
    pathc = pathp+f"/q={q}"
    ldocs = os.listdir(pathc)
    maxiter = 0
    for st in ldocs:
        if "_" in st:
            st = st.split("_")[1]
            iter = int(st.replace(".vtk", ""))
            if iter > maxiter:
                maxiter = iter

    if q==0.0 or q==1.0 or q==2.0: qq = round(q)
    else: qq=q

    # create a new 'Legacy VTK Reader'
    activeSource = LegacyVTKReader(registrationName='PiWall.vtk*', FileNames=[pathc+f'/PiWallq{qq}_{maxiter}.vtk'])


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
        
    EnergyData.append([str(pstar), str(q), str(NemEnergy + Pressure)])

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


f = open(pathexp+"/EnergyData2.txt", "w")
for i in range(0, len(EnergyData)):
    f.write(', '.join(EnergyData[i])+'\n')









