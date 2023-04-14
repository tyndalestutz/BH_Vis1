import vtk
import numpy as np
import os

# Set up grid parameters
num_points_x = 100
num_points_y = 100
delta_x = 0.1
delta_y = 0.1
num_states = 1000
smoothity_variable = 10

# Create folder for output files
if not os.path.exists("../data/mesh/test1"):
    os.makedirs("../data/mesh/test1")

for t in range(num_states):
    # Create mesh
    points = vtk.vtkPoints()
    grid = vtk.vtkStructuredGrid()
    grid.SetDimensions(num_points_x, num_points_y, 1)
    for j in range(num_points_y):
        y = -delta_y*(num_points_y-1) + 2*j*delta_y
        for i in range(num_points_x):
            x = -delta_x*(num_points_x-1) + 2*i*delta_x
            z = np.sin(np.sqrt(x ** 2 + y ** 2) - t/smoothity_variable)
            points.InsertNextPoint(x, y, z)
    grid.SetPoints(points)

    # Write mesh to file
    writer = vtk.vtkXMLStructuredGridWriter()
    filename = "../data/mesh/test1/state{}.vts".format(t)
    writer.SetFileName(filename)
    writer.SetInputData(grid)
    writer.Write()
