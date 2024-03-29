import random
import sys
import time
import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Plant On!")
display = pygame.display.set_mode((128, 64), pygame.SCALED)
peashooter_img = pygame.image.load("assets/peashooter.png").convert_alpha()
sunflower_img = pygame.image.load("assets/sunflower.png").convert_alpha()
cherrybomb_img = pygame.image.load("assets/cherrybomb.png").convert_alpha()
walnut_img = pygame.image.load("assets/walnut.png").convert_alpha()
potatomine_img = pygame.image.load("assets/potatomine.png").convert_alpha()
my_font = pygame.font.SysFont("calibri", 8)
cooldown_font = pygame.font.SysFont("calibri", 20)
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()

cursor_x = 6
cursor_y = 6

pea_progress = 0
player_choice = None
ticks = 0
sun = 50

choices = [peashooter_img,sunflower_img,cherrybomb_img,walnut_img,potatomine_img]
cooldown_key = [8,8,50,30,30]
new_cooldown_key = cooldown_key[:]
board = [[None,None,None,None,None,None,None,None,None],
         [None,None,None,None,None,None,None,None,None],
         [None,None,None,None,None,None,None,None,None],
         [None,None,None,None,None,None,None,None,None]]

while True:
    time.sleep(0.1)
    display.fill("orange")
    ticks += 1
    if ticks == 10:
        ticks = 0

    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == K_SPACE:
                    if cursor_y == 58:
                        for i,j in enumerate(choices):
                            if i * 12 + 6 == cursor_x:
                                player_choice = j

                    if cursor_y < 58:
                        for j,x in enumerate(board):
                            for i,y in enumerate(x):
                                if i == int(cursor_x / 12) and j == int(cursor_y / 12):
                                    if sun >= 100 and player_choice == peashooter_img and board[j][i] == None:
                                        board[j][i] = peashooter_img
                                        sun -= 100

                                    if sun >= 50 and player_choice == sunflower_img and board[j][i] == None:
                                        board[j][i] = sunflower_img
                                        sun -= 50

                                    if sun >= 150 and player_choice == cherrybomb_img and board[j][i] == None:
                                        board[j][i] = cherrybomb_img
                                        sun -= 150

                                    if sun >= 50 and player_choice == walnut_img and board[j][i] == None:
                                        board[j][i] = walnut_img
                                        sun -= 50

                                    if sun >= 25 and player_choice == potatomine_img and board[j][i] == None:
                                        board[j][i] = potatomine_img
                                        sun -= 25
                                            
                if event.key == K_UP or event.key == K_w:
                    if cursor_y < 58 and cursor_y > 6:
                        cursor_y -= 12

                    elif cursor_y == 58:
                        cursor_y -= 16

                if event.key == K_DOWN or event.key == K_s:
                    if cursor_y < 42:
                        cursor_y += 12

                    elif cursor_y == 42:
                        cursor_y += 16

                if event.key == K_LEFT or event.key == K_a:
                    if cursor_x > 6:
                        cursor_x -= 12

                if event.key == K_RIGHT or event.key == K_d:
                    if cursor_x < 102:
                        cursor_x += 12

    # draw tiles
    for i in range(0,108, 12):
        pygame.draw.rect(display, "black", [i, 0, 12, 12], 1)
        pygame.draw.rect(display, "black", [i, 12, 12, 12], 1)
        pygame.draw.rect(display, "black", [i, 24, 12, 12], 1)
        pygame.draw.rect(display, "black", [i, 36, 12, 12], 1)
        pygame.draw.rect(display, "black", [i, 52, 12, 12], 1)

    # draw plant choices
    for i,j in enumerate(choices):
        display.blit(j, ((i * 6) * 2 + 2, 54))

    # draw plants on board
    for i,x in enumerate(board):
        for j,y in enumerate(x):
            if y != None:
                display.blit(y, ((j * 6) * 2 + 2, (i * 6) * 2 + 2))

    # calculate sun
    sunflower_count = 0
    for i in board:
        sunflower_count += i.count(sunflower_img)

    for i in range(0,sunflower_count):
        my_rand = random.randint(1,240)
        if my_rand == 1:
            if sun + 25 < 1000:
                sun += 25

            else:
                sun = 999

    my_rand = random.randint(1,100)
    if my_rand == 1:
        if sun + 25 < 1000:
            sun += 25

        else:
            sun = 999
    

    # draw ammo
    pea_bool = True
    for i,x in enumerate(board):
        for j,y in enumerate(x):
            if y == peashooter_img:
                if pea_bool:
                    pea_progress += 4
                    pea_bool = False

                if pea_progress + (j * 6) * 2 + 12 <= 108:
                    pygame.draw.circle(display, "black", [pea_progress + (j * 6) * 2 + 8, (i * 6) * 2 + 4], 2, 0)

                if pea_progress == 108:
                    pea_progress = 0

    

    # draw cursor
    pygame.draw.circle(display, "black", [cursor_x, cursor_y], 6, 1)

    # draw sun text
    new_sun = ""
    for i in str(sun):
        new_sun += i + " "

    sun_font = my_font.render(new_sun, False, "black")
    display.blit(sun_font, (110, 0))

    # draw cooldown text
    if ticks == 9:
        for i,j in enumerate(choices):
            if  new_cooldown_key[i] - 1 >= 0:
                new_cooldown_key[i] -= 1

    for i,j in enumerate(choices):
        if new_cooldown_key[i] != 0:
            new_cooldown_font = cooldown_font.render("X", False, "black")
            display.blit(new_cooldown_font, ((i * 12) + 1, 50))

    # refresh
    pygame.display.update()
