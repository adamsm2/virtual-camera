from vertex import Vertex
from edge import Edge
from wall import Wall
import numpy as np
import random

class Cube:
    def __init__(self, x, y, z, cube_edge_length):
        self.x = x
        self.y = y
        self.z = z
        self.width = cube_edge_length
        self.height = cube_edge_length
        self.depth = cube_edge_length
        self.vertices = self.calculate_vertices()
        self.edges = self.calculate_edges()
        self.walls = self.calculate_walls()

    def get_random_color(self):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return (red, green, blue)

    def calculate_vertices(self):
        x, y, z = self.x, self.y, self.z
        width, height, depth = self.width, self.height, self.depth
        vertices = [
            Vertex(x, y, z), 
            Vertex(x + width, y, z), 
            Vertex(x, y, z + depth), 
            Vertex(x + width, y, z + depth), 
            Vertex(x, y + height, z), 
            Vertex(x + width, y + height, z), 
            Vertex(x, y + height, z + depth), 
            Vertex(x + width, y + height, z + depth) 
        ]
        return vertices
    
    def calculate_edges(self):
        vertices = self.vertices
        edges = [
            Edge(vertices[0], vertices[1], self.get_random_color()),
            Edge(vertices[1], vertices[3], self.get_random_color()),
            Edge(vertices[2], vertices[3], self.get_random_color()),
            Edge(vertices[0], vertices[2], self.get_random_color()),

            Edge(vertices[4], vertices[5], self.get_random_color()),
            Edge(vertices[5], vertices[7], self.get_random_color()),
            Edge(vertices[6], vertices[7], self.get_random_color()),
            Edge(vertices[4], vertices[6], self.get_random_color()),

            Edge(vertices[0], vertices[4], self.get_random_color()),
            Edge(vertices[1], vertices[5], self.get_random_color()),
            Edge(vertices[2], vertices[6], self.get_random_color()),
            Edge(vertices[3], vertices[7], self.get_random_color())
        ]
        return edges
    
    def calculate_walls(self):
        vertices = self.vertices
        walls = [
            Wall(vertices[0], vertices[1], vertices[3], vertices[2], self.get_random_color()),
            Wall(vertices[4], vertices[6], vertices[7], vertices[5], self.get_random_color()), 
            Wall(vertices[2], vertices[3], vertices[7], vertices[6], self.get_random_color()),
            Wall(vertices[1], vertices[5], vertices[7], vertices[3], self.get_random_color()),
            Wall(vertices[0], vertices[2], vertices[6], vertices[4], self.get_random_color()),
            Wall(vertices[0], vertices[4], vertices[5], vertices[1], self.get_random_color())
        ]
        return walls
    
    def transform(self, matrix):
        for vertex in self.vertices:
            transformed_vertex = np.dot(matrix, vertex.get_4d_matrix())
            vertex.x = transformed_vertex[0][0].item()
            vertex.y = transformed_vertex[1][0].item()
            vertex.z = transformed_vertex[2][0].item()

    def get_visible_walls(self):
        visible_walls = []
        for wall in self.walls:
            if(wall.is_visible()):
                visible_walls.append(wall)
        return visible_walls


