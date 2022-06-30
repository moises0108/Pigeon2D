import pygame
import pygame.font
from pygame.locals import *
import sys, os, time, random
pygame.init()
pygame.font.init()
class Game:
    def __init__(self, title="New Pigeon2D Game", GRAVITY=1, FRICTION=0.8, ACCELERATION=1):
        self.window = pygame.display.set_mode((500, 500))
        pygame.display.set_caption(title)
        self.GRAV = GRAVITY
        self.FRIC = FRICTION
        self.ACCEL = ACCELERATION
        self.FPS = pygame.time.Clock()
        # Built in pallete
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
    def update(self, fill=(0, 0, 0)):
        self.window.fill(fill)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        self.FPS.tick(60)
