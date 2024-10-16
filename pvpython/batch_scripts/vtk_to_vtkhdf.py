from paraview.simple import *
import subprocess
import sys

path = input("input path: ")
basename = input("file name (head): ")
output = path+basename+".vtkhdf"

filenames = subprocess.check_output(['find', path, "-name", basename+"*" ], text=True)

filenames = sorted(filenames.split("\n"))
filenames.pop(0)
filenames = sorted(filenames, key=len)
print(filenames)

def __main__(inputpaths, outputpath):
    transient_data = LegacyVTKReader(registrationName='transient_data*', FileNames=inputpaths)
    SaveData(outputpath, proxy=transient_data, WriteAllTimeSteps=1)

__main__(filenames, output)
