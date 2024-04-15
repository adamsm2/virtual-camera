import random
from vertex import Vertex

class Edge:
    def __init__(self, start_vertex, end_vertex):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.color = self.get_random_color()

    def get_random_color(self):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return (red, green, blue)
    
    def is_visible(self):
        return self.start_vertex.z > 0 and self.end_vertex.z > 0