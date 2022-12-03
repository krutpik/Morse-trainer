import sys
import pygame
from Button import Button
from ABC import abc
import time
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


def myFunction():
    print(f'{duf.pressing_time:0.2f}')
    if 0.1 < duf.pressing_time < 0.15:
        print('.')
    elif 1.5 > duf.pressing_time > 0.4:
        print('-')

def mourse_code():
    random = choices(list(abc.keys()), k=5)

    answers = 0

    print('Тренажёр передачи сигнала азбукой Морзе \nОлейников production\n')

    answer = input('Готов ?\n')
    if answer.upper() == 'ДА' or answer.upper() == 'Y':
        tic = time.perf_counter()
        for ran in random:
            print(f'\n{ran}')
            answer = input(': ')
            if answer == abc[ran]:
                answers += 1
                print('Правильно')
            else:
                print('Неверно!')
        toc = time.perf_counter()
        print('Итог:\n')

        if answers < 5:
            print(f'Правильных ответов - {answers}')
        else:
            print('Всё верно!')
            print(f"Вы ввели все буквы за {toc - tic:0.0f} секунд")


duf = Button(38, 220, objects, screen, WHITE, myFunction)


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
