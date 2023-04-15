import vtk
import numpy as np
import os

# Set up grid parameters
num_points_x = 300
num_points_y = 300
delta_x = 0.1
delta_y = 0.1
num_states = 1000
smoothness_variable = 10

# Create folder for output files
if not os.path.exists("../data/mesh/test15"):
    os.makedirs("../data/mesh/test15")

for t in range(num_states):
    # Create mesh
    points = vtk.vtkPoints()
    grid = vtk.vtkStructuredGrid()
    grid.SetDimensions(num_points_x, num_points_y, 1)
    for j in range(num_points_y):
        y = -delta_y*(num_points_y-1) + 2*j*delta_y
        for i in range(num_points_x):
            x = -delta_x*(num_points_x-1) + 2*i*delta_x
            # Modify the z-coordinate calculation to create a ripple spiral on the XY plane
            r = np.sqrt(x ** 2 + y ** 2)
            theta = np.arctan2(y, x)  # Calculate angle with respect to x-axis
            z = np.sin(r - t/smoothness_variable + theta)  # Add angles to z-coordinate
            points.InsertNextPoint(x, y, z)
    grid.SetPoints(points)

    # Write mesh to file
    writer = vtk.vtkXMLStructuredGridWriter()
    filename = "../data/mesh/test15/state{}.vts".format(t)
    writer.SetFileName(filename)
    writer.SetInputData(grid)
    writer.Write()