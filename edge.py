from vertex import Vertex
import pygame

class Edge:
    def __init__(self, start_vertex, end_vertex, color):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.color = color
    
    def project_to_2d(self, screen, d, screen_width, screen_height):
        if(self.is_visible()):
            pygame.draw.line(screen, self.color, self.start_vertex.get_2d_representation(d, screen_width, screen_height), self.end_vertex.get_2d_representation(d, screen_width, screen_height), 1)

    def is_visible(self):
        return self.start_vertex.z > 0 and self.end_vertex.z > 0