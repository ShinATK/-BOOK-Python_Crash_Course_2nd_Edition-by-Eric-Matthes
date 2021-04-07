# 12-1 蓝色天空 创建一个背景为蓝色的Pygame窗口

import pygame
import sys

class My_Screen:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 720))
        pygame.display.set_caption("My screen's bg color setting!")
        self.bg_color = (0, 0, 255)

    def run_my_screen(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()

if __name__ == '__main__':

    my_screen = My_Screen()
    my_screen.run_my_screen()

