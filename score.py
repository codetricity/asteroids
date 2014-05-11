__author__ = 'Craig'

import pygame
import sys
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
            self.congrats_text = "Congratulations, you have the high score!"
        else:
            self.congrats_text = "Better luck next time."
        self.scorefile.close()

    def screen(self, surface):
        self.load()
        self.write()
        self.player_score = "Your score: {}".format(self.points)
        self.p_score_surface = self.score_font.render(self.player_score, True, self.WHITE)
        self.h_score = "High score: {}".format(self.scoredata)
        self.h_score_surface = self.score_font.render(self.h_score, True, self.WHITE)
        self.congrats_surface =self.score_font.render(self.congrats_text, True, self.WHITE)

        self.play_again_surface = self.score_font.render("Play Again?", True, self.WHITE)
        self.play_again_rect = self.play_again_surface.get_rect(center = (150, 450))

        self.quit_surface = self.score_font.render("Quit", True, self.WHITE)
        self.quit_center = (450, 450)
        self.quit_rect = self.quit_surface.get_rect(center = self.quit_center)


        while True:
            event = pygame.event.poll()
            pos = pygame.mouse.get_pos()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    break
            if self.play_again_rect.collidepoint(pos):
                break
            if self.quit_rect.collidepoint(pos):
                pygame.quit()
                sys.exit()
            surface.fill((0,0,0))
            surface.blit(self.p_score_surface, (100, 100))
            surface.blit(self.h_score_surface, (100, 200))
            surface.blit(self.congrats_surface, (100, 260))
            pygame.draw.circle(surface, self.WHITE, self.play_again_rect.center, 100, 1)
            quit_rect = pygame.draw.circle(surface, self.WHITE, self.quit_center, 100, 1)
            surface.blit(self.play_again_surface, self.play_again_rect)
            surface.blit(self.quit_surface, self.quit_rect)
            pygame.display.update()