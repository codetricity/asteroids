import pygame
import math
import random

class Rock(pygame.sprite.Sprite):
    def __init__(self, size = 100):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.speed = 1
        self.direction = random.choice(["right", "left", "up", "down", "rightup",
                                        "rightdown", "leftup", "leftdown"])
        self.center = [self.size/2, self.size/2]
        self.screencenter = [800/2, 600/2]
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0,0,0))

        self.safe_zone = 150
        self.draw()
        self.place()

    def draw(self):
        self.rect = pygame.draw.circle(self.image, (0, 255, 0), self.center,
                                       self.size/2, 1)
        pygame.draw.circle(self.image, (200, 15, 0), self.center,
                           int(.8 * self.size/2), 1)
        pygame.draw.circle(self.image, (200, 15, 100), self.center,
                           int(.5 * self.size/2), 1)

    def place(self):
        self.rect.center = (random.randrange(0, 800),
                            (random.randrange(0, 600)))
        if (self.rect.centerx > self.screencenter[0]  - self.safe_zone
            and self.rect.centerx < self.screencenter[0] + self.safe_zone
            and self.rect.centery > self.screencenter[1] - self.safe_zone
            and self.rect.centery < self.screencenter[1] + self.safe_zone):
            self.place()

    def update(self):
        if self.direction == "right":
            self.rect.centerx += self.speed
        elif self.direction == "left":
            self.rect.centerx -= self.speed
        elif self.direction == "up":
            self.rect.centery -= self.speed
        elif self.direction == "down":
            self.rect.centery += self.speed
        elif self.direction == "rightdown":
            self.rect.centery += self.speed
            self.rect.centerx += self.speed
        elif self.direction == "rightup":
            self.rect.centery -= self.speed
            self.rect.centerx += self.speed
        elif self.direction == "leftdown":
            self.rect.centery += self.speed
            self.rect.centerx -= self.speed
        elif self.direction == "leftup":
            self.rect.centery -= self.speed
            self.rect.centerx -= self.speed

        if self.rect.centerx > 800:
            self.rect.centerx = 0
        if self.rect.centerx < 0:
            self.rect.centerx = 800
        if self.rect.centery > 600:
            self.rect.centery = 0
        if self.rect.centery < 0:
            self.rect.centery = 600

