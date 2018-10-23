import pygame
import sys
pygame.init()
# # 创建敌机的定时器常量
ENEMY_EVENT = pygame.USEREVENT

class Enemy(object):
    def __init__(self):
        # 初始化
        pygame.time.set_timer(ENEMY_EVENT, 1000)

    def blited(self):
        while True:
            event_list = pygame.event.get()  # 不管长短事件都要这个函数
            for event in event_list:
                print(1)
                # 1. 鼠标点击关闭窗口事件
                if event.type == pygame.QUIT:
                    print("关闭了窗口")
                    sys.exit()
                print(4)
                if event.type == ENEMY_EVENT:
                    print(3)
E = Enemy()
E.blited()