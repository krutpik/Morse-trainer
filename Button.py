import pygame


class Button():
    def __init__(self, x, y, objects, screen, WHITE, onclickFunction=None, buttonText='Ключ',  onePress=False):
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
        objects.append(self)

    def process(self):
        mousePos = pygame.mouse.get_pos()
        if self.buttonRect.collidepoint(mousePos):
            if pygame.mouse.get_pressed()[0]:
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        self.image.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        self.screen.blit(self.image, self.buttonRect)
