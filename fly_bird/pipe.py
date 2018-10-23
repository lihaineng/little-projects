
"""
因为地图要移动所以有属性有方法因而将地图看做一个类
"""
import pygame
import random

# 设置全局常量
WIN_X = 800
WIN_Y = 712


class Pipe(object):
    def __init__(self, win, temp):
        pygame.init()
        self.window = win
        self.img1 = pygame.image.load("imgs/pipe1.png")
        self.img2 = pygame.image.load("imgs/pipe2.png")
        self.land_rect1 = self.img1.get_rect()
        self.land_rect2 = self.img1.get_rect()
        self.temp = temp
        num = random.randint(100, 220)
        length = random.randint(80, 120)
        self.land_rect1[0] = 280*temp -self.land_rect1[2] - 560
        self.land_rect2[0] = 280*temp -self.land_rect2[2] - 560
        self.land_rect2[1] -= num
        self.land_rect1[1] = self.land_rect1[3] - num + length


    def blited(self):
        self.window.blit(self.img2, (self.land_rect2[0], self.land_rect2[1]))
        self.window.blit(self.img1, (self.land_rect1[0], self.land_rect1[1]))

    def reserve(self):
        self.img1 = pygame.image.load("imgs/pipe1.png")
        self.img2 = pygame.image.load("imgs/pipe2.png")
        self.land_rect1 = self.img1.get_rect()
        self.land_rect2 = self.img1.get_rect()
        num = random.randint(50, 220)
        length = random.randint(80, 120)
        self.land_rect1[0] = 840
        self.land_rect2[0] = 840
        self.land_rect2[1] -= num
        self.land_rect1[1] = self.land_rect1[3] - num + length

    def move(self):
        if self.land_rect1[0] > -280:
            self.land_rect1[0] -= 2
        else:
            self.reserve()
        if self.land_rect2[0] > -280:
            self.land_rect2[0] -= 2
        else:
            self.reserve()

