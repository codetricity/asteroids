__author__ = 'Craig'

import pygame
import json


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


    def load(self):
        self.scorefile = open('highscore.json', 'r+')
        self.scoredata = self.scorefile.read()

        try:
            self.scoredata = int(self.scoredata)
        except:
            self.scoredata = 0


    def write(self):

        if self.points > self.scoredata:
            self.scorefile.seek(0)
            self.scorefile.write(str(self.points))
        self.scorefile.close()

    def screen(self, surface):
        self.load()
        self.write()
        self.player_score = "Your score: {}".format(self.points)
        self.p_score_surface = self.score_font.render(self.player_score, True, self.WHITE)
        self.h_score = "High score: {}".format(self.scoredata)
        self.h_score_surface = self.score_font.render(self.h_score, True, self.WHITE)
        while True:
            event = pygame.event.poll()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    break
            surface.fill((0,0,0))
            surface.blit(self.p_score_surface, (100, 100))
            surface.blit(self.h_score_surface, (100, 200))
            pygame.display.update()