# 12-2 游戏角色 找一副你喜欢的游戏角色位图图像或将一副图片转换为位图。创建一个类，将该角色绘制到屏幕中央，并将该图像的背景色设置为屏幕背景色，或者将屏幕背景色设置为该图像的背景色。

import sys
import pygame

class Chara:

    def __init__(self, show_my_chara):
        self.screen = show_my_chara.screen
        self.screen_rect = show_my_chara.screen.get_rect()

        self.image = pygame.image.load('my_chara.png')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
    def blitme(self):
        self.screen.blit(self.image, self.rect)

class Show_My_Chara:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 720))
        pygame.display.set_caption('Show my character!')

        self.chara = Chara(self)
        self.bg_color = (230, 230, 230)

    def run_my_show(self):

        while True:
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.chara.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    show_my_chara = Show_My_Chara()
    show_my_chara.run_my_show()