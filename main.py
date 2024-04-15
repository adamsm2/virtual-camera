from transformations import Transformations
import pygame
from cube import Cube
import math

def compare_distance(wall):
    return get_wall_min_distance_to_camera(wall)

def get_wall_min_distance_to_camera(wall):
    min_distance = float('inf')
    max_distance = 0
    for vertex in [wall.v1, wall.v2, wall.v3, wall.v4]:
        distance = math.sqrt((vertex.x) ** 2 + (vertex.y) ** 2 + (vertex.z) ** 2)
        if distance < min_distance:
            min_distance = distance
        if distance > max_distance:
            max_distance = distance
    return -max_distance




screen_width = 1280
screen_height = 720
d = 300
distance_between_cubes = 40
cube_edge_length = 150
distance_between_start_vertices = distance_between_cubes + cube_edge_length

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((0, 0, 0))

cubes = []
cubes.append(Cube(0, 0, 100))
cubes.append(Cube(distance_between_start_vertices, 0, 100))
cubes.append(Cube(0, 0, 100+distance_between_start_vertices))
cubes.append(Cube(distance_between_start_vertices, 0, 100+distance_between_start_vertices))
cubes.append(Cube(0, distance_between_start_vertices, 100))
cubes.append(Cube(distance_between_start_vertices, distance_between_start_vertices, 100))
cubes.append(Cube(0, distance_between_start_vertices, 100+distance_between_start_vertices))
cubes.append(Cube(distance_between_start_vertices, distance_between_start_vertices, 100+distance_between_start_vertices))


all_walls = []
for cube in cubes:
    all_walls.extend(cube.walls)


keys_pressed = {}
for key in [pygame.K_SPACE, pygame.K_LSHIFT, pygame.K_a, pygame.K_d,
            pygame.K_w, pygame.K_s, pygame.K_DOWN, pygame.K_UP,
            pygame.K_LEFT, pygame.K_RIGHT, pygame.K_q, pygame.K_e,
            pygame.K_c, pygame.K_v, pygame.K_1, pygame.K_2, pygame.K_3]:
    keys_pressed[key] = False

draw_walls = False
if_full_walls = True
is_running = True
while is_running:
    screen.fill((0, 0, 0))
    if(draw_walls):
        visible_walls = []
        for cube in cubes:
            visible_walls.extend(cube.get_visible_walls())
        sorted_walls = sorted(visible_walls, key=compare_distance)
        for wall in sorted_walls:
            wall.project_to_2d(screen, d, if_full_walls)
    else:
        for cube in cubes:
            cube.project_edges_to_2d(screen, d)

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
            cube.transform(Transformations.up)
        if keys_pressed[pygame.K_LSHIFT]:
            cube.transform(Transformations.down)
        if keys_pressed[pygame.K_a]:
            cube.transform(Transformations.left)
        if keys_pressed[pygame.K_d]:
            cube.transform(Transformations.right)
        if keys_pressed[pygame.K_w]:
            cube.transform(Transformations.forward)
        if keys_pressed[pygame.K_s]:
            cube.transform(Transformations.backward)
        if keys_pressed[pygame.K_DOWN]:
            cube.transform(Transformations.rotate_x_left)
        if keys_pressed[pygame.K_UP]:
            cube.transform(Transformations.rotate_x_right)
        if keys_pressed[pygame.K_LEFT]:
            cube.transform(Transformations.rotate_y_left)
        if keys_pressed[pygame.K_RIGHT]:
            cube.transform(Transformations.rotate_y_right)
        if keys_pressed[pygame.K_q]:
            cube.transform(Transformations.rotate_z_left)
        if keys_pressed[pygame.K_e]:
            cube.transform(Transformations.rotate_z_right)
        if keys_pressed[pygame.K_c]:
            d = d * 1.001
        if keys_pressed[pygame.K_v]:
            d = d / 1.001
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

