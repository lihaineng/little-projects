
"""
因为地图要移动所以有属性有方法因而将地图看做一个类
"""
import pygame

# 设置全局常量
WIN_X = 800
WIN_Y = 712


class Map(object):
    def __init__(self, win):
        pygame.init()
        self.window = win
        self.img = pygame.image.load("imgs/sky.png")
        self.map_x1 = 0
        self.map_x2 = WIN_X

    def blited(self):
        self.window.blit(self.img, (self.map_x1, 0))
        self.window.blit(self.img, (self.map_x2, 0))

    def move(self):
        if self.map_x1 == -WIN_X:
            self.map_x1 = WIN_X
        else:
            self.map_x1 -= 2
        if self.map_x2 == -WIN_X:
            self.map_x2 = WIN_X
        else:
            self.map_x2 -= 2


