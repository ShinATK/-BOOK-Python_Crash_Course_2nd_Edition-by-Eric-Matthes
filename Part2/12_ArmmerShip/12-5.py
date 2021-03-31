# 12-5 按键 创建一个程序，它显示一个空屏幕，在事件循环中，每当检测到pygame.KEYDOWN事件时都打印属性event.key。运行这个程序并按各种键，看看那Pygame如何响应

import pygame
import sys

class Show_my_pressed:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Show!")
        self.bg_color = (230, 230, 230)

    def run_my_screen(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    # 显示对应按键的键值
                    print(event.key)
                    # 显示对应按键的名称
                    # print(event.unicode)
            self.screen.fill(self.bg_color)
            pygame.display.flip()

if __name__ == '__main__':

    my_screen = Show_my_pressed()
    my_screen.run_my_screen()

