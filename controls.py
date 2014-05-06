__author__ = 'Craig'
import pygame

class Draw():
    def __init__(self, screensize):
        self.screensize = screensize
        self.height = 250
        self.width = 600
        self.menu_bar = pygame.Surface((self.width, self.height))
        self.GREEN = (0, 200, 0)
        self.LIGHTBLUE = (175, 238, 238)
        self.menu_bar_indent = 100
        self.posx=[0, 150, 300, 400]
        self.posx_upper = 75
        self.posy_upper = self.screensize[1] - self.height
        self.posy_lower = self.screensize[1] - 100



        self.left = pygame.Surface((100, 100))
        self.left_pos = pygame.Rect(self.menu_bar_indent, self.posy_lower, 100, 100)
        pygame.draw.polygon(self.left, self.LIGHTBLUE, [(95, 5), (5, 50), (95, 95) ], 2)

        self.right = pygame.Surface((100, 100))
        self.right_pos = pygame.Rect(self.menu_bar_indent + self.posx[1], self.posy_lower, 100, 100)
        pygame.draw.polygon(self.right, self.LIGHTBLUE, [(5,5), (95, 50), (5, 95)], 2)

        self.thrust = pygame.Surface((100, 100))
        self.thrust_pos = pygame.Rect(self.menu_bar_indent + self.posx_upper,
                                      self.posy_upper, 100, 100)
        pygame.draw.polygon(self.thrust, self.LIGHTBLUE, [(5, 95), (50, 5), (95, 95)], 2)

        self.fire = pygame.Surface((200, 200))
        self.fire_pos = pygame.Rect(self.menu_bar_indent + self.posx[3], self.posy_upper, 200, 200)
        pygame.draw.circle(self.fire, self.LIGHTBLUE, (100, 100), 98, 2)

        self.menu_bar.blit(self.left, (0,150))
        self.menu_bar.blit(self.right, (self.posx[1], 150))
        self.menu_bar.blit(self.thrust, (self.posx_upper, 0))
        self.menu_bar.blit(self.fire, (self.posx[3], 0))




    def update(self):
        pass


