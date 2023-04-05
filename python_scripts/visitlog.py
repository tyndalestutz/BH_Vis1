# Visit 3.3.1 log file
ScriptVersion = "3.3.1"
if ScriptVersion != Version():
    print "This script is for VisIt %s. It may not work with version %s" % (ScriptVersion, Version())
visit.ShowAllWindows()
visit.OpenDatabase("../database/mesh/iscos_halfr_sphere_sub8.obj", 0)
# The UpdateDBPluginInfo RPC is not supported in the VisIt module so it will not be logged.
visit.AnnotationAtts = visit.AnnotationAttributes()
AnnotationAtts.axes2D.visible = 0
AnnotationAtts.axes2D.autoSetTicks = 1
AnnotationAtts.axes2D.autoSetScaling = 1
AnnotationAtts.axes2D.lineWidth = 0
AnnotationAtts.axes2D.tickLocation = AnnotationAtts.axes2D.Outside  # Inside, Outside, Both
AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.BottomLeft  # Off, Bottom, Left, BottomLeft, All
AnnotationAtts.axes2D.xAxis.title.visible = 1
AnnotationAtts.axes2D.xAxis.title.font.font = AnnotationAtts.axes2D.xAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.title.font.scale = 1
AnnotationAtts.axes2D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.title.font.bold = 1
AnnotationAtts.axes2D.xAxis.title.font.italic = 1
AnnotationAtts.axes2D.xAxis.title.userTitle = 0
AnnotationAtts.axes2D.xAxis.title.userUnits = 0
AnnotationAtts.axes2D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes2D.xAxis.title.units = ""
AnnotationAtts.axes2D.xAxis.label.visible = 1
AnnotationAtts.axes2D.xAxis.label.font.font = AnnotationAtts.axes2D.xAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.xAxis.label.font.scale = 1
AnnotationAtts.axes2D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.xAxis.label.font.bold = 1
AnnotationAtts.axes2D.xAxis.label.font.italic = 1
AnnotationAtts.axes2D.xAxis.label.scaling = 0
AnnotationAtts.axes2D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.xAxis.grid = 0
AnnotationAtts.axes2D.yAxis.title.visible = 1
AnnotationAtts.axes2D.yAxis.title.font.font = AnnotationAtts.axes2D.yAxis.title.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.title.font.scale = 1
AnnotationAtts.axes2D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.title.font.bold = 1
AnnotationAtts.axes2D.yAxis.title.font.italic = 1
AnnotationAtts.axes2D.yAxis.title.userTitle = 0
AnnotationAtts.axes2D.yAxis.title.userUnits = 0
AnnotationAtts.axes2D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes2D.yAxis.title.units = ""
AnnotationAtts.axes2D.yAxis.label.visible = 1
AnnotationAtts.axes2D.yAxis.label.font.font = AnnotationAtts.axes2D.yAxis.label.font.Courier  # Arial, Courier, Times
AnnotationAtts.axes2D.yAxis.label.font.scale = 1
AnnotationAtts.axes2D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes2D.yAxis.label.font.bold = 1
AnnotationAtts.axes2D.yAxis.label.font.italic = 1
AnnotationAtts.axes2D.yAxis.label.scaling = 0
AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes2D.yAxis.grid = 0
AnnotationAtts.axes3D.visible = 0
AnnotationAtts.axes3D.autoSetTicks = 1
AnnotationAtts.axes3D.autoSetScaling = 1
AnnotationAtts.axes3D.lineWidth = 0
AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.ClosestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
AnnotationAtts.axes3D.triadFlag = 0
AnnotationAtts.axes3D.bboxFlag = 0
AnnotationAtts.axes3D.xAxis.title.visible = 1
AnnotationAtts.axes3D.xAxis.title.font.font = AnnotationAtts.axes3D.xAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.title.font.scale = 1
AnnotationAtts.axes3D.xAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.title.font.bold = 0
AnnotationAtts.axes3D.xAxis.title.font.italic = 0
AnnotationAtts.axes3D.xAxis.title.userTitle = 0
AnnotationAtts.axes3D.xAxis.title.userUnits = 0
AnnotationAtts.axes3D.xAxis.title.title = "X-Axis"
AnnotationAtts.axes3D.xAxis.title.units = ""
AnnotationAtts.axes3D.xAxis.label.visible = 1
AnnotationAtts.axes3D.xAxis.label.font.font = AnnotationAtts.axes3D.xAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.xAxis.label.font.scale = 1
AnnotationAtts.axes3D.xAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.xAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.xAxis.label.font.bold = 0
AnnotationAtts.axes3D.xAxis.label.font.italic = 0
AnnotationAtts.axes3D.xAxis.label.scaling = 0
AnnotationAtts.axes3D.xAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.xAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.xAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.xAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.xAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.xAxis.grid = 0
AnnotationAtts.axes3D.yAxis.title.visible = 1
AnnotationAtts.axes3D.yAxis.title.font.font = AnnotationAtts.axes3D.yAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.title.font.scale = 1
AnnotationAtts.axes3D.yAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.title.font.bold = 0
AnnotationAtts.axes3D.yAxis.title.font.italic = 0
AnnotationAtts.axes3D.yAxis.title.userTitle = 0
AnnotationAtts.axes3D.yAxis.title.userUnits = 0
AnnotationAtts.axes3D.yAxis.title.title = "Y-Axis"
AnnotationAtts.axes3D.yAxis.title.units = ""
AnnotationAtts.axes3D.yAxis.label.visible = 1
AnnotationAtts.axes3D.yAxis.label.font.font = AnnotationAtts.axes3D.yAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.yAxis.label.font.scale = 1
AnnotationAtts.axes3D.yAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.yAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.yAxis.label.font.bold = 0
AnnotationAtts.axes3D.yAxis.label.font.italic = 0
AnnotationAtts.axes3D.yAxis.label.scaling = 0
AnnotationAtts.axes3D.yAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.yAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.yAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.yAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.yAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.yAxis.grid = 0
AnnotationAtts.axes3D.zAxis.title.visible = 1
AnnotationAtts.axes3D.zAxis.title.font.font = AnnotationAtts.axes3D.zAxis.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.title.font.scale = 1
AnnotationAtts.axes3D.zAxis.title.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.title.font.bold = 0
AnnotationAtts.axes3D.zAxis.title.font.italic = 0
AnnotationAtts.axes3D.zAxis.title.userTitle = 0
AnnotationAtts.axes3D.zAxis.title.userUnits = 0
AnnotationAtts.axes3D.zAxis.title.title = "Z-Axis"
AnnotationAtts.axes3D.zAxis.title.units = ""
AnnotationAtts.axes3D.zAxis.label.visible = 1
AnnotationAtts.axes3D.zAxis.label.font.font = AnnotationAtts.axes3D.zAxis.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axes3D.zAxis.label.font.scale = 1
AnnotationAtts.axes3D.zAxis.label.font.useForegroundColor = 1
AnnotationAtts.axes3D.zAxis.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axes3D.zAxis.label.font.bold = 0
AnnotationAtts.axes3D.zAxis.label.font.italic = 0
AnnotationAtts.axes3D.zAxis.label.scaling = 0
AnnotationAtts.axes3D.zAxis.tickMarks.visible = 1
AnnotationAtts.axes3D.zAxis.tickMarks.majorMinimum = 0
AnnotationAtts.axes3D.zAxis.tickMarks.majorMaximum = 1
AnnotationAtts.axes3D.zAxis.tickMarks.minorSpacing = 0.02
AnnotationAtts.axes3D.zAxis.tickMarks.majorSpacing = 0.2
AnnotationAtts.axes3D.zAxis.grid = 0
AnnotationAtts.axes3D.setBBoxLocation = 0
AnnotationAtts.axes3D.bboxLocation = (0, 1, 0, 1, 0, 1)
AnnotationAtts.axes3D.triadColor = (0, 0, 0)
AnnotationAtts.axes3D.triadLineWidth = 0
AnnotationAtts.axes3D.triadFont = 0
AnnotationAtts.axes3D.triadBold = 1
AnnotationAtts.axes3D.triadItalic = 1
AnnotationAtts.axes3D.triadSetManually = 0
AnnotationAtts.userInfoFlag = 0
AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.userInfoFont.scale = 1
AnnotationAtts.userInfoFont.useForegroundColor = 1
AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.userInfoFont.bold = 0
AnnotationAtts.userInfoFont.italic = 0
AnnotationAtts.databaseInfoFlag = 0
AnnotationAtts.timeInfoFlag = 1
AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
AnnotationAtts.databaseInfoFont.scale = 1
AnnotationAtts.databaseInfoFont.useForegroundColor = 1
AnnotationAtts.databaseInfoFont.color = (0, 0, 0, 255)
AnnotationAtts.databaseInfoFont.bold = 0
AnnotationAtts.databaseInfoFont.italic = 0
AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
AnnotationAtts.databaseInfoTimeScale = 1
AnnotationAtts.databaseInfoTimeOffset = 0
AnnotationAtts.legendInfoFlag = 0
AnnotationAtts.backgroundColor = (255, 255, 255, 255)
AnnotationAtts.foregroundColor = (0, 0, 0, 255)
AnnotationAtts.gradientBackgroundStyle = AnnotationAtts.LeftToRight  # TopToBottom, BottomToTop, LeftToRight, RightToLeft, Radial
AnnotationAtts.gradientColor1 = (80, 80, 80, 255)
AnnotationAtts.gradientColor2 = (70, 70, 70, 255)
AnnotationAtts.backgroundMode = AnnotationAtts.Image  # Solid, Gradient, Image, ImageSphere
AnnotationAtts.backgroundImage = "../database/background_images/blue_grid.png"
AnnotationAtts.imageRepeatX = 1
AnnotationAtts.imageRepeatY = 1
AnnotationAtts.axesArray.visible = 1
AnnotationAtts.axesArray.ticksVisible = 1
AnnotationAtts.axesArray.autoSetTicks = 1
AnnotationAtts.axesArray.autoSetScaling = 1
AnnotationAtts.axesArray.lineWidth = 0
AnnotationAtts.axesArray.axes.title.visible = 1
AnnotationAtts.axesArray.axes.title.font.font = AnnotationAtts.axesArray.axes.title.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.title.font.scale = 1
AnnotationAtts.axesArray.axes.title.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.title.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.title.font.bold = 0
AnnotationAtts.axesArray.axes.title.font.italic = 0
AnnotationAtts.axesArray.axes.title.userTitle = 0
AnnotationAtts.axesArray.axes.title.userUnits = 0
AnnotationAtts.axesArray.axes.title.title = ""
AnnotationAtts.axesArray.axes.title.units = ""
AnnotationAtts.axesArray.axes.label.visible = 1
AnnotationAtts.axesArray.axes.label.font.font = AnnotationAtts.axesArray.axes.label.font.Arial  # Arial, Courier, Times
AnnotationAtts.axesArray.axes.label.font.scale = 1
AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
AnnotationAtts.axesArray.axes.label.font.bold = 0
AnnotationAtts.axesArray.axes.label.font.italic = 0
AnnotationAtts.axesArray.axes.label.scaling = 0
AnnotationAtts.axesArray.axes.tickMarks.visible = 1
AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
AnnotationAtts.axesArray.axes.grid = 0
SetAnnotationAttributes(AnnotationAtts)
# Begin spontaneous state
View3DAtts = visit.View3DAttributes()
View3DAtts.viewNormal = (0, 0, 1)
View3DAtts.focus = (0, 0, 0)
View3DAtts.viewUp = (0, 1, 0)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.5
View3DAtts.nearPlane = -28.4429
View3DAtts.farPlane = 28.4429
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, 0)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
visit.SetView3D(View3DAtts)
# End spontaneous state

View3DAtts = visit.View3DAttributes()
View3DAtts.viewNormal = (0, 0, 1)
View3DAtts.focus = (0, 0, 0)
View3DAtts.viewUp = (0, 1, 0)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 0.5
View3DAtts.nearPlane = -28.4429
View3DAtts.farPlane = 28.4429
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (0, 0, 0)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
visit.SetView3D(View3DAtts)
light0 = visit.LightAttributes()
light0.enabledFlag = 1
light0.type = light0.Object  # Ambient, Object, Camera
light0.direction = (0.666, -0.666, -0.666)
light0.color = (255, 255, 255, 255)
light0.brightness = 1
visit.SetLight(0, light0)
light1 = visit.LightAttributes()
light1.enabledFlag = 0
light1.type = light1.Camera  # Ambient, Object, Camera
light1.direction = (0, 0, -1)
light1.color = (255, 255, 255, 255)
light1.brightness = 1
visit.SetLight(1, light1)
light2 = visit.LightAttributes()
light2.enabledFlag = 0
light2.type = light2.Camera  # Ambient, Object, Camera
light2.direction = (0, 0, -1)
light2.color = (255, 255, 255, 255)
light2.brightness = 1
visit.SetLight(2, light2)
light3 = visit.LightAttributes()
light3.enabledFlag = 0
light3.type = light3.Camera  # Ambient, Object, Camera
light3.direction = (0, 0, -1)
light3.color = (255, 255, 255, 255)
light3.brightness = 1
visit.SetLight(3, light3)
light4 = visit.LightAttributes()
light4.enabledFlag = 0
light4.type = light4.Camera  # Ambient, Object, Camera
light4.direction = (0, 0, -1)
light4.color = (255, 255, 255, 255)
light4.brightness = 1
visit.SetLight(4, light4)
light5 = visit.LightAttributes()
light5.enabledFlag = 0
light5.type = light5.Camera  # Ambient, Object, Camera
light5.direction = (0, 0, -1)
light5.color = (255, 255, 255, 255)
light5.brightness = 1
visit.SetLight(5, light5)
light6 = visit.LightAttributes()
light6.enabledFlag = 0
light6.type = light6.Camera  # Ambient, Object, Camera
light6.direction = (0, 0, -1)
light6.color = (255, 255, 255, 255)
light6.brightness = 1
visit.SetLight(6, light6)
light7 = visit.LightAttributes()
light7.enabledFlag = 0
light7.type = light7.Camera  # Ambient, Object, Camera
light7.direction = (0, 0, -1)
light7.color = (255, 255, 255, 255)
light7.brightness = 1
visit.SetLight(7, light7)
visit.RenderingAtts = visit.RenderingAttributes()
RenderingAtts.antialiasing = 0
RenderingAtts.orderComposite = 1
RenderingAtts.depthCompositeThreads = 2
RenderingAtts.depthCompositeBlocking = 65536
RenderingAtts.alphaCompositeThreads = 2
RenderingAtts.alphaCompositeBlocking = 65536
RenderingAtts.depthPeeling = 0
RenderingAtts.occlusionRatio = 0
RenderingAtts.numberOfPeels = 16
RenderingAtts.multiresolutionMode = 0
RenderingAtts.multiresolutionCellSize = 0.002
RenderingAtts.geometryRepresentation = RenderingAtts.Surfaces  # Surfaces, Wireframe, Points
RenderingAtts.stereoRendering = 0
RenderingAtts.stereoType = RenderingAtts.CrystalEyes  # RedBlue, Interlaced, CrystalEyes, RedGreen
RenderingAtts.notifyForEachRender = 0
RenderingAtts.scalableActivationMode = RenderingAtts.Auto  # Never, Always, Auto
RenderingAtts.scalableAutoThreshold = 2000000
RenderingAtts.specularFlag = 1
RenderingAtts.specularCoeff = 0.13
RenderingAtts.specularPower = 3.2
RenderingAtts.specularColor = (255, 255, 255, 255)
RenderingAtts.doShadowing = 0
RenderingAtts.shadowStrength = 0.5
RenderingAtts.doDepthCueing = 0
RenderingAtts.depthCueingAutomatic = 1
RenderingAtts.startCuePoint = (-10, 0, 0)
RenderingAtts.endCuePoint = (10, 0, 0)
RenderingAtts.compressionActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.colorTexturingFlag = 1
RenderingAtts.compactDomainsActivationMode = RenderingAtts.Never  # Never, Always, Auto
RenderingAtts.compactDomainsAutoThreshold = 256
RenderingAtts.osprayRendering = 0
RenderingAtts.ospraySPP = 1
RenderingAtts.osprayAO = 0
RenderingAtts.osprayShadows = 0
SetRenderingAttributes(RenderingAtts)
visit.AddPlot("Pseudocolor", "mesh_quality/warpage", 1, 1)
visit.AddOperator("Transform", 1)
PseudocolorAtts = visit.PseudocolorAttributes()
PseudocolorAtts.scaling = PseudocolorAtts.Linear  # Linear, Log, Skew
PseudocolorAtts.skewFactor = 1
PseudocolorAtts.limitsMode = PseudocolorAtts.OriginalData  # OriginalData, ActualData
PseudocolorAtts.minFlag = 1
PseudocolorAtts.min = -0.1
PseudocolorAtts.useBelowMinColor = 1
PseudocolorAtts.belowMinColor = (31, 31, 31, 255)
PseudocolorAtts.maxFlag = 1
PseudocolorAtts.max = 0.1
PseudocolorAtts.useAboveMaxColor = 1
PseudocolorAtts.aboveMaxColor = (0, 255, 0, 255)
PseudocolorAtts.centering = PseudocolorAtts.Natural  # Natural, Nodal, Zonal
PseudocolorAtts.colorTableName = "Default"
PseudocolorAtts.invertColorTable = 0
PseudocolorAtts.opacityType = PseudocolorAtts.FullyOpaque  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
PseudocolorAtts.opacityVariable = ""
PseudocolorAtts.opacity = 1
PseudocolorAtts.opacityVarMin = 0
PseudocolorAtts.opacityVarMax = 1
PseudocolorAtts.opacityVarMinFlag = 0
PseudocolorAtts.opacityVarMaxFlag = 0
PseudocolorAtts.pointSize = 0.05
PseudocolorAtts.pointType = PseudocolorAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
PseudocolorAtts.pointSizeVarEnabled = 0
PseudocolorAtts.pointSizeVar = "default"
PseudocolorAtts.pointSizePixels = 2
PseudocolorAtts.lineType = PseudocolorAtts.Line  # Line, Tube, Ribbon
PseudocolorAtts.lineWidth = 0
PseudocolorAtts.tubeResolution = 10
PseudocolorAtts.tubeRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
PseudocolorAtts.tubeRadiusAbsolute = 0.125
PseudocolorAtts.tubeRadiusBBox = 0.005
PseudocolorAtts.tubeRadiusVarEnabled = 0
PseudocolorAtts.tubeRadiusVar = ""
PseudocolorAtts.tubeRadiusVarRatio = 10
PseudocolorAtts.tailStyle = PseudocolorAtts.NONE  # NONE, Spheres, Cones
PseudocolorAtts.headStyle = PseudocolorAtts.NONE  # NONE, Spheres, Cones
PseudocolorAtts.endPointRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
PseudocolorAtts.endPointRadiusAbsolute = 0.125
PseudocolorAtts.endPointRadiusBBox = 0.05
PseudocolorAtts.endPointResolution = 10
PseudocolorAtts.endPointRatio = 5
PseudocolorAtts.endPointRadiusVarEnabled = 0
PseudocolorAtts.endPointRadiusVar = ""
PseudocolorAtts.endPointRadiusVarRatio = 10
PseudocolorAtts.renderSurfaces = 1
PseudocolorAtts.renderWireframe = 0
PseudocolorAtts.renderPoints = 0
PseudocolorAtts.smoothingLevel = 0
PseudocolorAtts.legendFlag = 1
PseudocolorAtts.lightingFlag = 1
PseudocolorAtts.wireframeColor = (0, 0, 0, 0)
PseudocolorAtts.pointColor = (0, 0, 0, 0)
visit.SetPlotOptions(PseudocolorAtts)
visit.AddPlot("Pseudocolor", "mesh_quality/warpage", 1, 1)
visit.AddOperator("Transform", 1)
PseudocolorAtts = visit.PseudocolorAttributes()
PseudocolorAtts.scaling = PseudocolorAtts.Linear  # Linear, Log, Skew
PseudocolorAtts.skewFactor = 1
PseudocolorAtts.limitsMode = PseudocolorAtts.OriginalData  # OriginalData, ActualData
PseudocolorAtts.minFlag = 1
PseudocolorAtts.min = -0.1
PseudocolorAtts.useBelowMinColor = 1
PseudocolorAtts.belowMinColor = (31, 31, 31, 255)
PseudocolorAtts.maxFlag = 1
PseudocolorAtts.max = 0.1
PseudocolorAtts.useAboveMaxColor = 1
PseudocolorAtts.aboveMaxColor = (0, 255, 0, 255)
PseudocolorAtts.centering = PseudocolorAtts.Natural  # Natural, Nodal, Zonal
PseudocolorAtts.colorTableName = "Default"
PseudocolorAtts.invertColorTable = 0
PseudocolorAtts.opacityType = PseudocolorAtts.FullyOpaque  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
PseudocolorAtts.opacityVariable = ""
PseudocolorAtts.opacity = 1
PseudocolorAtts.opacityVarMin = 0
PseudocolorAtts.opacityVarMax = 1
PseudocolorAtts.opacityVarMinFlag = 0
PseudocolorAtts.opacityVarMaxFlag = 0
PseudocolorAtts.pointSize = 0.05
PseudocolorAtts.pointType = PseudocolorAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
PseudocolorAtts.pointSizeVarEnabled = 0
PseudocolorAtts.pointSizeVar = "default"
PseudocolorAtts.pointSizePixels = 2
PseudocolorAtts.lineType = PseudocolorAtts.Line  # Line, Tube, Ribbon
PseudocolorAtts.lineWidth = 0
PseudocolorAtts.tubeResolution = 10
PseudocolorAtts.tubeRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
PseudocolorAtts.tubeRadiusAbsolute = 0.125
PseudocolorAtts.tubeRadiusBBox = 0.005
PseudocolorAtts.tubeRadiusVarEnabled = 0
PseudocolorAtts.tubeRadiusVar = ""
PseudocolorAtts.tubeRadiusVarRatio = 10
PseudocolorAtts.tailStyle = PseudocolorAtts.NONE  # NONE, Spheres, Cones
PseudocolorAtts.headStyle = PseudocolorAtts.NONE  # NONE, Spheres, Cones
PseudocolorAtts.endPointRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
PseudocolorAtts.endPointRadiusAbsolute = 0.125
PseudocolorAtts.endPointRadiusBBox = 0.05
PseudocolorAtts.endPointResolution = 10
PseudocolorAtts.endPointRatio = 5
PseudocolorAtts.endPointRadiusVarEnabled = 0
PseudocolorAtts.endPointRadiusVar = ""
PseudocolorAtts.endPointRadiusVarRatio = 10
PseudocolorAtts.renderSurfaces = 1
PseudocolorAtts.renderWireframe = 0
PseudocolorAtts.renderPoints = 0
PseudocolorAtts.smoothingLevel = 0
PseudocolorAtts.legendFlag = 1
PseudocolorAtts.lightingFlag = 1
PseudocolorAtts.wireframeColor = (0, 0, 0, 0)
PseudocolorAtts.pointColor = (0, 0, 0, 0)
visit.SetPlotOptions(PseudocolorAtts)
# Logging for AddAnnotationObject is not implemented yet.
# Logging for AddAnnotationObject is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
visit.DrawPlots()
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
visit.SetActivePlots(0)
visit.SetActivePlots(0)
TransformAtts = visit.TransformAttributes()
TransformAtts.doRotate = 0
TransformAtts.rotateOrigin = (0, 0, 0)
TransformAtts.rotateAxis = (0, 0, 1)
TransformAtts.rotateAmount = 0
TransformAtts.rotateType = TransformAtts.Deg  # Deg, Rad
TransformAtts.doScale = 0
TransformAtts.scaleOrigin = (0, 0, 0)
TransformAtts.scaleX = 1
TransformAtts.scaleY = 1
TransformAtts.scaleZ = 1
TransformAtts.doTranslate = 0
TransformAtts.translateX = 0
TransformAtts.translateY = 0
TransformAtts.translateZ = 0
TransformAtts.transformType = TransformAtts.Similarity  # Similarity, Coordinate, Linear
TransformAtts.inputCoordSys = TransformAtts.Cartesian  # Cartesian, Cylindrical, Spherical
TransformAtts.outputCoordSys = TransformAtts.Spherical  # Cartesian, Cylindrical, Spherical
TransformAtts.continuousPhi = 0
TransformAtts.m00 = 1
TransformAtts.m01 = 0
TransformAtts.m02 = 0
TransformAtts.m03 = 0
TransformAtts.m10 = 0
TransformAtts.m11 = 1
TransformAtts.m12 = 0
TransformAtts.m13 = 0
TransformAtts.m20 = 0
TransformAtts.m21 = 0
TransformAtts.m22 = 1
TransformAtts.m23 = 0
TransformAtts.m30 = 0
TransformAtts.m31 = 0
TransformAtts.m32 = 0
TransformAtts.m33 = 1
TransformAtts.invertLinearTransform = 0
TransformAtts.vectorTransformMethod = TransformAtts.AsDirection  # NONE, AsPoint, AsDisplacement, AsDirection
TransformAtts.transformVectors = 1
visit.SetOperatorOptions(TransformAtts, 0, 1)
visit.SetActivePlots(0)
visit.SetActivePlots(1)
visit.SetActivePlots(1)
TransformAtts = visit.TransformAttributes()
TransformAtts.doRotate = 0
TransformAtts.rotateOrigin = (0, 0, 0)
TransformAtts.rotateAxis = (0, 0, 1)
TransformAtts.rotateAmount = 0
TransformAtts.rotateType = TransformAtts.Deg  # Deg, Rad
TransformAtts.doScale = 0
TransformAtts.scaleOrigin = (0, 0, 0)
TransformAtts.scaleX = 1
TransformAtts.scaleY = 1
TransformAtts.scaleZ = 1
TransformAtts.doTranslate = 0
TransformAtts.translateX = 0
TransformAtts.translateY = 0
TransformAtts.translateZ = 0
TransformAtts.transformType = TransformAtts.Similarity  # Similarity, Coordinate, Linear
TransformAtts.inputCoordSys = TransformAtts.Cartesian  # Cartesian, Cylindrical, Spherical
TransformAtts.outputCoordSys = TransformAtts.Spherical  # Cartesian, Cylindrical, Spherical
TransformAtts.continuousPhi = 0
TransformAtts.m00 = 1
TransformAtts.m01 = 0
TransformAtts.m02 = 0
TransformAtts.m03 = 0
TransformAtts.m10 = 0
TransformAtts.m11 = 1
TransformAtts.m12 = 0
TransformAtts.m13 = 0
TransformAtts.m20 = 0
TransformAtts.m21 = 0
TransformAtts.m22 = 1
TransformAtts.m23 = 0
TransformAtts.m30 = 0
TransformAtts.m31 = 0
TransformAtts.m32 = 0
TransformAtts.m33 = 1
TransformAtts.invertLinearTransform = 0
TransformAtts.vectorTransformMethod = TransformAtts.AsDirection  # NONE, AsPoint, AsDisplacement, AsDirection
TransformAtts.transformVectors = 1
visit.SetOperatorOptions(TransformAtts, 0, 0)
visit.SetActivePlots(1)
visit.DrawPlots()
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
visit.SetActivePlots(0)
visit.SetActivePlots(0)
TransformAtts = visit.TransformAttributes()
TransformAtts.doRotate = 0
TransformAtts.rotateOrigin = (0, 0, 0)
TransformAtts.rotateAxis = (0, 0, 1)
TransformAtts.rotateAmount = 0
TransformAtts.rotateType = TransformAtts.Deg  # Deg, Rad
TransformAtts.doScale = 0
TransformAtts.scaleOrigin = (0, 0, 0)
TransformAtts.scaleX = 1
TransformAtts.scaleY = 1
TransformAtts.scaleZ = 1
TransformAtts.doTranslate = 1
TransformAtts.translateX = 4.98831
TransformAtts.translateY = 0
TransformAtts.translateZ = 0
TransformAtts.transformType = TransformAtts.Similarity  # Similarity, Coordinate, Linear
TransformAtts.inputCoordSys = TransformAtts.Cartesian  # Cartesian, Cylindrical, Spherical
TransformAtts.outputCoordSys = TransformAtts.Spherical  # Cartesian, Cylindrical, Spherical
TransformAtts.continuousPhi = 0
TransformAtts.m00 = 1
TransformAtts.m01 = 0
TransformAtts.m02 = 0
TransformAtts.m03 = 0
TransformAtts.m10 = 0
TransformAtts.m11 = 1
TransformAtts.m12 = 0
TransformAtts.m13 = 0
TransformAtts.m20 = 0
TransformAtts.m21 = 0
TransformAtts.m22 = 1
TransformAtts.m23 = 0
TransformAtts.m30 = 0
TransformAtts.m31 = 0
TransformAtts.m32 = 0
TransformAtts.m33 = 1
TransformAtts.invertLinearTransform = 0
TransformAtts.vectorTransformMethod = TransformAtts.AsDirection  # NONE, AsPoint, AsDisplacement, AsDirection
TransformAtts.transformVectors = 1
visit.SetOperatorOptions(TransformAtts, 0, 0)
visit.SetActivePlots(0)
visit.SetActivePlots(1)
visit.SetActivePlots(1)
TransformAtts = visit.TransformAttributes()
TransformAtts.doRotate = 0
TransformAtts.rotateOrigin = (0, 0, 0)
TransformAtts.rotateAxis = (0, 0, 1)
TransformAtts.rotateAmount = 0
TransformAtts.rotateType = TransformAtts.Deg  # Deg, Rad
TransformAtts.doScale = 0
TransformAtts.scaleOrigin = (0, 0, 0)
TransformAtts.scaleX = 1
TransformAtts.scaleY = 1
TransformAtts.scaleZ = 1
TransformAtts.doTranslate = 1
TransformAtts.translateX = -4.98831
TransformAtts.translateY = -0
TransformAtts.translateZ = 0
TransformAtts.transformType = TransformAtts.Similarity  # Similarity, Coordinate, Linear
TransformAtts.inputCoordSys = TransformAtts.Cartesian  # Cartesian, Cylindrical, Spherical
TransformAtts.outputCoordSys = TransformAtts.Spherical  # Cartesian, Cylindrical, Spherical
TransformAtts.continuousPhi = 0
TransformAtts.m00 = 1
TransformAtts.m01 = 0
TransformAtts.m02 = 0
TransformAtts.m03 = 0
TransformAtts.m10 = 0
TransformAtts.m11 = 1
TransformAtts.m12 = 0
TransformAtts.m13 = 0
TransformAtts.m20 = 0
TransformAtts.m21 = 0
TransformAtts.m22 = 1
TransformAtts.m23 = 0
TransformAtts.m30 = 0
TransformAtts.m31 = 0
TransformAtts.m32 = 0
TransformAtts.m33 = 1
TransformAtts.invertLinearTransform = 0
TransformAtts.vectorTransformMethod = TransformAtts.AsDirection  # NONE, AsPoint, AsDisplacement, AsDirection
TransformAtts.transformVectors = 1
visit.SetOperatorOptions(TransformAtts, 0, 0)
visit.SetActivePlots(1)
visit.DrawPlots()
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
visit.SetActivePlots(0)
visit.SetActivePlots(0)
TransformAtts = visit.TransformAttributes()
TransformAtts.doRotate = 0
TransformAtts.rotateOrigin = (0, 0, 0)
TransformAtts.rotateAxis = (0, 0, 1)
TransformAtts.rotateAmount = 0
TransformAtts.rotateType = TransformAtts.Deg  # Deg, Rad
TransformAtts.doScale = 0
TransformAtts.scaleOrigin = (0, 0, 0)
TransformAtts.scaleX = 1
TransformAtts.scaleY = 1
TransformAtts.scaleZ = 1
TransformAtts.doTranslate = 1
TransformAtts.translateX = 4.98032
TransformAtts.translateY = 0.278443
TransformAtts.translateZ = 0
TransformAtts.transformType = TransformAtts.Similarity  # Similarity, Coordinate, Linear
TransformAtts.inputCoordSys = TransformAtts.Cartesian  # Cartesian, Cylindrical, Spherical
TransformAtts.outputCoordSys = TransformAtts.Spherical  # Cartesian, Cylindrical, Spherical
TransformAtts.continuousPhi = 0
TransformAtts.m00 = 1
TransformAtts.m01 = 0
TransformAtts.m02 = 0
TransformAtts.m03 = 0
TransformAtts.m10 = 0
TransformAtts.m11 = 1
TransformAtts.m12 = 0
TransformAtts.m13 = 0
TransformAtts.m20 = 0
TransformAtts.m21 = 0
TransformAtts.m22 = 1
TransformAtts.m23 = 0
TransformAtts.m30 = 0
TransformAtts.m31 = 0
TransformAtts.m32 = 0
TransformAtts.m33 = 1
TransformAtts.invertLinearTransform = 0
TransformAtts.vectorTransformMethod = TransformAtts.AsDirection  # NONE, AsPoint, AsDisplacement, AsDirection
TransformAtts.transformVectors = 1
visit.SetOperatorOptions(TransformAtts, 0, 0)
visit.SetActivePlots(0)
visit.SetActivePlots(1)
visit.SetActivePlots(1)
TransformAtts = visit.TransformAttributes()
TransformAtts.doRotate = 0
TransformAtts.rotateOrigin = (0, 0, 0)
TransformAtts.rotateAxis = (0, 0, 1)
TransformAtts.rotateAmount = 0
TransformAtts.rotateType = TransformAtts.Deg  # Deg, Rad
TransformAtts.doScale = 0
TransformAtts.scaleOrigin = (0, 0, 0)
TransformAtts.scaleX = 1
TransformAtts.scaleY = 1
TransformAtts.scaleZ = 1
TransformAtts.doTranslate = 1
TransformAtts.translateX = -4.98032
TransformAtts.translateY = -0.278443
TransformAtts.translateZ = 0
TransformAtts.transformType = TransformAtts.Similarity  # Similarity, Coordinate, Linear
TransformAtts.inputCoordSys = TransformAtts.Cartesian  # Cartesian, Cylindrical, Spherical
TransformAtts.outputCoordSys = TransformAtts.Spherical  # Cartesian, Cylindrical, Spherical
TransformAtts.continuousPhi = 0
TransformAtts.m00 = 1
TransformAtts.m01 = 0
TransformAtts.m02 = 0
TransformAtts.m03 = 0
TransformAtts.m10 = 0
TransformAtts.m11 = 1
TransformAtts.m12 = 0
TransformAtts.m13 = 0
TransformAtts.m20 = 0
TransformAtts.m21 = 0
TransformAtts.m22 = 1
TransformAtts.m23 = 0
TransformAtts.m30 = 0
TransformAtts.m31 = 0
TransformAtts.m32 = 0
TransformAtts.m33 = 1
TransformAtts.invertLinearTransform = 0
TransformAtts.vectorTransformMethod = TransformAtts.AsDirection  # NONE, AsPoint, AsDisplacement, AsDirection
TransformAtts.transformVectors = 1
visit.SetOperatorOptions(TransformAtts, 0, 0)
visit.SetActivePlots(1)
visit.DrawPlots()
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
# Logging for SetAnnotationObjectOptions is not implemented yet.
visit.SetActivePlots(0)
visit.SetActivePlots(0)
TransformAtts = visit.TransformAttributes()
TransformAtts.doRotate = 0
TransformAtts.rotateOrigin = (0, 0, 0)
TransformAtts.rotateAxis = (0, 0, 1)
TransformAtts.rotateAmount = 0
TransformAtts.rotateType = TransformAtts.Deg  # Deg, Rad
TransformAtts.doScale = 0
TransformAtts.scaleOrigin = (0, 0, 0)
TransformAtts.scaleX = 1
TransformAtts.scaleY = 1
TransformAtts.scaleZ = 1
TransformAtts.doTranslate = 1
TransformAtts.translateX = 4.9568
TransformAtts.translateY = 0.555994
TransformAtts.translateZ = 0
TransformAtts.transformType = TransformAtts.Similarity  # Similarity, Coordinate, Linear
TransformAtts.inputCoordSys = TransformAtts.Cartesian  # Cartesian, Cylindrical, Spherical
TransformAtts.outputCoordSys = TransformAtts.Spherical  # Cartesian, Cylindrical, Spherical
TransformAtts.continuousPhi = 0
TransformAtts.m00 = 1
TransformAtts.m01 = 0
TransformAtts.m02 = 0
TransformAtts.m03 = 0
TransformAtts.m10 = 0
TransformAtts.m11 = 1
TransformAtts.m12 = 0
TransformAtts.m13 = 0
TransformAtts.m20 = 0
TransformAtts.m21 = 0
TransformAtts.m22 = 1
TransformAtts.m23 = 0
TransformAtts.m30 = 0
TransformAtts.m31 = 0
TransformAtts.m32 = 0
TransformAtts.m33 = 1
TransformAtts.invertLinearTransform = 0
TransformAtts.vectorTransformMethod = TransformAtts.AsDirection  # NONE, AsPoint, AsDisplacement, AsDirection
TransformAtts.transformVectors = 1
visit.SetOperatorOptions(TransformAtts, 0, 0)
visit.SetActivePlots(0)
