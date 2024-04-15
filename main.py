from transformations import Transformations
import pygame
from cube import Cube
from math import sqrt, pi

class App:
    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 720
        self.d = 300
        self.distance_between_cubes = 40
        self.cube_edge_length = 150
        self.translation_step = 0.5
        self.rotation_angle = pi / 800
        self.main()

    def compare_distance(self, wall):
        max_distance = 0
        for vertex in [wall.v1, wall.v2, wall.v3, wall.v4]:
            distance = sqrt((vertex.x) ** 2 + (vertex.y) ** 2 + (vertex.z) ** 2)
            if distance > max_distance:
                max_distance = distance
        return -max_distance

    def init_cubes(self):
        cubes = []
        distance_between_start_vertices = self.distance_between_cubes + self.cube_edge_length
        cubes.append(Cube(0, 0, 100, self.cube_edge_length))
        cubes.append(Cube(distance_between_start_vertices, 0, 100, self.cube_edge_length))
        cubes.append(Cube(0, 0, 100+distance_between_start_vertices, self.cube_edge_length))
        cubes.append(Cube(distance_between_start_vertices, 0, 100+distance_between_start_vertices, self.cube_edge_length))
        cubes.append(Cube(0, distance_between_start_vertices, 100, self.cube_edge_length))
        cubes.append(Cube(distance_between_start_vertices, distance_between_start_vertices, 100, self.cube_edge_length))
        cubes.append(Cube(0, distance_between_start_vertices, 100+distance_between_start_vertices, self.cube_edge_length))
        cubes.append(Cube(distance_between_start_vertices, distance_between_start_vertices, 100+distance_between_start_vertices, self.cube_edge_length))
        return cubes

    def main(self):
        pygame.init()
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        screen.fill((0, 0, 0))

        cubes = self.init_cubes()
        all_walls = []
        for cube in cubes:
            all_walls.extend(cube.walls)

        keys_pressed = {}
        for key in [pygame.K_SPACE, pygame.K_LSHIFT, pygame.K_a, pygame.K_d,
                    pygame.K_w, pygame.K_s, pygame.K_DOWN, pygame.K_UP,
                    pygame.K_LEFT, pygame.K_RIGHT, pygame.K_q, pygame.K_e,
                    pygame.K_c, pygame.K_v, pygame.K_1, pygame.K_2, pygame.K_3]:
            keys_pressed[key] = False

        transformations = Transformations(self.translation_step, self.rotation_angle)
        draw_walls = False
        if_full_walls = True
        is_running = True
        while is_running:
            screen.fill((0, 0, 0))
            if(draw_walls):
                visible_walls = []
                for cube in cubes:
                    visible_walls.extend(cube.get_visible_walls())
                sorted_walls = sorted(visible_walls, key=self.compare_distance)
                for wall in sorted_walls:
                    wall.project_to_2d(screen, self.d, if_full_walls, self.screen_width, self.screen_height)
            else:
                for cube in cubes:
                    for edge in cube.edges:
                        edge.project_to_2d(screen, self.d, self.screen_width, self.screen_height)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key in keys_pressed:
                        keys_pressed[event.key] = True
                elif event.type == pygame.KEYUP:
                    if event.key in keys_pressed:
                        keys_pressed[event.key] = False
            for cube in cubes:
                if keys_pressed[pygame.K_SPACE]:
                    cube.transform(transformations.up)
                if keys_pressed[pygame.K_LSHIFT]:
                    cube.transform(transformations.down)
                if keys_pressed[pygame.K_a]:
                    cube.transform(transformations.left)
                if keys_pressed[pygame.K_d]:
                    cube.transform(transformations.right)
                if keys_pressed[pygame.K_w]:
                    cube.transform(transformations.forward)
                if keys_pressed[pygame.K_s]:
                    cube.transform(transformations.backward)
                if keys_pressed[pygame.K_DOWN]:
                    cube.transform(transformations.rotate_x_left)
                if keys_pressed[pygame.K_UP]:
                    cube.transform(transformations.rotate_x_right)
                if keys_pressed[pygame.K_LEFT]:
                    cube.transform(transformations.rotate_y_left)
                if keys_pressed[pygame.K_RIGHT]:
                    cube.transform(transformations.rotate_y_right)
                if keys_pressed[pygame.K_q]:
                    cube.transform(transformations.rotate_z_left)
                if keys_pressed[pygame.K_e]:
                    cube.transform(transformations.rotate_z_right)
                if keys_pressed[pygame.K_c]:
                    self.d = self.d * 1.001
                if keys_pressed[pygame.K_v]:
                    self.d = self.d / 1.001
                if keys_pressed[pygame.K_1]:
                    draw_walls = False
                if keys_pressed[pygame.K_2]:
                    draw_walls = True
                    if_full_walls = True
                if keys_pressed[pygame.K_3]:
                    draw_walls = True
                    if_full_walls = False



            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    app = App()

