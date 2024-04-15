from vertex import Vertex
from edge import Edge
from wall import Wall
import numpy as np
import pygame

class Cube:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.width = 150
        self.height = 150
        self.depth = 150
        self.vertices = self.calculate_vertices()
        self.edges = self.calculate_edges()
        self.walls = self.calculate_walls()

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
            Edge(vertices[0], vertices[1]),
            Edge(vertices[1], vertices[3]),
            Edge(vertices[2], vertices[3]),
            Edge(vertices[0], vertices[2]),

            Edge(vertices[4], vertices[5]),
            Edge(vertices[5], vertices[7]),
            Edge(vertices[6], vertices[7]),
            Edge(vertices[4], vertices[6]),

            Edge(vertices[0], vertices[4]),
            Edge(vertices[1], vertices[5]),
            Edge(vertices[2], vertices[6]),
            Edge(vertices[3], vertices[7])
        ]
        return edges
    
    def calculate_walls(self):
        vertices = self.vertices
        walls = [
            Wall(vertices[0], vertices[1], vertices[3], vertices[2]),
            Wall(vertices[4], vertices[6], vertices[7], vertices[5]), 
            Wall(vertices[2], vertices[3], vertices[7], vertices[6]),
            Wall(vertices[1], vertices[5], vertices[7], vertices[3]),
            Wall(vertices[0], vertices[2], vertices[6], vertices[4]),
            Wall(vertices[0], vertices[4], vertices[5], vertices[1])
        ]
        return walls
    
    def transform(self, matrix):
        for vertex in self.vertices:
            transformed_vertex = np.dot(matrix, vertex.get_4d_matrix())
            vertex.x = transformed_vertex[0][0].item()
            vertex.y = transformed_vertex[1][0].item()
            vertex.z = transformed_vertex[2][0].item()

    def project_edges_to_2d(self, screen, d):
        for edge in self.edges:
            if(edge.is_visible()):
                pygame.draw.line(screen, edge.color, edge.start_vertex.get_2d_representation(d), edge.end_vertex.get_2d_representation(d), 1)

    def get_visible_walls(self):
        visible_walls = []
        for wall in self.walls:
            if(wall.is_visible()):
                visible_walls.append(wall)
        return visible_walls


