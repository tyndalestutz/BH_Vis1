import sys
sys.path.append("/usr/local/3.3.1/linux-x86_64/lib/site-packages") 
import visit
visit.Launch()
import visit
v = visit

visit.OpenDatabase("localhost:/home/guest/Documents/VisIt/tutorial1/tenthr_sphere_16pts.obj", 0)
v.AddPlot("Mesh", "OBJMesh", 1, 1)
v.DrawPlots()

AnnotationAtts = v.AnnotationAttributes()
AnnotationAtts.axes3D.bboxLocation = (-7, 7, -7, 7, -1, 1)

v.SetAnnotationAttributes(AnnotationAtts)

View3DAtts = v.View3DAttributes()
v.SetView3D(View3DAtts)

print(AnnotationAtts)