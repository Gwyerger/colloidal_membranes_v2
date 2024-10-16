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
# find source
activeSource = GetActiveSource()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# create a new 'Extract Cells By Type'
extractCellsByType2 = ExtractCellsByType(registrationName='ExtractCellsByType2', Input=activeSource)

# Properties modified on extractCellsByType2
extractCellsByType2.CellTypes = ['Bezier Curve', 'Bezier Hexahedron', 'Bezier Pyramid', 'Bezier Quadrilateral', 'Bezier Tetrahedron', 'Bezier Triangle', 'Bezier Wedge', 'Bi-Quadratic Quadratic Hexahedron', 'Bi-Quadratic Quadratic Wedge', 'Bi-Quadratic Quadrilateral', 'Bi-Quadratic Triangle', 'Cubic Line', 'Hexagonal Prism', 'Hexahedron', 'Lagrange Curve', 'Lagrange Hexahedron', 'Lagrange Pyramid', 'Lagrange Quadrilateral', 'Lagrange Tetrahedron', 'Lagrange Triangle', 'Lagrange Wedge', 'Pentagonal Prism', 'Pixel', 'Polygon', 'Polyhedron', 'Polyline', 'Polyvertex', 'Pyramid', 'Quadratic Edge', 'Quadratic Hexahedron', 'Quadratic Linear Quadrilateral', 'Quadratic Linear Wedge', 'Quadratic Polygon', 'Quadratic Pyramid', 'Quadratic Quadrilateral', 'Quadratic Tetrahedron', 'Quadratic Triangle', 'Quadratic Wedge', 'Quadrilateral', 'Tetrahedron', 'Tri-Quadratic Hexahedron', 'Tri-Quadratic Pyramid', 'Triangle', 'Triangle Strip', 'Vertex', 'Voxel', 'Wedge']

# set active source
SetActiveSource(extractCellsByType2)

# create a new 'Compute Derivatives'
computeDerivatives2 = ComputeDerivatives(registrationName='ComputeDerivatives2', Input=extractCellsByType2)

# Properties modified on computeDerivatives2
computeDerivatives2.Scalars = ['POINTS', '']
computeDerivatives2.Vectors = ['POINTS', 'vectors']

# create a new 'Point Data to Cell Data'
pointDatatoCellData2 = PointDatatoCellData(registrationName='PointDatatoCellData2', Input=computeDerivatives2)

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=pointDatatoCellData2)
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
passArrays2 = PassArrays(registrationName='PassArrays2', Input=calculator7)

# Properties modified on passArrays2
passArrays2.CellDataArrays = ['nx', 'nxz', 'ny', 'nyx', 'nz', 'nzy', 'splay']

# create a new 'Calculator'
calculator8 = Calculator(registrationName='Calculator8', Input=passArrays2)
calculator8.AttributeType = 'Cell Data'

# Properties modified on calculator8
calculator8.ResultArrayName = 'TotalEnergy'
calculator8.Function = f'1/2*(splay + (ny*nyx - nz*nxz)^2 + (nz*nzy - nx*nyx)^2 + (nx*nxz - ny*nzy)^2 + (nx*nzy + ny*nxz + nz*nyx - {qstar})^2) + 1/2*{C}*(1-nz^2)'

# show data in view
calculator8Display = Show(calculator8, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
calculator8Display.Representation = 'Surface'

# show color bar/color legend
calculator8Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'TotalEnergy'
totalEnergyLUT = GetColorTransferFunction('TotalEnergy')

# get opacity transfer function/opacity map for 'TotalEnergy'
totalEnergyPWF = GetOpacityTransferFunction('TotalEnergy')

# get 2D transfer function for 'TotalEnergy'
totalEnergyTF2D = GetTransferFunction2D('TotalEnergy')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
totalEnergyLUT.ApplyPreset('Viridis (matplotlib)', True)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(696, 768)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [0.00017499923706054688, 0.0001201629638671875, 42.37458790892597]
renderView1.CameraFocalPoint = [0.00017499923706054688, 0.0001201629638671875, 8.222149090048037e-13]
renderView1.CameraParallelScale = 11.0335928005867


##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://www.paraview.org/paraview-docs/latest/python/paraview.simple.html
##--------------------------------------------
