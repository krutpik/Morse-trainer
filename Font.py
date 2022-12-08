import pygame


def font(screen, text, x, y, size, color):
    text_color = color
    font = pygame.font.Font('Font/a_OldTyperNr Regular.ttf', size)
    text = str(text)
    font_image = font.render(text, True, text_color)
    font_image_rect = font_image.get_rect()
    font_image_rect.centerx = x
    font_image_rect.y = y
    screen.blit(font_image, font_image_rect)
