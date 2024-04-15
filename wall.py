import random
from vertex import Vertex
import pygame
import numpy as np

class Wall:
    def __init__(self, v1, v2, v3, v4):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4
        self.color = self.get_random_color()

    def get_random_color(self):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return (red, green, blue)
    
    def project_to_2d(self, screen, d, if_full_walls):
        vertices = []
        vertices.append(self.v1.get_2d_representation(d))
        vertices.append(self.v2.get_2d_representation(d))
        vertices.append(self.v3.get_2d_representation(d))
        vertices.append(self.v4.get_2d_representation(d))
        if(if_full_walls):
            pygame.draw.polygon(screen, self.color, vertices)
        else:
            pygame.draw.polygon(screen, self.color, vertices, 1)

    def is_visible(self):
        vector1 = np.array([self.v2.x, self.v2.y, self.v2.z]) - np.array([self.v1.x, self.v1.y, self.v1.z])
        vector2 = np.array([self.v3.x, self.v3.y, self.v3.z]) - np.array([self.v1.x, self.v1.y, self.v1.z])
        normal_vector = np.cross(vector1, vector2)
        dot = np.dot(normal_vector, np.array([-self.v1.x, -self.v1.y, -self.v1.z]))
        return self.v1.z > 0 and self.v2.z > 0 and self.v3.z > 0 and self.v4.z > 0 and dot > 0

