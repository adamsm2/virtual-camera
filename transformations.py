import numpy as np
from math import sin, cos, pi


STEP = 0.5
ANGLE = pi / 800

class Transformations:
    
    @staticmethod
    def create_translation_matrix(x, y, z):
        return np.matrix([
            [1, 0, 0, x],
            [0, 1, 0, y],
            [0, 0, 1, z],
            [0, 0, 0, 1]
        ])
    
    @staticmethod
    def create_x_rotation_matrix(angle):
        return np.matrix([
            [1, 0, 0, 0],
            [0, cos(angle), -sin(angle), 0],
            [0, sin(angle), cos(angle), 0],
            [0, 0, 0, 1]
        ])
    
    @staticmethod
    def create_y_rotation_matrix(angle):
        return np.matrix([
            [cos(angle), 0, sin(angle), 0],
            [0, 1, 0, 0],
            [-sin(angle), 0, cos(angle), 0],
            [0, 0, 0, 1]
        ])

    @staticmethod
    def create_z_rotation_matrix(angle):
        return np.matrix([
            [cos(angle), -sin(angle), 0, 0],
            [sin(angle), cos(angle), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
    
Transformations.up = Transformations.create_translation_matrix(0, -STEP, 0)
Transformations.down = Transformations.create_translation_matrix(0, STEP, 0)
Transformations.left = Transformations.create_translation_matrix(STEP, 0, 0)
Transformations.right = Transformations.create_translation_matrix(-STEP, 0, 0)
Transformations.forward = Transformations.create_translation_matrix(0, 0, -STEP)
Transformations.backward = Transformations.create_translation_matrix(0, 0, STEP)

Transformations.rotate_x_left = Transformations.create_x_rotation_matrix(-ANGLE)
Transformations.rotate_x_right = Transformations.create_x_rotation_matrix(ANGLE)
Transformations.rotate_y_left = Transformations.create_y_rotation_matrix(ANGLE)
Transformations.rotate_y_right = Transformations.create_y_rotation_matrix(-ANGLE)
Transformations.rotate_z_left = Transformations.create_z_rotation_matrix(ANGLE)
Transformations.rotate_z_right = Transformations.create_z_rotation_matrix(-ANGLE)