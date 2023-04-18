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
#MeshAtts.pointSize = 0.05
MeshAtts.opaqueColor = (51, 51, 51, 255)
MeshAtts.smoothingLevel = MeshAtts.NONE  # NONE, Fast, High
#MeshAtts.pointSizeVarEnabled = 0
MeshAtts.pointSizeVar = "default"
MeshAtts.pointType = MeshAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
#MeshAtts.showInternal = 0
#MeshAtts.pointSizePixels = 2
#MeshAtts.opacity = 1
v.SetDefaultPlotOptions(MeshAtts)
'''
MeshAtts = v.MeshAttributes()
MeshAtts.legendFlag = 1
MeshAtts.lineWidth = 0
MeshAtts.meshColor = (51, 51, 51, 255)
MeshAtts.meshColorSource = MeshAtts.MeshCustom  # Foreground, MeshCustom, MeshRandom
MeshAtts.opaqueColorSource = MeshAtts.OpaqueCustom  # Background, OpaqueCustom, OpaqueRandom
MeshAtts.opaqueMode = MeshAtts.Auto  # Auto, On, Off
MeshAtts.pointSize = 0.05
MeshAtts.opaqueColor = (51, 51, 51, 255)
MeshAtts.smoothingLevel = MeshAtts.NONE  # NONE, Fast, High
MeshAtts.pointSizeVarEnabled = 0
MeshAtts.pointSizeVar = "default"
MeshAtts.pointType = MeshAtts.Point  # Box, Axis, IcosahedronLightAttributes, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
MeshAtts.showInternal = 0
MeshAtts.pointSizePixels = 2
MeshAtts.opacity = 1
'''
v.SetPlotOptions(MeshAtts)
RenderingAtts = v.RenderingAttributes()
RenderingAtts.antialiasing = 0
#RenderingAtts.orderComposite = 1
#RenderingAtts.depthCompositeThreads = 2
#RenderingAtts.depthCompositeBlocking = 65536
#RenderingAtts.alphaCompositeThreads = 2
#RenderingAtts.alphaCompositeBlocking = 65536
#RenderingAtts.depthPeeling = 0
#RenderingAtts.occlusionRatio = 0
#RenderingAtts.numberOfPeels = 16
#RenderingAtts.multiresolutionMode = 0
#RenderingAtts.multiresolutionCellSize = 0.002
#RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
#RenderingAtts.notifyForEachRender = 0
#RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
#RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 1
RenderingAtts.specularCoeff = 0.98
RenderingAtts.specularPower = 2.8
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
#RenderingAtts.doDepthCueing = 0
#RenderingAtts.depthCueingAutomatic = 1
#RenderingAtts.startCuePoint = (-10, 0, 0)
#RenderingAtts.endCuePoint = (10, 0, 0)
#RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
#RenderingAtts.colorTexturingFlag = 1
#RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
#RenderingAtts.compactDomainsAutoThreshold = 256
#RenderingAtts.osprayRendering = 0
#RenderingAtts.ospraySPP = 1
#RenderingAtts.osprayAO = 0
#RenderingAtts.osprayShadows = 0
v.SetRenderingAttributes(RenderingAtts)
light0 = v.LightAttributes()
light0.enabledFlag = 1
light0.type = light0.Object  # Ambient, Object, Camera
light0.direction = (-0.693, -0.638, -0.335)
light0.color = (255, 255, 255, 255)
light0.brightness = 1
v.SetLight(0, light0)
#light1 = v.LightAttributes()
#light1.enabledFlag = 0
#light1.type = light1.Camera  # Ambient, Object, Camera
#light1.direction = (0, 0, -1)
#light1.color = (255, 255, 255, 255)
#light1.brightness = 1
#v.SetLight(1, light1)
