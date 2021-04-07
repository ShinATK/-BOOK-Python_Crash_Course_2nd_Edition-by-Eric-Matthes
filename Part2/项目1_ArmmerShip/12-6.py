# 12-6 侧面设计 编写一个游戏，将一艘飞船放在屏幕左侧，并允许玩家上下移动飞船。在玩家按空格键时，让飞船发射一颗在屏幕中向右飞行的子弹，并在子弹从屏幕中消失后删除

import sys
import pygame
from pygame.sprite import Sprite

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
        """在指定的位置绘制"""
        self.screen.blit(self.image, self.rect)

class Bullet(Sprite):
    """管理所发射子弹的类"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 在（0，0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.midright = ai_game.chara.rect.midright

        #存储用小数表示的子弹的位置
        self.x = float(self.rect.x)

    def update(self):
        """向上移动子弹。"""
        # 更新表示子弹位置的小数值
        self.x += self.bullet_speed
        # 更新表示子弹的rect的位置
        self.rect.x = self.x

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)

class Move_My_Chara:

    def __init__(self):
        pygame.init()
        self.screen_size = (1200, 720)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption('Move my character!')
        self.bullets = pygame.sprite.Group()

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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

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

    def _fire_bullet(self):
        """创建一个子弹，并将其加入编组bullets中"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """更新子弹的位置并删除消失的子弹"""
        # 更新子弹的位置
        self.bullets.update()
        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.right > self.screen_size[0]:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        # 每次循环都重绘制屏幕
        self.screen.fill(self.bg_color)
        self.chara.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def run_my_chara(self):
        """开始游戏的主循环。"""
        while True:
            self._check_events()
            self.chara.upadate()
            self.bullets.update()
            self._update_bullets()
            self._update_screen()

if __name__ == '__main__':
    move_my_chara = Move_My_Chara()
    move_my_chara.run_my_chara()