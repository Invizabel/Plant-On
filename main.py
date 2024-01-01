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
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()

cursor_x = 6
cursor_y = 6

choices = [peashooter_img,sunflower_img]
board = [[sunflower_img,sunflower_img,peashooter_img,None,None,None,None,None,None],
              [sunflower_img,sunflower_img,peashooter_img,None,None,None,None,None,None],
              [sunflower_img,sunflower_img,peashooter_img,None,None,None,None,None,None],
              [sunflower_img,sunflower_img,peashooter_img,None,None,None,None,None,None]]

while True:
    time.sleep(0.1)
    display.fill("orange")
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

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
    
    pygame.draw.circle(display, "black", [cursor_x, cursor_y], 6, 1)    

    pygame.display.flip()
