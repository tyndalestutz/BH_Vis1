import sys, csv, time
sys.path.append("/usr/local/3.3.1/linux-x86_64/lib/site-packages") 
import visit
visit.Launch()
import visit
v = visit

#object 0: Black hole 1
#object 1: Black hole 2


database = "/home/guest/Documents/Tyndale/vscode/database/iscos_halfr_sphere_sub8.obj"
bh_data = "/home/guest/Documents/Tyndale/vscode/visit_run/synthetic_data_BH_scaled_x10_lowres2.csv"


visit.OpenDatabase(database, 0)

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

# Begin spontaneous state
View3DAtts = v.View3DAttributes()
View3DAtts.viewNormal = (0, 0, 1)
View3DAtts.focus = (0, 0, 0)
View3DAtts.viewUp = (0, 1, 0)
View3DAtts.nearPlane = -28.4429
View3DAtts.farPlane = 28.4429
View3DAtts.windowValid = 1
v.SetView3D(View3DAtts)

v.AddPlot("Pseudocolor", "mesh_quality/warpage", 1, 1)
v.AddOperator("Transform")
v.AddPlot("Pseudocolor", "mesh_quality/warpage", 1, 1)
v.AddOperator("Transform")


light = v.LightAttributes()
light.enabledFlag = 1
light.type = light.Object 
light.direction = (0.666, -0.666, -0.666)
v.SetLight(0, light)

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
        s = v.SaveWindowAttributes()
        s.fileName = "synthetic_BH_test_animation"
        s.format = s.PNG
        s.progressive = 1
        s.width = 772
        s.height = 702
        s.screenCapture = 1
        v.SetSaveWindowAttributes(s)
        # Save the window
        #v.SaveWindow()
        
        #input_pattern = "synthetic_BH_test_animation_%04d.png"
        #output_movie = "streamline_crop_example.mp4"
        #v.encoding.encode(input_pattern,output_movie,fdup=4)

# The following command worked to create a movie from the file of pngs
#ffmpeg -framerate 1000 -i synthetic_BH_test_animation%04d.png -vf "scale=770:-2" -c:v libx264 -r 1000 -pix_fmt yuv420p output.mp4

