import sys
import pygame
from Button import Button
import ABC
from random import choices
import Font
import json_import


pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 290, 450
pygame_icon = pygame.image.load('icon.png')
pygame.display.set_icon(pygame_icon)
screen = pygame.display.set_mode((width, height))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 153, 0)
BLUE = (0, 0, 255)

objects = []

answers_time = json_import.answers_time
answer = ''
mistake = True
result = ''
result_color = RED


def myFunction():
    global answer
    if button.number > json_import.pressed_dashes:
        answer = f'{answer}-'
    elif button.number > json_import.pressed_dot:
        answer = f'{answer}.'


button = Button(38, 220, objects, screen, WHITE, myFunction)
if json_import.language.upper() == 'EN':
    abc = ABC.abc_en
else:
    abc = ABC.abc_ru

def key_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def button_spawn():
    for object in objects:
        object.process()


print('Тренажёр передачи сигнала азбукой Морзе \nОлейников production\n')

while True:
    screen.fill(WHITE)
    key_event()
    button_spawn()
    fpsClock.tick(fps)
    if json_import.answers_time == answers_time:
        mistake = True
        json_import.answers_time = 0
        random = choices(list(abc.keys()))
        for ran in random:
            answer = ''
    Font.font(screen, ran, screen.get_rect().centerx, 70, 60, BLACK)
    Font.font(screen, answer, screen.get_rect().centerx, 120, 60, BLACK)
    if answer == abc[ran]:
        result = 'Правильно'
        result_color = GREEN
        json_import.answers_time = answers_time - 1
    elif json_import.answers_time == answers_time - 1 or (len(answer) > 5 and mistake):
        mistake = False
        result = 'Неправильно!'
        result_color = RED
        json_import.answers_time = answers_time - 1
    json_import.answers_time += 1
    Font.font(screen, result, screen.get_rect().centerx, 25, 30, result_color)
    pygame.display.flip()
