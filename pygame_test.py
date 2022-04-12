from typing import Match
import pygame
from pygame.constants import *
pygame.init()

color_black = (0, 0, 0)
color_red = (255, 0, 0)
color_orange = (255, 128, 0)
color_yellow = (255, 255, 0)
color_green = (0, 255, 0)
color_blue = (0, 0, 255)
color_white = (255, 255, 255)
screen_color = color_white
x = 0
y = 0
screen = pygame.display.set_mode((500, 500))
objects = pygame.Surface((500, 500))

def reset_screen(screen):
    screen.fill(screen_color) # Makes screen background a specific color
    pygame.display.update()    # Updates screen

def draw_shapes(screen, objects):
    objects.fill(screen_color) # Refills Object's surface with screen_color
    
    pygame.draw.rect(objects, color_black, pygame.Rect(30 + x, 30 + y, 30, 30))

    pygame.draw.polygon(objects, color_red, [(100 + x, 100 + y), (220 + x, 30 + y), (150 + x, 200 + y)])

    pygame.draw.circle(objects, color_green, (200 + x, 300+ y), 100, width = 10)
    screen.blit(objects, (0, 0)) # Draws the objects on the object Surface
    pygame.display.update() # Updates entire screen

def refresh_screen(screen, objects):
    reset_screen(screen)
    draw_shapes(screen, objects)


# Initial Screen, with the shapes drawn in
refresh_screen(screen, objects)
screen.blit(objects, (0, 0))


running = True
while running:
    for event in pygame.event.get():        # Allows user to quit the application
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:         # Quit application when ESCAPE key is pressed
                print("ESCAPE KEY")
                running = False
            elif event.key == K_RIGHT:        # Move shapes to the right by 50 pixels
                x += 50
                refresh_screen(screen, objects)
                print("RIGHT KEY")
            elif event.key == K_LEFT:         # Move shapes to the left by 50 pixels
                x -= 50
                refresh_screen(screen, objects)
                print("LEFT KEY")
            elif event.key == K_UP:           # Move shapes upward by 50 pixels
                y -= 50
                refresh_screen(screen, objects)
                print("UP KEY")
            elif event.key == K_DOWN:         # Move shapes downward by 50 pixels
                y += 50
                refresh_screen(screen, objects)
                print("DOWN KEY")
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if event.button == 1:             # prints the clicked mouse button in the terminal
                print("Left Click")
                screen_color = color_black
                refresh_screen(screen, objects)
            elif event.button == 2:
                print("Middle Click")
                screen_color = color_red
                refresh_screen(screen, objects)
            elif event.button == 3:
                print("Right Button")
                screen_color = color_orange
                refresh_screen(screen, objects)
            elif event.button == 4:
                print("Up Scroll")
                screen_color = color_yellow
                refresh_screen(screen, objects)
            elif event.button == 5:
                print("Down Scroll")
                screen_color = color_green
                refresh_screen(screen, objects)
            elif event.button == 6:
                print("Back Button")
                screen_color = color_blue
                refresh_screen(screen, objects)
            elif event.button == 7:
                print("Forward Button")
                screen_color = color_white
                refresh_screen(screen, objects)
        else: continue

pygame.quit()

