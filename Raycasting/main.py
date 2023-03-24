import pygame
import sys

import math
import functions
import objects

pygame.init()

SIZE = WIDTH, HEIGHT = 1900, 1000
SCREEN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Raycasting")

FPS = 60
FPS_CLOCK = pygame.time.Clock()

# Source object from where rays are cast
source = objects.Circle(SCREEN, objects.WHITE, (WIDTH/2)/2-50, HEIGHT/2, 10)
source.draw()
# Center line of source object (Points towards the mouse)
center_line = objects.Line(SCREEN, objects.RED, source.this.center, (source.this.centerx, source.this.centery - 50))
# Field of view rays (cast from source object)
FOV = 80
RES = 400
fov_lines = []
for i in range(RES):
    fov_lines.append(objects.Line(SCREEN, objects.WHITE, source.this.center, (100, 100)))
# Field of view angle (to be incremented in running loop) & view distance
fov_angle = -FOV/2
view_distance = 1000
ray = FOV/RES

# Some control variables for source object
up = False
down = False
left = False
right = False

# Box object to render in 3d (boundries)
box = objects.Square(SCREEN, objects.BLUE, 30, 30, (WIDTH/2)-50)
# Cube to render in 3d
cube = objects.Square(SCREEN, objects.BLUE, (WIDTH/2)/2, HEIGHT/2, 50)
# Walls to render in 3d
walls = []
walls.append(objects.Line(SCREEN, objects.RED, (100, 800), (100, 600)))
walls.append(objects.Line(SCREEN, objects.RED, (300, 800), (300, 700)))
walls.append(objects.Line(SCREEN, objects.RED, (100, 600), (300, 600)))
walls.append(objects.Line(SCREEN, objects.RED, (300, 700), (500, 700)))

# TODO: Fix glitch of distant walls drawing over close walls
# Rect objects for 3d representation
x = (WIDTH/2)+6
rects = []
for i in range(RES):
    rects.append(objects.ThreeDRect(SCREEN, x, 3))
    x += 2.32


while True:

    # Fill and divide the screen
    SCREEN.fill(objects.BLACK)
    pygame.draw.rect(SCREEN, objects.GREEN, (20, 20, (WIDTH/2)-20, HEIGHT-40), 1)
    pygame.draw.rect(SCREEN, objects.GREEN, ((WIDTH/2)+5, 20, (WIDTH/2)-20, HEIGHT-40), 1)
    # Add sky and floor to render
    SCREEN.fill(objects.LIGHT_BLUE, ((WIDTH/2)+6, 21, (WIDTH/2)-22, 299))
    SCREEN.fill(objects.BROWN, ((WIDTH/2)+6, 300, (WIDTH/2)-22, HEIGHT-321))

    source.draw()
    box.draw()
    cube.draw()
    for wall in walls:
        wall.draw()

    # Update the center line's angle to follow mouse position
    center_line.start = source.this.center
    center_line.end = (source.this.centerx, source.this.centery - 50)
    center_angle = functions.point_to_mouse(source.this.center, pygame.mouse.get_pos())
    center_line.end = functions.rotate(source.this.center, center_line.end, center_angle)

    # Update field of view lines relative to center line
    rect = 0    # Check which rects need to be rendered
    for line in fov_lines:
        line.start = source.this.center
        line.end = (source.this.x, source.this.y - view_distance)
        line.end = functions.rotate(source.this.center, line.end, center_angle + fov_angle)
        fov_angle += ray

        if fov_angle >= FOV/2:
            fov_angle = -FOV/2
            ray = FOV/RES
    
        # Check for line, box intersections
        for side in box.sides:
            intersection = functions.line_intersect(line.start, line.end, side[0], side[1])
            if intersection:
                line.end = intersection
                distance = functions.calc_dist((line.start), (line.end))
                color_value = functions.limit(view_distance - distance - 650, 20, 255)
                rects[rect].draw(functions.get_range(distance, FOV), color_value, side[2])
        # Check for line, cube intersections
        for side in cube.sides:
            intersection = functions.line_intersect(line.start, line.end, side[0], side[1])
            if intersection:
                line.end = intersection
                distance = functions.calc_dist((line.start), (line.end))
                color_value = functions.limit(view_distance - distance - 650, 20, 255)
                rects[rect].draw(functions.get_range(distance, FOV), color_value, side[2])
        # Check for wall intersections
        for wall in walls:
            wall_intersection = functions.line_intersect(line.start, line.end, wall.start, wall.end)
            if wall_intersection:
                line.end = wall_intersection
                distance = functions.calc_dist((line.start), (line.end))
                color_value = functions.limit(view_distance - distance - 650, 20, 255)
                rects[rect].draw(functions.get_range(distance, FOV), color_value, "w")

        rect += 1
        line.draw()
    

    # Draw center line now so it's on top of FOV lines
    center_line.draw()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                up = True
            if event.key == pygame.K_s:
                down = True
            if event.key == pygame.K_a:
                left = True
            if event.key == pygame.K_d:
                right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                up = False
            if event.key == pygame.K_s:
                down = False
            if event.key == pygame.K_a:
                left = False
            if event.key == pygame.K_d:
                right = False

    if up:
        source.y -= 3
    if down:
        source.y += 3
    if left:
        source.x -= 3
    if right:
        source.x += 3

   
    pygame.display.update()
    FPS_CLOCK.tick(FPS)