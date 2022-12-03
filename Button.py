import pygame
import time


class Button:
    def __init__(self, x, y, objects, screen, WHITE, onclickFunction=None, buttonText='Ключ', onePress=True):
        self.x = x
        self.y = y
        self.WHITE = WHITE
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load('circle.png')
        self.buttonRect = self.image.get_rect()
        self.buttonRect.x = self.x
        self.buttonRect.y = self.y
        self.buttonSurf = pygame.font.SysFont('Arial', 40).render(buttonText, True, WHITE)
        self.pressing_time = 0
        self.number = 0
        objects.append(self)

    def process(self):
        global toc, tic
        mousePos = pygame.mouse.get_pos()
        if self.buttonRect.collidepoint(mousePos):
            if pygame.mouse.get_pressed()[0]:
                self.number += 1
                time.sleep(0.5)
            else:
                self.onclickFunction()
                self.number = 0
        self.image.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        self.screen.blit(self.image, self.buttonRect)
