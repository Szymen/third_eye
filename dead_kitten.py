
import numpy as np

def get_rotation_matrix(angle_x, angle_y, angle_z ):
    sin_x = np.sin(angle_x * (np.pi / 180))
    cos_x = np.cos(angle_x * (np.pi / 180))

    sin_y = np.sin(angle_y * (np.pi / 180))
    cos_y = np.cos(angle_y * (np.pi / 180))

    sin_z = np.sin(angle_z * (np.pi / 180))
    cos_z = np.cos(angle_z * (np.pi / 180))

    rx = np.array([
        [1.0, 0.0, 0.0],
        [0.0, cos_x, -sin_x],
        [0.0, sin_x, cos_x],
    ])

    ry = np.array([
        [cos_y, 0.0, sin_y],
        [0.0, 1.0, 0.0],
        [-sin_y, 0.0, cos_y],
        ])

    rz = np.array([
        [cos_z, -sin_z, 0.0],
        [sin_z, cos_z, 0.0],
        [0.0, 0.0, 1.0],
    ])
    return np.matmul(np.matmul(rx, ry), rz)
