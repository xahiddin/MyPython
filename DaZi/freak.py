tree_name = "back.jpg"
apple_name = "apple64.png"

# 导入程序相关的模块
import pygame
from pygame.locals import *
from sys import exit
import random
from time import sleep
from threading import Thread

pygame.init()

# 生成窗口以及窗口标题
screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Little Case")

# 加载并转换图片
tree = pygame.image.load(tree_name).convert()
apple = pygame.image.load(apple_name).convert_alpha()
clock=pygame.time.Clock()

x = 50
y = 0
z = 1

# 加载以及渲染字体
my_font = pygame.font.SysFont("arial", 16)
text_surface = my_font.render(("%d apple" % (z)), True, (0, 0, 255))


def bliti():
    global x, y, z, i, text_surface
    y += 0.3
    if y > 480 + apple.get_width():
        x = random.randint(0, 500)
        y = -apple.get_width()
        z += 1
        text_surface = my_font.render(("%d apples" % z), True, (0, 0, 255))

    screen.blit(tree, (0, 0))
    screen.blit(text_surface, (620 - text_surface.get_width(), text_surface.get_height()))
    screen.blit(apple, (x, y))


# 主循环
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.quit()
            exit()

    bliti()
    clock.tick(100)

    pygame.display.update()
