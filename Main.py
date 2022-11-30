import sys
import pygame
from Button import Button

pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 290, 450
screen = pygame.display.set_mode((width, height))


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

objects = []

def myFunction():
    print('.')


Button(38, 220, objects, screen, WHITE, myFunction)

def key_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def button_spawn():
    for object in objects:
        object.process()

while True:
    screen.fill(WHITE)
    key_event()
    button_spawn()
    pygame.display.flip()
    fpsClock.tick(fps)
