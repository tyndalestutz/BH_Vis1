import sys
sys.path.append("/usr/local/3.3.1/linux-x86_64/lib/site-packages") 
import visit
visit.Launch()
import visit
import pandas as pd
import csv
v = visit

v.OpenDatabase("localhost:/home/guest/Documents/Tyndale/vscode/database/sphere_50pts.obj", 0)
v.AddPlot("Mesh", "OBJMesh", 1, 1)
v.DrawPlots()
MeshAtts = v.MeshAttributes()

MeshAtts.meshColor = (51, 51, 51, 255)
MeshAtts.meshColorSource = MeshAtts.MeshCustom  # Foreground, MeshCustom, MeshRandom
MeshAtts.opaqueColorSource = MeshAtts.OpaqueCustom  # Background, OpaqueCustom, OpaqueRandom
MeshAtts.opaqueMode = MeshAtts.Auto  # Auto, On, Off
MeshAtts.opaqueColor = (51, 51, 51, 255)
MeshAtts.smoothingLevel = MeshAtts.NONE  # NONE, Fast, High
MeshAtts.pointSizeVar = "default"
MeshAtts.pointType = MeshAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
v.SetDefaultPlotOptions(MeshAtts)
v.SetPlotOptions(MeshAtts)

RenderingAtts = v.RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.specularFlag = 1
RenderingAtts.specularCoeff = 0.98
RenderingAtts.specularPower = 2.8
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5

v.SetRenderingAttributes(RenderingAtts)
light0 = v.LightAttributes()
light0.enabledFlag = 1
light0.type = light0.Object  # Ambient, Object, Camera
light0.direction = (-0.693, -0.638, -0.335)
light0.color = (255, 255, 255, 255)
light0.brightness = 1
v.SetLight(0, light0)
