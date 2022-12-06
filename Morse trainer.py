import sys
import pygame
from Button import Button
import ABC
import Settings
from random import choices
import Font

pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 290, 450
screen = pygame.display.set_mode((width, height))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 153, 0)
BLUE = (0, 0, 255)

objects = []

answers_time = Settings.answers_time
answer = ''
mistake = True
result = ''
result_color = RED


def myFunction():
    global answer
    if button.number > Settings.pressed_dashes:
        answer = f'{answer}-'
    elif button.number > Settings.pressed_dot:
        answer = f'{answer}.'


button = Button(38, 220, objects, screen, WHITE, myFunction)
if Settings.language.upper() == 'EN':
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
    if Settings.answers_time == answers_time:
        mistake = True
        Settings.answers_time = 0
        random = choices(list(abc.keys()))
        for ran in random:
            answer = ''
    Font.font(screen, ran, screen.get_rect().centerx, 70, 60, BLACK)
    Font.font(screen, answer, screen.get_rect().centerx, 120, 60, BLACK)
    if answer == abc[ran]:
        result = 'Правильно'
        result_color = GREEN
        Settings.answers_time = answers_time - 1
    elif Settings.answers_time == answers_time - 1 or (len(answer) > 5 and mistake):
        mistake = False
        result = 'Неправильно!'
        result_color = RED
        Settings.answers_time = answers_time - 1
    Settings.answers_time += 1
    Font.font(screen, result, screen.get_rect().centerx, 25, 30, result_color)
    pygame.display.flip()
