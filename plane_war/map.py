
"""
因为地图要移动所以有属性有方法因而将地图看做一个类
"""
import pygame
import random

WIN_X = 512
WIN_Y = 768

class Map(object):
    def __init__(self, win):
        pygame.init()
        self.window = win
        self.num = random.randint(1, 5)     # 通过随机数产生不一样的地图背景
        self.img = pygame.image.load("res/img_bg_level_%s.jpg" % self.num)
        self.map_y1 = 0
        self.map_y2 = -WIN_Y

    def blited(self):
        self.window.blit(self.img, (0, self.map_y1))
        self.window.blit(self.img, (0, self.map_y2))

    def move(self):
        if self.map_y1 >= WIN_Y:
            self.map_y1 = -WIN_Y
        else:
            self.map_y1 += 1
        if self.map_y2 >= WIN_Y:
            self.map_y2 = -WIN_Y
        else:
            self.map_y2 += 1

