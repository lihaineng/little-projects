# -*- coding: utf-8 -*-
import pygame
import sys

WIN_X = 512
WIN_Y = 768

class Start(object):
    def __init__(self):
        self.flag = False
        pygame.init()  # 初始化pygame库
        pygame.mixer.music.load("res/bg2.ogg")  # 加载背景音乐
        pygame.mixer.music.play(-1)  # 循环播放背景音乐
        f = pygame.font.SysFont("宋体", 36)
        text_surface1 = f.render("Welcome To My Game", True, (0, 0, 255))
        text_surface2 = f.render("Please Enter SPACE To The Game ", True, (0, 0, 255))
        while True:
            window = pygame.display.set_mode([WIN_X, WIN_Y])  # 绘制游戏窗口(为了以后修改将窗口数据用常量)
            pygame.display.set_caption("飞机大战")  # 设置窗口标题
            # 设计游戏图标步骤1 加载图片(凡是涉及到添加图形,音乐的都要先把内容加载都内存)  2 调用set_icon()
            img = pygame.image.load("res/app.ico")  # 因为这个img只在__init__函数里面使用故不加self
            pygame.display.set_icon(img)
            img = pygame.image.load("res/img_bg_level_1.jpg")
            window.blit(img, (0, 0))
            window.blit(text_surface1, (100, 300))
            window.blit(text_surface2, (45, 350))
            pygame.display.update()
            event_list = pygame.event.get()
            for event in event_list:
                # 1. 鼠标点击关闭窗口事件
                if event.type == pygame.QUIT:
                    print("关闭了窗口")
                    sys.exit()
                    # 2. 键盘按下事件
                if event.type == pygame.KEYDOWN:  # 现有键盘按下时间才能对按下那个键进行判断,这个容易忘
                    # 判断用户按下的键是否是空格键
                    if event.key == pygame.K_SPACE:
                        self.flag = True
            if self.flag:
                break
