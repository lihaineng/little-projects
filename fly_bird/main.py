"""
小鸟飞翔游戏:分析主要有三个对象游戏对象,小鸟对象,管道对象
"""
import pygame
import sys

# 设置全局常量
from bird import Bird
from land import Land
from map import Map
from pipe import Pipe

WIN_X = 800
WIN_Y = 712


class Game(object):
    def __init__(self):         # 初始化
        pygame.init()  # 初始化pygam
        self.window = pygame.display.set_mode([WIN_X, WIN_Y])  # 绘制游戏窗口(为了以后修改将窗口数据用常量)
        pygame.display.set_caption("飞翔的小鸟")  # 设置窗口标题
        # 设计游戏图标步骤1 加载图片(凡是涉及到添加图形,音乐的都要先把内容加载都内存)  2 调用set_icon()
        img = pygame.image.load("imgs/icon.gif")  # 因为这个img只在__init__函数里面使用故不加self
        pygame.display.set_icon(img)
        self.map = Map(self.window)
        self.bird = Bird(self.window)
        self.land_list = [Land(self.window, i) for i in range(1, 4)]
        self.pipe_list = [Pipe(self.window, i) for i in range(1, 5)]
        # pygame.mixer.music.load("res/bg2.ogg")  # 加载背景音乐
        # pygame.mixer.music.play(-1)  # 循环播放背景音乐

    def inputOrder(self):       # 接受输入指令
        # 获得所有事件的列表
        event_list = pygame.event.get()
        for event in event_list:
            # 1. 鼠标点击关闭窗口事件
            if event.type == pygame.QUIT:
                print("关闭了窗口")
                sys.exit()

    def move(self):     # 对象移动
        self.map.move()
        self.bird.move()
        for i in self.pipe_list:
            i.move()

    def Draw(self):             # 画图
        self.map.blited()
        self.bird.blited()
        for i in self.pipe_list:
            i.blited()
        for i in self.land_list:
            i.blited()

    @staticmethod  # 因为图片更新方法不需要任何参数所以设置成静态方法
    def update():
        pygame.display.update()


    def is_over(self):
        # pygame.mixer.music.stop()  # 停止背景音乐
        # boom_sound = pygame.mixer.Sound("res/gameover.wav")  # 加载音效
        # boom_sound.play()  # 播放音效
        while True:
            event_list = pygame.event.get()
            for event in event_list:
                # 1. 鼠标点击关闭窗口事件
                if event.type == pygame.QUIT:
                    print("关闭了窗口")
                    sys.exit()

    def is_bird_hit_pipe(self):
        for i in self.pipe_list:
            if pygame.Rect.colliderect(i.land_rect1, self.bird.bird_rect):
                return True
            elif pygame.Rect.colliderect(i.land_rect2, self.bird.bird_rect):
                return True
            else:
                return False


    def main(self):         # 分析游戏主要有以下属性:初始化,接受输入事件,对象移动,画图,更新,记分
        while True:
            # 游戏运行时主要有下面四件事
            if self.bird.flag or self.is_bird_hit_pipe():
                self.is_over()
            self.inputOrder()  # 1 接受外界输入指令
            self.move()  # 2 接受命令后导致图片移动
            self.Draw()  # 3 图片重新绘制
            self.update()  # 4 图片更新


if __name__ == "__main__":      # 防止模块导入时被调用
    my_game = Game()
    my_game.main()
