# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
import os 
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

SizeData = [["g","p","q","pore_area"]]
AofRect = 96


fs = [0.05]
qs = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0, 1.05, 1.1]
gs = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]
C = 2
pathp = r'/home/gabriel/Desktop/ProjectFiles/ColloidalMembranes/VTKMega/Round9'
pathexp = '/home/gabriel/Desktop/ProjectFiles/ColloidalMembranes/CodeMega/DataAnalysis/Round9'
filename = r"/PoreSizeData.txt"
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
            DataSet = LegacyVTKReader(registrationName='SinglePore.vtk*', FileNames=[pathc+f'/SinglePoreg{gg}p{ff}q{qq}_{maxiter}.vtk'])

            # create a new 'Integrate Variables'
            integrateVariables1 = IntegrateVariables(registrationName='IntegrateVariables1', Input=DataSet)

            # Create a new 'SpreadSheet View'
            spreadSheetView1 = CreateView('SpreadSheetView')
            spreadSheetView1.ColumnToSort = ''
            spreadSheetView1.BlockSize = 1024

            # show data in view
            integrateVariables1Display = Show(integrateVariables1, spreadSheetView1, 'SpreadSheetRepresentation')

        
            # Properties modified on integrateVariables1Display
            integrateVariables1Display.Assembly = ''


            # update the view to ensure updated data information
            spreadSheetView1.Update()

            # Properties modified on spreadSheetView1
            spreadSheetView1.FieldAssociation = 'Cell Data'

            # set active source
            SetActiveSource(integrateVariables1)

            # create a new 'Pass Arrays'
            passArrays1 = PassArrays(Input=integrateVariables1)
            passArrays1.CellDataArrays = ['Area']
            ss_data = paraview.servermanager.Fetch(passArrays1)    
            Area1 = ss_data.GetCellData().GetArray('Area').GetValue(0)

            # set active source
            SetActiveSource(integrateVariables1)

            # get animation scene
            animationScene1 = GetAnimationScene()

            animationScene1.GoToLast()

            # create a new 'Pass Arrays'
            passArrays1 = PassArrays(Input=integrateVariables1)
            passArrays1.CellDataArrays = ['Area']
            ss_data = paraview.servermanager.Fetch(passArrays1)  
            Area2 = ss_data.GetCellData().GetArray('Area').GetValue(0)

            SizeData.append([str(gg), str(ff), str(qq), str(AofRect - Area2)])

            animationScene1.GoToFirst()

            # destroy DataSet
            Delete(spreadSheetView1)
            del spreadSheetView1

            # destroy integrateVariables1
            Delete(integrateVariables1)
            del integrateVariables1

            Delete(passArrays1)
            del passArrays1

            Delete(DataSet)
            del DataSet

print(SizeData)

f = open(pathexp+filename, "w")
for i in range(0, len(SizeData)):
    f.write(', '.join(SizeData[i])+'\n')
