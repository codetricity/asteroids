import pygame
import math


class Bullet(pygame.sprite.Sprite):
    def __init__(self, radian_angle, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((4, 4))
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, (255, 255, 255), (2, 2), 2)
        self.radian_angle = radian_angle
        self.radius = 70
        self.orig_center = center
        self.bullet_center = [center[0], center[1]]
        self.pass_right = False
        self.pass_left = False
        self.pass_up = False
        self.pass_down = False


    def update(self):
        length_x_fire = math.cos(self.radian_angle) * self.radius
        length_y_fire = math.sin(self.radian_angle) * self.radius
        x_fire = int(self.bullet_center[0] + length_x_fire)
        y_fire = int(self.bullet_center[1] - length_y_fire)
        self.rect.center = [x_fire, y_fire],

        self.radius = self.radius + 13

        if self.rect.centerx > 800:
            self.bullet_center[0] = 0
            self.rect.centerx = self.bullet_center[0]
            self.radius = 0
            self.pass_right = True

        elif self.rect.centerx < 0:
            self.bullet_center[0] = 800
            self.rect.centerx = self.bullet_center[0]
            self.radius = 0
            self.pass_left = True

        if self.rect.centery < 0:
            self.bullet_center[1] = 600
            self.rect.centery = self.bullet_center[1]
            self.radius = 0
            self.pass_up = True

        elif self.rect.centery > 600:
            self.bullet_center[1] = 0
            self.rect.centery = self.bullet_center[1]
            self.radius = 0
            self.pass_down = True

