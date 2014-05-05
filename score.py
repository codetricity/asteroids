__author__ = 'Craig'

import pygame


class Score():
    def __init__(self):
        self.WHITE = (200, 200, 200)
        self.points = 0
        self.score_font = pygame.font.Font("fnt/animeace2_reg.ttf", 20)
        self.score_text = "SCORE: "
        self.update()


    def update(self):
        text = self.score_text + str(self.points)
        self.image = self.score_font.render(text, True,
                                                    self.WHITE)
