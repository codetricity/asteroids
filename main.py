import pygame, sys
import math
import random
from pygame.locals import *



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


        

        


pygame.init()


RED = ((255, 0, 0))
GREEN = ((0, 255, 0))
ORANGE = ((254, 158, 27))
center = [400, 300]
size = 10
angle = 0
WHITE = ((255, 255, 255))
radius = 50

screen_size = (800, 600)
windowSurface = pygame.display.set_mode(screen_size)


clock = pygame.time.Clock()
FPS = 30

forward = False
fume = False

direction = "stop"
fire = False
bullet_group = pygame.sprite.Group()


rock_group = pygame.sprite.Group()
rock = Rock()
rock_group.add(rock)
rock_start = pygame.time.get_ticks()
rock_delay = 1500

score = Score()

ship_min_brake = 8
ship_speed_brake = ship_min_brake


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                direction = "right"
            if event.key == K_LEFT:
                direction = "left"
            if event.key == K_s:
                radius = radius - 10
            if event.key == K_l:
                radius = radius + 10
            if event.key == K_UP:
                forward = True
                thurst_start = pygame.time.get_ticks()
                ship_speed_brake = ship_min_brake
                fume = True
            if event.key == K_SPACE:
                fire = True
        if event.type == KEYUP:
            if event.key == K_UP:
                # forward = False
                fume = False
            if event.key == K_RIGHT:
                direction = "stop"
            if event.key == K_LEFT:
                direction = "stop"
            
    
    radian_angle = math.radians(angle)
    length_x = math.cos(radian_angle) * radius
    length_y = math.sin(radian_angle) * radius
    
    x = int(center[0] + length_x)
    y = int(center[1] - length_y)
            
####
    angle_2 = math.radians(angle + 120)
    length_x_2 = math.cos(angle_2) * radius
    length_y_2 = math.sin(angle_2) * radius
    x_2 = int(center[0] + length_x_2)
    y_2 = int(center[1] - length_y_2)
    
####
    angle_3 = math.radians(angle + 240)
    length_x_3 = math.cos(angle_3) * radius
    length_y_3 = math.sin(angle_3) * radius
    x_3 = int(center[0] + length_x_3)
    y_3 = int(center[1] - length_y_3)
    
###
    length_x_motion = math.cos(radian_angle) * radius / ship_speed_brake
    length_y_motion = math.sin(radian_angle) * radius / ship_speed_brake
    x_motion = int(center[0] + length_x_motion)
    y_motion = int(center[1] - length_y_motion)
     
###
    angle_4 = math.radians(angle + 180)
    length_x_4 = math.cos(angle_4) * radius
    length_y_4 = math.sin(angle_4) * radius
    x_4 = int(center[0] + length_x_4)
    y_4 = int(center[1] - length_y_4)
    
    thrust_x = (x_2 + x_3) / 2
    thrust_y = (y_2 + y_3) / 2
    

    windowSurface.fill((0, 0, 0))
    
    #pygame.draw.circle(windowSurface, RED, center, size)
    #pygame.draw.circle(windowSurface, GREEN, (x, y), size)
    #pygame.draw.circle(windowSurface, GREEN, (x_2, y_2), size)
    #pygame.draw.circle(windowSurface, GREEN, (x_3, y_3), size)
    #

    score.update()
    windowSurface.blit(score.image, (10, 10))
    
    rock_group.update()
    rock_current_time =  pygame.time.get_ticks() - rock_start
    if rock_current_time > rock_delay:
        rock_group.add(Rock())
        rock_start = pygame.time.get_ticks()
    rock_group.draw(windowSurface)
    
    
    pygame.draw.line(windowSurface, WHITE, (x,y), (x_2, y_2))
    pygame.draw.line(windowSurface, WHITE, (x_2, y_2), (center))
    pygame.draw.line(windowSurface, WHITE, (center), (x_3, y_3))
    pygame.draw.line(windowSurface, WHITE, (x_3, y_3), (x, y))
    
    ship_rect = pygame.Rect(0, 0, radius * 1.5, radius * 1.5)
    ship_rect.center = center


    
    pygame.draw.circle(windowSurface, RED, (x_motion, y_motion), size / 2)

    
    bullet_group.update()
    bullet_group.draw(windowSurface)
    
    
    
    
    if angle >= 360:
        angle = 0
    if direction == "left":
        angle = angle + 3
    if direction == "right":
        angle = angle - 3
        
    if forward == True:
        thrust_elapsed = pygame.time.get_ticks() - thurst_start
        if thrust_elapsed < 10000:
            center = [x_motion, y_motion]
            if thrust_elapsed > 3000:
                ship_speed_brake = 14
            if thrust_elapsed > 7000:
                ship_speed_brake = 20
        
    if fume == True:
        pygame.draw.circle(windowSurface, ORANGE, (thrust_x, thrust_y), size, 2)
        
    if center[0] > screen_size[0]:
        center[0] = 0
    if center[0] < 0:
        center[0] = screen_size[0]
    if center[1] > screen_size[1]:
        center[1] = 0
    if center[1] < 0:
        center[1] = screen_size[1]
        
    if fire == True:
        bullet = Bullet(radian_angle, center)
        bullet_group.add(bullet)
        fire = False
        
    for bullet in bullet_group:
        if bullet.pass_right:
            if bullet.rect.centerx + 200 > bullet.orig_center[0]:
                bullet_group.remove(bullet)
        elif bullet.pass_left:
            if bullet.rect.centerx - 200 < bullet.orig_center[0]:
                bullet_group.remove(bullet)
        if bullet.pass_down:
            if bullet.rect.centery + 200 > bullet.orig_center[1]:
                bullet_group.remove(bullet)
        elif bullet.pass_up:
            if bullet.rect.centery - 200 < bullet.orig_center[1]:
                bullet_group.remove(bullet)

    # rocks_hit = pygame.sprite.groupcollide(bullet_group, rock_group, True, True)
    # if len(rocks_hit) > 0:
    #     score.points = score.points + len(rocks_hit)
        

    for rock in rock_group:
        if ship_rect.colliderect(rock.rect):
            windowSurface.fill((255, 0, 0))
            score.points = 0
        for bullet in bullet_group:
            if bullet.rect.colliderect(rock.rect):
                bullet_group.remove(bullet)
                score.points = score.points + 1
                if rock.size > 20:
                    new_rock = Rock(rock.size/2)
                    new_rock.rect.center = rock.rect.center
                    rock_group.add(new_rock)
                    new_rock = Rock(rock.size/2)
                    new_rock.rect.center = rock.rect.center
                    rock_group.add(new_rock)

                rock_group.remove(rock)



    
    clock.tick(FPS)
    pygame.display.update()
    
