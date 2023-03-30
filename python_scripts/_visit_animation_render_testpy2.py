import sys, csv
sys.path.append("/usr/local/3.3.1/linux-x86_64/lib/site-packages") 
import visit
visit.Launch()
import visit
v = visit

# object 0: Black hole 1
# object 1: Black hole 2
# bh1_x, bh2_x, etc are the values of the xyz coordinates of each black hole
# L1_X, L2_x, etc are the xyz magnitudes of angular momentum (L) vectors 1 and 2.

database = "../database/mesh/iscos_halfr_sphere_sub8.obj"
bh_data = "../database/synthetic_coords/synthetic_data_ang_momentum.csv"



def default_atts():
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
    
    View3DAtts = v.View3DAttributes()
    View3DAtts.viewNormal = (0, 0, 1)
    View3DAtts.focus = (0, 0, 0)
    View3DAtts.viewUp = (0, 1, 0)
    View3DAtts.nearPlane = -28.4429
    View3DAtts.farPlane = 28.4429
    View3DAtts.windowValid = 1
    v.SetView3D(View3DAtts)

    light = v.LightAttributes()
    light.enabledFlag = 1
    light.type = light.Object 
    light.direction = (0.666, -0.666, -0.666)
    v.SetLight(0, light)

def create_spheres():
    v.AddPlot("Pseudocolor", "mesh_quality/warpage", 1, 1)
    v.AddOperator("Transform")
    v.AddPlot("Pseudocolor", "mesh_quality/warpage", 1, 1)
    v.AddOperator("Transform")

def set_coords(objNum, x, y, z):
    v.SetActivePlots(objNum)
    trasnformAtts = v.TransformAttributes()
    trasnformAtts.doTranslate = 1
    trasnformAtts.translateX = x
    trasnformAtts.translateY = y
    trasnformAtts.translateZ = z
    v.SetOperatorOptions(trasnformAtts, 0, 0)

visit.OpenDatabase(database, 0)
default_atts()
create_spheres()

L1 = v.CreateAnnotationObject("Line3D")
L2 = v.CreateAnnotationObject("Line3D")


#to find annotation attributes
#print(L1) 

L1.arrow2 = 1
L1.arrow2Height = 0.2
L2.arrow2 = 1
L1.arrow2Height = 0.2


with open(bh_data, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # skip the header row
    v.DrawPlots()
    for row in reader:
        t = float(row[0])
        bh1_x = float(row[1])
        bh1_y = float(row[2])
        bh1_z = float(row[3])
        L1_x = float(row[4])
        L1_y = float(row[5])
        L1_z = float(row[6])
        bh2_x = float(row[7])
        bh2_y = float(row[8])
        bh2_z = float(row[9])
        L2_x = float(row[10])
        L2_y = float(row[11])
        L2_z = float(row[12])
        
        L1.point1 = (bh1_x, bh1_y, bh1_z)
        L1.point2 = (bh1_x + L1_x, bh1_y + L1_y, bh1_z + L1_z)
        L2.point1 = (bh2_x, bh2_y, bh2_z)
        L2.point2 = (bh2_x + L2_x, bh2_y + L2_y, bh2_z + L2_z)
        set_coords(0, bh1_x, bh1_y, bh1_z)
        set_coords(1, bh2_x, bh2_y, bh2_z)
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

