
"""
因为飞机要移动所以有属性有方法因而将地图看做一个类
"""
import pygame
import random

from bullet import Bullet

WIN_X = 512
WIN_Y = 768

class Hero(object):
    def __init__(self, win):
        pygame.init()
        self.window = win
        self.num = random.randint(1, 2)     # 通过随机数产生不一样的飞机
        self.img = pygame.image.load("res/hero%s.png" % self.num)
        self.rect = self.img.get_rect()                 # 获取图片矩形
        self.rect[0] = WIN_X/2 - self.rect[2]/2
        self.rect[1] = WIN_Y - self.rect[3] - 15
        self.bullets_list = []          #  给飞机添加弹夹属性

    def blited(self):
        self.window.blit(self.img, (self.rect[0], self.rect[1])) # 图片矩形创建飞机位置方便后面求图片交集
        for i in self.bullets_list:
            i.blited()

    def shot(self):
        bullet = Bullet(self.window, self.rect[0], self.rect[1], self.rect[2])
        self.bullets_list.append(bullet)

    def move(self):
        # 获得当前键盘所有按键的状态(按下，没有按下)，返回bool元组
        # 注意左右上下用4个if不用elif是因为其实有时两个方向是可以同时操作的(比如上左)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
            if self.rect[1] > 0:
                self.rect[1] -= 2
        if pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
            if self.rect[1] < WIN_Y - self.rect[3]:
                self.rect[1] += 2
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            if self.rect[0] > 0:
                self.rect[0] -= 2
        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            if self.rect[0] < WIN_X - self.rect[2]:
                self.rect[0] += 2
        for i in self.bullets_list:
            if i.rect[1] < 0:
                self.bullets_list.remove(i)     # 一定要将超出边界的子弹一处不然列表会越来越大浪费内存
            else:
                i.move()



