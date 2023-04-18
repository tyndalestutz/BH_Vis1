import vtk
import numpy as np
import os

# Set up grid parameters
num_points_x = 200
num_points_y = 200
delta_x = 0.1
delta_y = 0.1
num_states = 100
smoothness_variable = 5
amplitude = 0.5  # Set the amplitude for both stems
black_hole_radius = 1  # Set the radius of the "black holes"

# Create folder for output files
if not os.path.exists("../data/mesh/test13"):
    os.makedirs("../data/mesh/test13")

for t in range(num_states):
    # Create mesh
    points = vtk.vtkPoints()
    grid = vtk.vtkStructuredGrid()
    grid.SetDimensions(num_points_x, num_points_y, 1)
    for j in range(num_points_y):
        y = -delta_y * (num_points_y - 1) + 2 * j * delta_y
        for i in range(num_points_x):
            x = -delta_x * (num_points_x - 1) + 2 * i * delta_x
            # Modify the z-coordinate calculation to create two opposite spirals on the same YZ plane with equal amplitude
            r1 = np.sqrt(y ** 2 + (x + black_hole_radius) ** 2)  # Point 1 at (black_hole_radius, 0)
            theta1 = np.arctan2(x + black_hole_radius, y)  # Calculate angle with respect to y-axis for point 1
            z1 = amplitude * np.sin(r1 - t / smoothness_variable + theta1)  # Add angles to z-coordinate for point 1 with amplitude

            r2 = np.sqrt(y ** 2 + (x - black_hole_radius) ** 2)  # Point 2 at (-black_hole_radius, 0)
            theta2 = np.arctan2(x - black_hole_radius, y)  # Calculate angle with respect to y-axis for point 2
            z2 = amplitude * np.sin(r2 - t / smoothness_variable + theta2)  # Add angles to z-coordinate for point 2 with amplitude

            # Set the z-coordinates of both points to be the same, so that they are on the same YZ plane
            z = (z1 + z2) / 2
            points.InsertNextPoint(x, y, z)
    grid.SetPoints(points)

    # Write mesh to file
    writer = vtk.vtkXMLStructuredGridWriter()
    filename = "../data/mesh/test13/state{}.vts".format(t)
    writer.SetFileName(filename)
    writer.SetInputData(grid)
    writer.Write()
