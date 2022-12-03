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
        self.tic = time.perf_counter()
        self.toc = time.perf_counter()
        objects.append(self)

    def process(self):
        global toc, tic
        time.sleep(0.1)
        mousePos = pygame.mouse.get_pos()
        if self.buttonRect.collidepoint(mousePos):
            if pygame.mouse.get_pressed()[0]:
                self.tic = time.perf_counter()
                self.onclickFunction()
            else:
                self.toc = time.perf_counter()
            self.pressing_time = self.tic - self.toc
        self.image.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        self.screen.blit(self.image, self.buttonRect)
