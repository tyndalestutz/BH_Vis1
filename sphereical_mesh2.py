import numpy as np
import trimesh

def sphere(r, n_points):
    u = np.linspace(0, 2 * np.pi, n_points)
    v = np.linspace(0, np.pi, n_points)
    x = r * np.outer(np.cos(u), np.sin(v))
    y = r * np.outer(np.sin(u), np.sin(v))
    z = r * np.outer(np.ones(np.size(u)), np.cos(v))
    return x, y, z

def save_sphere_obj(x, y, z, filename):
    faces = np.array([])
    for i in range(x.shape[0] - 1):
        for j in range(x.shape[1] - 1):
            a = i * x.shape[1] + j
            b = i * x.shape[1] + j + 1
            c = (i + 1) * x.shape[1] + j
            d = (i + 1) * x.shape[1] + j + 1
            faces = np.append(faces, [a, b, c])
            faces = np.append(faces, [b, c, d])
    faces = faces.reshape((-1, 3)).astype(np.int64)
    mesh = trimesh.Trimesh(vertices=np.c_[x.flatten(), y.flatten(), z.flatten()], faces=faces)
    mesh.export(filename, file_type='obj')

x, y, z = sphere(1, 100)
save_sphere_obj(x, y, z, 'sphere.obj')
