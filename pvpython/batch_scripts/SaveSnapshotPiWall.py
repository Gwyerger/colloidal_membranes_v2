# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
import os
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()




#gs = [0.1]#, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
#gs = [0.1, 0.2, 0.3]
fs = [0.05]
#qs = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
qs = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7]

pathp = r'/home/gabriel/Desktop/ProjectFiles/ColloidalMembranes/VTKMega/PiWall'
pathexp = '/home/gabriel/Desktop/ProjectFiles/ColloidalMembranes/CodeMega/DataAnalysis/PiWall/FinalSnapshot'

for f in fs:
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
        if f==0.0 or f==1.0 or f==2.0: ff = round(f)
        else: ff=f
        # create a new 'Legacy VTK Reader'
        DataSet = LegacyVTKReader(registrationName='PiWall.vtk*', FileNames=[pathc+f'/PiWallq{qq}_{maxiter}.vtk'])
        # create a new 'Extract Cells By Type'
        extractCellsByType1 = ExtractCellsByType(registrationName='ExtractCellsByType1', Input=DataSet)

        # Properties modified on extractCellsByType1
        extractCellsByType1.CellTypes = ['Bezier Curve', 'Bezier Hexahedron', 'Bezier Pyramid', 'Bezier Quadrilateral', 'Bezier Tetrahedron', 'Bezier Triangle', 'Bezier Wedge', 'Bi-Quadratic Quadratic Hexahedron', 'Bi-Quadratic Quadratic Wedge', 'Bi-Quadratic Quadrilateral', 'Bi-Quadratic Triangle', 'Cubic Line', 'Hexagonal Prism', 'Hexahedron', 'Lagrange Curve', 'Lagrange Hexahedron', 'Lagrange Pyramid', 'Lagrange Quadrilateral', 'Lagrange Tetrahedron', 'Lagrange Triangle', 'Lagrange Wedge', 'Pentagonal Prism', 'Pixel', 'Polygon', 'Polyhedron', 'Polyline', 'Polyvertex', 'Pyramid', 'Quadratic Edge', 'Quadratic Hexahedron', 'Quadratic Linear Quadrilateral', 'Quadratic Linear Wedge', 'Quadratic Polygon', 'Quadratic Pyramid', 'Quadratic Quadrilateral', 'Quadratic Tetrahedron', 'Quadratic Triangle', 'Quadratic Wedge', 'Quadrilateral', 'Tetrahedron', 'Tri-Quadratic Hexahedron', 'Tri-Quadratic Pyramid', 'Triangle', 'Triangle Strip', 'Vertex', 'Voxel', 'Wedge']

        # get active view
        renderView1 = GetActiveViewOrCreate('RenderView')

        # Properties modified on renderView1
        renderView1.UseColorPaletteForBackground = 0

        # Properties modified on renderView1
        renderView1.Background = [1.0, 1.0, 1.0]
        # show data in view
        DataSetDisplay = Show(extractCellsByType1, renderView1, 'UnstructuredGridRepresentation')
        # change representation type
        DataSetDisplay.SetRepresentationType('Surface With Edges')
        DataSetDisplay.EdgeColor = [0.0, 0.0, 0.0]
        DataSetDisplay.EdgeOpacity = 0.5
        # trace defaults for the display properties.

        DataSetDisplay.ColorArrayName = [None, '']
        DataSetDisplay.SelectTCoordArray = 'None'
        DataSetDisplay.SelectNormalArray = 'None'
        DataSetDisplay.SelectTangentArray = 'None'
        DataSetDisplay.OSPRayScaleArray = 'vectors'
        DataSetDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
        DataSetDisplay.SelectOrientationVectors = 'vectors'
        DataSetDisplay.ScaleFactor = 1.2000000000000002
        DataSetDisplay.SelectScaleArray = 'None'
        DataSetDisplay.GlyphType = 'Arrow'
        DataSetDisplay.GlyphTableIndexArray = 'None'
        DataSetDisplay.GaussianRadius = 0.06
        DataSetDisplay.SetScaleArray = ['POINTS', 'vectors']
        DataSetDisplay.ScaleTransferFunction = 'PiecewiseFunction'
        DataSetDisplay.OpacityArray = ['POINTS', 'vectors']
        DataSetDisplay.OpacityTransferFunction = 'PiecewiseFunction'
        DataSetDisplay.DataAxesGrid = 'GridAxesRepresentation'
        DataSetDisplay.PolarAxes = 'PolarAxesRepresentation'
        DataSetDisplay.ScalarOpacityUnitDistance = 0.731620427723986
        DataSetDisplay.OpacityArrayName = ['POINTS', 'vectors']
        DataSetDisplay.SelectInputVectors = ['POINTS', 'vectors']
        DataSetDisplay.WriteLog = ''

        # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
        DataSetDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

        # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
        DataSetDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

        # get layout
        layout1 = GetLayout()
        
        renderView1.OrientationAxesVisibility = 0

                    # set scalar coloring
        ColorBy(DataSetDisplay, ('POINTS', 'vectors', 'Y'))

        # rescale color and/or opacity maps used to include current data range
        DataSetDisplay.RescaleTransferFunctionToDataRange(True, False)

        # show color bar/color legend
        DataSetDisplay.SetScalarBarVisibility(renderView1, True)

        # get color transfer function/color map for 'vectors'
        vectorsLUT = GetColorTransferFunction('vectors')
        # Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
        vectorsLUT.ApplyPreset('Viridis (matplotlib)', True)
        # get opacity transfer function/opacity map for 'vectors'
        vectorsPWF = GetOpacityTransferFunction('vectors')

        # get 2D transfer function for 'vectors'
        vectorsTF2D = GetTransferFunction2D('vectors')

        # hide color bar/color legend
        DataSetDisplay.SetScalarBarVisibility(renderView1, False)

        SetActiveSource(DataSet)

        #Enter preview mode
        layout1.PreviewMode = [976, 325]

        # reset view to fit data
        renderView1.ResetCamera(True)

        # layout/tab size in pixels
        layout1.SetSize(976, 325)

        # current camera placement for renderView1
        renderView1.CameraPosition = [0.0, 0.0, 10]
        renderView1.CameraFocalPoint = [0.0, 0.0, -1.1208997055187075e-13]
        renderView1.CameraParallelScale = 2.8499205516635553
        renderView1.CameraParallelProjection = 1

        # save screenshot
        SaveScreenshot(pathexp+f"/PiWallq{qq}.png", renderView1, ImageResolution=[1952, 650])

        # destroy DataSet
        Delete(DataSet)
        del DataSet

        Delete(extractCellsByType1)
        del extractCellsByType1

        Delete(renderView1)
        del renderView1
