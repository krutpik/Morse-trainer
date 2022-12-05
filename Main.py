import sys
import pygame
from Button import Button
from ABC import abc
import Settings
from random import choices

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

answers_time = Settings.answers_time
answer = ''
mistake = True


def myFunction():
    global answer
    if button.number > Settings.pressed_dashes:
        answer = f'{answer}-'
    elif button.number > Settings.pressed_dot:
        answer = f'{answer}.'


button = Button(38, 220, objects, screen, WHITE, myFunction)


def key_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def button_spawn():
    for object in objects:
        object.process()


print('Тренажёр передачи сигнала азбуки Морзе \nОлейников production\n')

while True:
    screen.fill(WHITE)
    key_event()
    button_spawn()
    pygame.display.flip()
    fpsClock.tick(fps)
    if Settings.answers_time == answers_time:
        mistake = True
        Settings.answers_time = 0
        answer = ''
        random = choices(list(abc.keys()))
        for ran in random:
            print(f'\n{ran}\n')
    if answer == abc[ran]:
        print('Правильно')
        Settings.answers_time = answers_time - 1
    elif Settings.answers_time == answers_time - 1 or (list(answer) > list(abc[ran]) and mistake):
        mistake = False
        Settings.answers_time = answers_time - 1
        print('Неправильно!')
    Settings.answers_time += 1
