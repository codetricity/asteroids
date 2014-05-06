__author__ = 'Craig'
import pygame

class Draw():
    def __init__(self):
        self.menu_bar = pygame.Surface((600, 100))
        self.GREEN = (0, 200, 0)
        self.menu_bar_indent = 100
        self.left = pygame.Surface((100, 100))
        self.left_pos = pygame.Rect(self.menu_bar_indent, 500, 100, 100)
        pygame.draw.polygon(self.left, self.GREEN, [(95, 5), (5, 50), (95, 95) ], 2)

        self.right = pygame.Surface((100, 100))
        self.right_pos = pygame.Rect(self.menu_bar_indent + 450, 500, 100, 100)
        pygame.draw.polygon(self.right, self.GREEN, [(5,5), (95, 50), (5, 95)], 2)

        self.thrust = pygame.Surface((100, 100))
        self.thrust_pos = pygame.Rect(self.menu_bar_indent + 150, 500, 100, 100)
        pygame.draw.polygon(self.thrust, self.GREEN, [(5, 95), (50, 5), (95, 95)], 2)

        self.fire = pygame.Surface((100, 100))
        self.fire_pos = pygame.Rect(self.menu_bar_indent + 300, 500, 100, 100)
        pygame.draw.circle(self.fire, self.GREEN, (50, 50), 48, 2)

        self.menu_bar.blit(self.left, (0,0))
        self.menu_bar.blit(self.thrust, (150, 0))
        self.menu_bar.blit(self.fire, (300, 0))
        self.menu_bar.blit(self.right, (450, 0))



    def update(self):
        pass


