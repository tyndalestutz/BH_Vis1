import numpy as np
from scipy.fft import fftn
from vtk import vtkPolyData, vtkPoints, vtkTriangle, vtkCellArray, vtkXMLPolyDataWriter

# Specify the full path to your Psi4 data file
data_file = "/home/guest/Documents/Users/Tyndale/sample_gw_data/Rpsi4_l2-r0100.0-onlyl2m2.txt"

# Load Psi4 data from file
psi4_data = np.loadtxt(data_file)

# Extract time, x, y, and z coordinates from Psi4 data
time = psi4_data[:, 0]
x = psi4_data[:, 1]
y = psi4_data[:, 2]
z = psi4_data[:, 3]

# Loop through time steps
for i in range(len(time)):
    # Perform FPI on x, y, and z coordinates
    x_fpi = fftn(x[i])
    y_fpi = fftn(y[i])
    z_fpi = fftn(z[i])

    # Create vtkPoints object
    points = vtkPoints()

    # Add points to vtkPoints object
    for j in range(len(x_fpi)):
        points.InsertNextPoint(x_fpi[j], y_fpi[j], z_fpi[j])

    # Create vtkPolyData object
    polydata = vtkPolyData()

    # Set the points in vtkPolyData object
    polydata.SetPoints(points)

    # Create vtkCellArray object for mesh connectivity
    cells = vtkCellArray()

    # Add triangular cells to vtkCellArray object
    for j in range(len(x_fpi)):
        if j % 2 == 0:
            triangle = vtkTriangle()
            triangle.GetPointIds().SetId(0, j)
            triangle.GetPointIds().SetId(1, (j + 1) % len(x_fpi))
            triangle.GetPointIds().SetId(2, (j + 2) % len(x_fpi))
            cells.InsertNextCell(triangle)

    # Set the cells in vtkPolyData object
    polydata.SetPolys(cells)

    # Create vtkXMLPolyDataWriter to write vtkPolyData to VTK file
    writer = vtkXMLPolyDataWriter()
    writer.SetFileName("output_{}.vtp".format(time[i]))
    writer.SetInputData(polydata)
    writer.Write()
