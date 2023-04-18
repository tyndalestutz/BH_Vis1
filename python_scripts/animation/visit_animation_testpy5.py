import sys, csv, time
sys.path.append("/usr/local/3.3.1/linux-x86_64/lib/site-packages") 
import visit
visit.Launch()
import visit
v = visit

#object 0: Black hole 1
#object 1: Black hole 2


database = "localhost:/home/guest/Documents/Tyndale/vscode/visit_run/halfr_sphere_16pts.obj"
bh_data = "/home/guest/Documents/Tyndale/vscode/visit_run/synthetic_data_BH_scaled_x10.csv"


visit.OpenDatabase(database, 0)

# Logging for SetAnnotationObjectOptions is not implemented yet.
AnnotationAtts = v.AnnotationAttributes()
AnnotationAtts.axes3D.visible = 0
AnnotationAtts.axes3D.bboxFlag = 1 
AnnotationAtts.axes3D.setBBoxLocation = 1
AnnotationAtts.axes3D.bboxLocation = (-7, 7, -7, 7, -1.5, 1.5)
v.SetAnnotationAttributes(AnnotationAtts)

# Begin spontaneous state
View3DAtts = v.View3DAttributes()
View3DAtts.viewNormal = (0, 0, 1)
View3DAtts.focus = (0, 0, 0)
View3DAtts.viewUp = (0, 1, 0)
View3DAtts.nearPlane = -28.4429
View3DAtts.farPlane = 28.4429
View3DAtts.windowValid = 1
v.SetView3D(View3DAtts)

v.AddPlot("Mesh", "OBJMesh")
v.AddOperator("Transform")
v.AddPlot("Mesh", "OBJMesh")
v.AddOperator("Transform")

def set_coords(objNum, x, y, z):
    v.SetActivePlots(objNum)
    trasnformAtts = v.TransformAttributes()
    trasnformAtts.doTranslate = 1
    trasnformAtts.translateX = x
    trasnformAtts.translateY = y
    trasnformAtts.translateZ = z
    v.SetOperatorOptions(trasnformAtts, 0, 0)

with open(bh_data, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # skip the header row
    v.DrawPlots()
    for row in reader:
        t = float(row[0])
        x1 = float(row[1])
        y1 = float(row[2])
        x2 = float(row[3])
        y2 = float(row[4])
        
        set_coords(0, x1, y1, 0)
        set_coords(1, x2, y2, 0)
    v.DrawPlots()
        
