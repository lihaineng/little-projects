
"""
因为子弹要移动所以有属性有方法因而将地图看做一个类
"""
import pygame
import random

WIN_X = 512
WIN_Y = 768

class Bullet(object):
    def __init__(self, win, plane_x, plane_y, plane_w):
        pygame.init()
        self.window = win
        self.num = random.randint(1,2)     # 通过随机数产生不一样的地图背景
        self.img = pygame.image.load("res/hero_bullet_%s.png" % self.num)
        self.rect = self.img.get_rect()
        self.x = plane_x         # 因为子弹位置跟飞机位置有关所以必须传参
        self.y = plane_y
        self.w = plane_w
        self.rect[0] = self.x + self.w/2 - self.rect[2]/2
        self.rect[1] = self.y - self.rect[3] + 10

    def blited(self):
        self.window.blit(self.img, (self.rect[0], self.rect[1]))

    def move(self):
        if self.rect[1] > -10:
            self.rect[1] -= 2.5

