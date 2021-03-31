# 12-4 火箭 编写一个游戏，它在屏幕中央显示一个火箭，而玩家可以使用四个方向键上下左右移动火箭。请务必确保火箭不会移动到屏幕外面。

import sys
import pygame

class Chara:

    def __init__(self, move_my_chara):
        self.screen = move_my_chara.screen
        self.screen_size = move_my_chara.screen_size
        self.screen_rect = move_my_chara.screen.get_rect()

        self.image = pygame.image.load('my_chara.png')
        self.rect = self.image.get_rect()

        # 图片初始位置在窗口正中央
        self.rect.center = self.screen_rect.center

        self.moving_speed = 1

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def upadate(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船而不是rect对象的x值
        if self.moving_right and self.rect.right < self.screen_size[0]:
            self.x += self.moving_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.moving_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.moving_speed
        if self.moving_down and self.rect.bottom < self.screen_size[1]:
            self.y += self.moving_speed

        # 根据self.x更细rect对象
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """在指定的位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

class Move_My_Chara:

    def __init__(self):
        pygame.init()
        self.screen_size = (1200, 720)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption('Move my character!')

        self.chara = Chara(self)
        self.bg_color = (230, 230, 230)

    def _check_events(self):
        """响应按键和鼠标事件"""
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 监测到关闭游戏窗口时，游戏将退出
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """响应按键"""
        if event.key == pygame.K_RIGHT:
            self.chara.moving_right = True
            # self.chara.moving_left = False
            # self.chara.moving_up = False
            # self.chara.moving_down = False
        elif event.key == pygame.K_LEFT:
            # self.chara.moving_right = False
            self.chara.moving_left = True
            # self.chara.moving_up = False
            # self.chara.moving_down = False
        elif event.key == pygame.K_UP:
            # self.chara.moving_right = False
            # self.chara.moving_left = False
            self.chara.moving_up = True
            # self.chara.moving_down = False
        elif event.key == pygame.K_DOWN:
            # self.chara.moving_right = False
            # self.chara.moving_left = False
            # self.chara.moving_up = False
            self.chara.moving_down = True

    def _check_keyup_events(self, event):
        """响应松开"""
        if event.key == pygame.K_RIGHT:
            self.chara.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.chara.moving_left = False
        elif event.key == pygame.K_UP:
            self.chara.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.chara.moving_down = False
        elif event.key == pygame.K_q:
            # 按q键退出
            sys.exit()

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        # 每次循环都重绘制屏幕
        self.screen.fill(self.bg_color)
        self.chara.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def run_my_chara(self):
        """开始游戏的主循环。"""
        while True:
            self._check_events()
            self.chara.upadate()
            self._update_screen()

if __name__ == '__main__':
    move_my_chara = Move_My_Chara()
    move_my_chara.run_my_chara()