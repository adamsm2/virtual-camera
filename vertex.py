import numpy as np

screen_width = 1280
screen_height = 720

class Vertex:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def get_2d_representation(self, d):
        x = screen_width/2 + (self.x * d) / self.z
        y = screen_height/2 - (self.y * d) / self.z
        return [x, y]

    def get_4d_matrix(self):
        return np.matrix([self.x, self.y, self.z, 1]).reshape(4,1)