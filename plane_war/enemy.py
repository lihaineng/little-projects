"""
此页面代码只是用来对自己知识猜想进行检测检测
"""

"""
因为飞机要移动所以有属性有方法因而将地图看做一个类
"""
import pygame
import random

WIN_X = 512
WIN_Y = 768

class Enemy(object):
    def __init__(self, win):
        pygame.init()
        self.window = win
        self.num = random.randint(1, 7)     # 通过随机数产生不一样的飞机
        self.img = pygame.image.load("res/img-plane_%s.png" % self.num)
        self.rect = self.img.get_rect()                 # 获取图片矩形
        self.rect[0] = random.randint(0, WIN_X - self.rect[2])
        self.rect[1] = random.randint(-50, 50)
        self.speed = random.randint(200, 500)*0.01          # 让飞机速度不同这样看起来舒服些

    def blited(self):
        self.window.blit(self.img, (self.rect[0], self.rect[1])) # 图片矩形创建飞机位置方便后面求图片交集

    def reserve(self):
        self.num = random.randint(1, 7)  # 通过随机数产生不一样的飞机
        self.img = pygame.image.load("res/img-plane_%s.png" % self.num)
        self.rect = self.img.get_rect()  # 获取图片矩形
        self.rect[0] = random.randint(0, WIN_X - self.rect[2])
        self.rect[1] = random.randint(-50, 50)

    def move(self):
        if self.rect[1] < WIN_Y:
            self.rect[1] += self.speed
        else:
            self.reserve()


