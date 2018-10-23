"""
整个游戏步骤:1 把游戏看做一个对象,面向对象搭好整体框架    2 初始化pygame库,设计好游戏窗口(由于这些都是在创建游戏对象时开始的所以放在__init__函数中)  3 绘制移动背景(map)  4 绘制英雄飞机(hero)   5 绘制子弹(bullet)
"""
import pygame
import pygame.font

import sys

from enemy import Enemy
from hero import Hero
from map import Map

# 设定游戏常量
from start import Start

WIN_X = 512
WIN_Y = 768

# 面向对象编程将游戏看做一个类,他有属性和各种方法
class Game(object):
    def __init__(self):
        pygame.init()   # 初始化pygame库
        self.score = 0
        self.window = pygame.display.set_mode([WIN_X, WIN_Y])  # 绘制游戏窗口(为了以后修改将窗口数据用常量)
        pygame.display.set_caption("飞机大战")  # 设置窗口标题
        # 设计游戏图标步骤1 加载图片(凡是涉及到添加图形,音乐的都要先把内容加载都内存)  2 调用set_icon()
        img = pygame.image.load("res/app.ico")  # 因为这个img只在__init__函数里面使用故不加self
        pygame.display.set_icon(img)
        self.map = Map(self.window)
        self.hero = Hero(self.window)
        self.enemys_list = [Enemy(self.window) for _ in range(4)]
        pygame.mixer.music.load("res/bg2.ogg")  # 加载背景音乐
        pygame.mixer.music.play(-1)      # 循环播放背景音乐
        self.f = pygame.font.SysFont("宋体", 36)

    def inputOrder(self):
        # 获得所有事件的列表
        event_list = pygame.event.get()
        for event in event_list:
            # 1. 鼠标点击关闭窗口事件
            if event.type == pygame.QUIT:
                print("关闭了窗口")
                sys.exit()
                # 2. 键盘按下事件
            if event.type == pygame.KEYDOWN:   # 现有键盘按下时间才能对按下那个键进行判断,这个容易忘
                # 判断用户按下的键是否是空格键
                if event.key == pygame.K_SPACE:
                    self.hero.shot()

    def is_bullet_hit_enemy(self):
        for i in self.enemys_list:
            for j in self.hero.bullets_list:
                if pygame.Rect.colliderect(i.rect, j.rect):
                    self.score += 1
                    i.reserve()

    def is_hero_hit_enemy(self):
        for i in self.enemys_list:
            if pygame.Rect.colliderect(i.rect, self.hero.rect):
                return True
            else:
                return False

    def move(self):
        self.map.move()
        self.hero.move()
        for i in self.enemys_list:
            i.move()
        self.is_bullet_hit_enemy()

    def blited(self):
        self.text_surface = self.f.render("SCORE: %s" % self.score, True, (0, 0, 255))
        self.map.blited()
        self.hero.blited()
        self.window.blit(self.text_surface, (340, 10))
        for i in self.enemys_list:
            i.blited()

    @staticmethod       # 因为图片更新方法不需要任何参数所以设置成静态方法
    def update():
        pygame.display.update()

    def run(self):
        # 游戏运行时主要有下面四件事
        self.inputOrder()     #1 接受外界输入指令
        self.move()         #2 接受命令后导致图片移动
        if self.is_hero_hit_enemy():      # 如果飞机被撞结束游戏
            self.is_over()
        self.blited()       #3 图片重新绘制
        self.update()       #4 图片更新

    def is_over(self):
        pygame.mixer.music.stop()  # 停止背景音乐
        boom_sound = pygame.mixer.Sound("res/gameover.wav")  # 加载音效
        boom_sound.play()  # 播放音效
        while True:
            event_list = pygame.event.get()
            for event in event_list:
                # 1. 鼠标点击关闭窗口事件
                if event.type == pygame.QUIT:
                    print("关闭了窗口")
                    sys.exit()

    def main(self):
        while True:
            self.run()

if __name__ == "__main__":  # 防止下面的代码被导包
# 进分析游戏进程如下:游戏开始game.start,游戏运行game.run,游戏结束game.over
    start = Start()
    my_game = Game()   # 创建一个游戏类
    my_game.main()
