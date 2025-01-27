import numpy as np


class Shape:

    def generate_shape(self):
        shape_i_rot1 = np.array([[1, 0], [1, 1], [1, 2], [1, 3]], np.int32)
        shape_i_rot2 = np.array([[0, 1], [1, 1], [2, 1], [3, 1]], np.int32)
        shape_i = Shape(np.array([shape_i_rot1, shape_i_rot2]))
