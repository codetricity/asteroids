import pygame, sys
import math
import random
from pygame.locals import *
from bullet import *
from rock import *
from score import *
import controls

try:
    import android
except ImportError:
    android = None

if android:
    android.init()
    android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

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

controller = controls.Draw()


while True:
    if android:
        if android.check_pause():
            android.wait_for_resume()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            # if event.key == K_RIGHT:
            #     direction = "right"
            # if event.key == K_LEFT:
            #     direction = "left"
            # if event.key == K_s:
            #     radius = radius - 10
            # if event.key == K_l:
            #     radius = radius + 10
            # if event.key == K_UP:
            #     forward = True
            #     thrust_start = pygame.time.get_ticks()
            #     ship_speed_brake = ship_min_brake
            #     fume = True
            # if event.key == K_SPACE:
            #     fire = True
        # if event.type == KEYUP:
        #     if event.key == K_UP:
        #         # forward = False
        #         fume = False
        #     if event.key == K_RIGHT:
        #         direction = "stop"
        #     if event.key == K_LEFT:
        #         direction = "stop"
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if controller.left_pos.collidepoint(pos):
                direction = "left"
            elif controller.right_pos.collidepoint(pos):
                direction = "right"
            elif controller.thrust_pos.collidepoint(pos):
                forward = True
                thrust_start = pygame.time.get_ticks()
                ship_speed_brake = ship_min_brake
                fume = True
            elif controller.fire_pos.collidepoint(pos):
                fire = True

        if event.type == pygame.MOUSEBUTTONUP:
            direction = "stop"
            fume = False
            
    
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

    controller.update()
    windowSurface.blit(controller.menu_bar, (100, 500))
    
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
        thrust_elapsed = pygame.time.get_ticks() - thrust_start
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
           # windowSurface.fill((255, 0, 0))
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
    
