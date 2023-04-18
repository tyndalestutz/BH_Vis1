import sys
sys.path.append("/usr/local/3.3.1/linux-x86_64/lib/site-packages") 
import visit
visit.Launch()
import visit
v = visit

v.OpenDatabase("localhost:/home/guest/Documents/Tyndale/vscode/database/iscos_sphere_sub8.obj", 0)
v.AddPlot("Pseudocolor", "mesh_quality/warpage", 1, 1)
v.DrawPlots()

# This is the minimum required arguments in order to render no annotations
AnnotationAtts = v.AnnotationAttributes()
AnnotationAtts.axes2D.visible = 0
AnnotationAtts.axes3D.visible = 0
AnnotationAtts.axes3D.triadFlag = 0
AnnotationAtts.axes3D.bboxFlag = 0
AnnotationAtts.axes3D.xAxis.grid = 0
AnnotationAtts.axes3D.yAxis.grid = 0
AnnotationAtts.axes3D.zAxis.grid = 0
AnnotationAtts.axes3D.triadLineWidth = 0
AnnotationAtts.userInfoFlag = 0
AnnotationAtts.databaseInfoFlag = 0
AnnotationAtts.legendInfoFlag = 0
AnnotationAtts.axesArray.lineWidth = 0
AnnotationAtts.axesArray.axes.grid = 0
v.SetAnnotationAttributes(AnnotationAtts)


RenderingAtts = v.RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes
v.SetRenderingAttributes(RenderingAtts)


light = v.LightAttributes()
light.enabledFlag = 1
light.type = light.Object 
light.direction = (0.666, -0.666, -0.666)
v.SetLight(0, light)

#v.SaveWindow()