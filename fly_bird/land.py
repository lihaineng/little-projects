
"""
因为地图要移动所以有属性有方法因而将地图看做一个类
"""
import pygame

# 设置全局常量
WIN_X = 800
WIN_Y = 712


class Land(object):
    def __init__(self, win, num):
        pygame.init()
        self.window = win
        self.img = pygame.image.load("imgs/land.png")
        self.num = num
        self.land_rect = self.img.get_rect()
        self.land_rect[0] = 336*self.num - 336
        self.land_rect[1] = WIN_Y - self.land_rect[3]

    def blited(self):
        self.window.blit(self.img, (self.land_rect[0], self.land_rect[1]))

