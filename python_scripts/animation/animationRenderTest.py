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

# Creates the box around the spheres with axes, labels, etc.
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
# Creates a viewpoint in the visualization, it's coordinates, etc.
View3DAtts = v.View3DAttributes()

# Top down view: viewNormal(0, 0, 1), viewUp(0, 1 ,0)
View3DAtts.viewNormal = (1, 0, 0.1) # one of the main attributes that determine viewing orientation
View3DAtts.focus = (0, 0, 0)
View3DAtts.viewUp = (-0.1, 0.25, 1) # other main attribute determining viewing orientation
View3DAtts.nearPlane = -15
View3DAtts.farPlane = 15
View3DAtts.imageZoom = 1.2
View3DAtts.windowValid = 1
v.SetView3D(View3DAtts)

v.AddPlot("Pseudocolor", "mesh_quality/warpage", 1, 1)
v.AddOperator("Transform")
v.AddPlot("Pseudocolor", "mesh_quality/warpage", 1, 1)
v.AddOperator("Transform")

# Set Lighting
light = v.LightAttributes()
light.enabledFlag = 1
light.type = light.Object 
light.direction = (0.666, -0.666, -0.666)
v.SetLight(0, light)

# create image/inset
image = v.CreateAnnotationObject("Image")
image.image = "/home/guest/Documents/Seth/vscode/animationRenders/animation1/synthetic_BH_test_animation" + "0100" + ".png"
image.position = (0, 0)
image.width = 40
image.height = 40
image.maintainAspectRatio = 1
image.visible = 1 # assuming 1 for visible 0 for not, maybe useful for rendering? either that or image.active = 1
# Print the other image annotation options
#print(image)

# transform function
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
    current_image = 0
    for row in reader:
        t = float(row[0])
        x1 = float(row[1])
        y1 = float(row[2])
        x2 = float(row[3])
        y2 = float(row[4])
        
        set_coords(0, x1, y1, 0)
        set_coords(1, x2, y2, 0)

        # super janky way to update the image inset, currently figuring out a better way
        image.image = "/home/guest/Documents/Seth/vscode/animationRenders/animation1/synthetic_BH_test_animation" + str(current_image) + "000" + ".png"
        current_image += 1
        v.DrawPlots()

        '''
        # Create new object that allows the current window's attributes to be changed - preparation for image saving
        s = v.SaveWindowAttributes()

        # Set file/window attributes and save
        s.fileName = "animationTestFrame"
        s.format = s.PNG
        s.progressive = 1
        s.width = 772
        s.height = 702
        s.screenCapture = 1
        v.SetSaveWindowAttributes(s)

        # Save the window to an image
        v.SaveWindow()
        '''
        #input_pattern = "synthetic_BH_test_animation_%04d.png"
        #output_movie = "streamline_crop_example.mp4"
        #v.encoding.encode(input_pattern,output_movie,fdup=4)

# The following command worked to create a movie from the file of pngs
#ffmpeg -framerate 1000 -i animationTestFrame%04d.png -vf "scale=770:-2" -c:v libx264 -r 1000 -pix_fmt yuv420p output.mp4