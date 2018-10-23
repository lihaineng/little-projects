
"""
因为鸟有属性有方法因而将鸟看做一个类
"""
import pygame

# 设置全局常量
import sys

WIN_X = 800
WIN_Y = 712


class Bird(object):
    def __init__(self, win):
        pygame.init()
        self.window = win
        self.flag = False
        self.img = pygame.image.load("imgs/bird1.png")
        self.bird_rect = self.img.get_rect()
        self.bird_rect[0] = 50
        self.bird_rect[1] = WIN_Y / 2

    def blited(self):
        self.window.blit(self.img, (self.bird_rect[0], self.bird_rect[1]))

    def move(self):
        # 获得当前键盘所有按键的状态(按下，没有按下)，返回bool元组
        # 注意左右上下用4个if不用elif是因为其实有时两个方向是可以同时操作的(比如上左)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
            if self.bird_rect[1] > 0:
                self.bird_rect[1] -= 8
        if pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
                self.bird_rect[1] += 2
        if self.bird_rect[0] < WIN_X:
            self.bird_rect[0] += 1
        else:
            self.bird_rect[0] = 0
        if self.bird_rect[1] < WIN_Y - 112:
            self.bird_rect[1] += 1
        else:
            self.flag = True



