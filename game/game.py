import pygame
from pygame.locals import *
from sys import exit

pygame.init()
s_size = (500, 500)
screen = pygame.display.set_mode(s_size, 0, 32)

font_height = font.get_linesize()
event_text = []
font = pygame.font.SysFont("arial", 16)
while True:
    event = pygame.event.wait()
    event_text.append(str(event))
    if event.type == QUIT:
        exit()
    if event == KEYDOWN:
        if event.key == K_LEFT:
            move_x = -1
    screen.fill((255, 255, 255))
    pygame.display.update()
    y = s_size[1] - font_height
    for text in reversed(event_text):
        screen.blit(font.render(text, True, (0, 0, 0)), (0, y))
        y -= font_height
    pygame.display.update()
