# -*- coding: utf-8 -*-

import pygame
import time
import random

HEIGHT = 640
WIDTH = 1000

tg_clock = time.time()
pygame.init()
pygame.mixer.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('xahidin')  # set title
clock = pygame.time.Clock()
# font = pygame.font.SysFont("alkatipui", 16)#system font
alkatip = pygame.font.Font('ALKATIP.ttf', 26)  # local font


class Object:
    def __init__(self, alma, back):
        self.alma = pygame.image.load(alma)
        self.back = pygame.image.load(back).convert()


# white circle
def target():
    global a
    global r
    global txt
    global tg_clock

    if time.time() > tg_clock and len(TG) < 25:
        TG.append([random.randint(50, WIDTH - 50), 0])
        tg_clock = time.time() + random.random()
    for j, i in enumerate(TG):
        display.blit(obj.alma, i)
        display.blit(alkatip.render(herp[j], True, (250, 250, 250)), (i[0] + 25, i[1] + 20))

        if TG[j][1] > 580:
            # TG.pop(j)
            pass
        else:
            TG[j][1] += 1


# press event
def check_key(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            print(event)
        if event.key == pygame.K_RIGHT:
            print(event)
        if event.key == pygame.K_DOWN:
            print(event)
        if event.key == pygame.K_UP:
            print(event)
        if event.key == pygame.K_SPACE:
            pygame.mixer.music.play()


BST = []
TG = []
obj = Object('apple64.png', 'back.jpg')
herp = ["ئ", "ا", "ە", "ې", "ى", "و", "ۇ", "ۆ", "ۈ", "ن", "ت", "س", "ش", "غ", "ك", "ڭ", "گ", "ل", "م", "ف", "ق", "ر",
        "ز", "ژ"]

brock = False
while not brock:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            brock = True
            continue
        check_key(event)
    display.blit(obj.back, (0, 0))
    target()
    pygame.display.update()
    clock.tick(100)
