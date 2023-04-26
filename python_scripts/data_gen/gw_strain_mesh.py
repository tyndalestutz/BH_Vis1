import vtk, sys, math
import numpy as np
import os

# Set up parameters
parent_directory = os.path.dirname(os.path.dirname(__file__))
output_directory = parent_directory + "mesh" #"../data/mesh/test732"
num_points_x = 200
num_points_y = 200
delta_x = 0.1
delta_y = 0.1
num_states = 100
smoothness_variable = 5
amplitude = 0.5  # Set the amplitude for both stems
black_hole_radius = 1  # Set the radius of the "black holes"

def Ysminus2l2m2(theta, phi):
    if math.fmod(phi,math.pi/2) == 0:
        return (-1/8)*math.sqrt(15/(2*math.pi))*pow(math.sin(theta),2)
    else:
        return (-1/8)*math.sqrt(15/(2*math.pi))*pow(math.sin(theta),2)*math.exp(2*1j*phi) 

#check to make sure program is run with proper arguments
if len(sys.argv) != 2:
    print("Usage: python3 gw_strain_mesh.py <h strain data.txt>")
    sys.exit(1)

file_name = sys.argv[1]

if not file_name.endswith('.txt'):
    print("Error: Input file must have a '.txt' extension.")
    sys.exit(1)

with open(file_name, 'r') as file:
    # Read the lines and ignore lines starting with #
    lines = [line for line in file.readlines() if not line.startswith('#')]

# Convert lines to arrays and sort by time
data = np.array([list(map(np.float64, line.split())) for line in lines])
data = data[np.argsort(data[:, 0])]

# Remove duplicate times
_, index = np.unique(data[:, 0], return_index=True)
data = data[index]

# Create folder for output files
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

time = data[:,0]
gw_strain = data[:,1] + 1j * data[:,2]

for t, h in zip(time, gw_strain):
    # Create mesh
    points = vtk.vtkPoints()
    grid = vtk.vtkStructuredGrid()
    grid.SetDimensions(num_points_x, num_points_y, 1)

    #for all 2-dimensional simulations, phi = 0
    phi = 0

    for j in range(num_points_y):
        y = -delta_y * (num_points_y - 1) + 2 * j * delta_y
        for i in range(num_points_x):
            x = -delta_x * (num_points_x - 1) + 2 * i * delta_x

            theta = math.atan(y/x)
            phi = 0 #for all 2-dimensional simulations, phi = 0
            r = math.sqrt(x**2 + y**2)
            z = (amplitude * Ysminus2l2m2(theta,phi) * h).real
            points.InsertNextPoint(x, y, z)
    grid.SetPoints(points)

    # Write mesh to file
    writer = vtk.vtkXMLStructuredGridWriter()
    filename = output_directory = "/state{}.vts".format(t)
    writer.SetFileName(filename)
    writer.SetInputData(grid)
    writer.Write()