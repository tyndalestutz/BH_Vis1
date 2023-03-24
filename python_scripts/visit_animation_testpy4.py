import sys
sys.path.append("/usr/local/3.3.1/linux-x86_64/lib/site-packages") 
import visit
visit.Launch()
import visit
import pandas as pd
import csv
v = visit

visit.OpenDatabase("localhost:/home/guest/Documents/VisIt/tutorial1/tenthr_sphere_16pts.obj", 0) # for smaller use tenthr_sphere_16pts.obj
#v.AddPlot("Mesh", "OBJMesh", 1, 1)
#v.DrawPlots()

# Logging for SetAnnotationObjectOptions is not implemented yet.
AnnotationAtts = v.AnnotationAttributes()
AnnotationAtts.axes3D.visible = 0
AnnotationAtts.axes3D.bboxFlag = 1 
AnnotationAtts.axes3D.setBBoxLocation = 1
AnnotationAtts.axes3D.bboxLocation = (-10, 10, -10, 10, -1.5, 1.5)
v.SetAnnotationAttributes(AnnotationAtts)

# Begin spontaneous state
View3DAtts = v.View3DAttributes()
View3DAtts.viewNormal = (0, 0, 1)
View3DAtts.focus = (0, 0, 0)
View3DAtts.viewUp = (0, 1, 0)
#View3DAtts.viewAngle = 30
#View3DAtts.parallelScale = 14.2215
View3DAtts.nearPlane = -28.4429
View3DAtts.farPlane = 28.4429
#View3DAtts.imagePan = (0, 0)
#View3DAtts.imageZoom = 1
#View3DAtts.perspective = 1
#View3DAtts.eyeAngle = 2
View3DAtts.windowValid = 1
v.SetView3D(View3DAtts)

v.AddPlot("Mesh", "OBJMesh", 1, 0)
v.AddOperator("Transform", 0)


def set_coords(x1, y1):
    #v.DeleteAllPlots()
    TransformAtts = v.TransformAttributes()
    TransformAtts.doTranslate = 1
    TransformAtts.translateX = x1
    TransformAtts.translateY = y1
    TransformAtts.translateZ = 0
    TransformAtts.vectorTransformMethod = TransformAtts.AsDirection  # NONE, AsPoint, AsDisplacement, AsDirection
    TransformAtts.transformVectors = 1
    v.SetOperatorOptions(TransformAtts, 0, 0)
    
    #v.SaveWindow()

#filename = 'synthetic_data_BH1xyOnly_x10.csv'
filename = '/home/guest/Documents/Tyndale/vscode/database/synthetic_data_BH1xyOnly_scaled_x10.csv'

with open(filename, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # skip the header row
    column1, column2, column3 = [], [], []
    for row in reader:
        t = float(row[0])
        x1 = float(row[1])
        y1 = float(row[2])
        #x2 = float(row[3])
        #y2 = float(row[4])
        set_coords(x1, y1)
        #set_coords(x2, y2)
        v.DrawPlots()
        #set_conords(x2, y2)
    done = False
    while True:
        set_coords(0, 0)
        
