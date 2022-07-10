import pygame
import pygame.font
from pygame.locals import *
import sys, os, time, random, requests
pygame.init()
pygame.font.init()
sprites = []
def resize_image(image, size=(32, 32)):
    try:
        image = pygame.image.load(image)
    except:
        image = image
    image = pygame.transform.scale(image, size)
    return image
class Game:
    def __init__(self, title="New Pigeon2D Game", GRAVITY=1, FRICTION=0.9, ACCELERATION=1):
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
        for sprite in sprites:
            if sprite.playerobj:
                sprite.move()
            sprite.draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        self.FPS.tick(60)
    def config(self, title=None, GRAVITY=None, FRICTION=None, ACCELERATION=None):
        if title:
            pygame.display.set_caption(title)
        if GRAVITY:
            self.GRAV = GRAVITY
        if FRICTION:
            self.FRIC = FRICTION
        if ACCELERATION:
            self.ACCEL = ACCELRATION
        if not title and not GRAVITY and not FRICTION and not ACCELERATION:
            print("Please enter a configuration option: title, GRAVITY, FRICTION or ACCELERATION.")
class Sprite(pygame.sprite.Sprite):
    def __init__(self, surface, image, pos=(0, 0), playerobj=True, gravityaffected=True):
        super().__init__()
        sprites.append(self)
        self.velx = 0
        self.vely = 0
        self.gravityaffected = gravityaffected
        self.playerobj = playerobj
        try:
            self.image = pygame.image.load(image)
        except:
            self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.surface = surface
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.velx -= self.surface.ACCEL    
        if pressed_keys[K_RIGHT]:
            self.velx += self.surface.ACCEL
        self.velx *= self.surface.FRIC
        if self.gravityaffected:
            self.vely += self.surface.GRAV
        self.rect.move_ip(self.velx, self.vely)
    def draw(self):
        self.surface.window.blit(self.image, self.rect)
    def config(self, surface=None, image=None, pos=None, playerobj=None, gravityaffected=None):
        if surface:
            self.surface = surface
        if image:
            try:
                self.image = pygame.image.load(image)
            except:
                self.image = image
        if pos:
            self.rect.center = pos
        if playerobj:
            self.playerobj = playerobj
        if gravityaffected:
            self.gravityaffected = gravityaffected
        if not playerobj and not pos and not image and not surface and not gravityaffected:
            print("Please enter a configuration option: surface, image, pos, playerobj or gravityaffected.")

# Spritesheet handling by pygame (https://www.pygame.org/wiki/Spritesheet) adapted to Python 3.9.2 by desvasicek

class spritesheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error:
            print('Unable to load spritesheet image:' + filename)
            raise SystemExit
    def image_at(self, rectangle, colorkey = None):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey != None:
            if colorkey == -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    def images_at(self, rects, colorkey = None):
        return [self.image_at(rect, colorkey) for rect in rects]
    def load_strip(self, rect, image_count, colorkey = None):
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)
class SpriteStripAnim(object):
    def __init__(self, filename, rect, count, colorkey=None, loop=False, frames=1):
        self.filename = filename
        ss = spritesheet.spritesheet(filename)
        self.images = ss.load_strip(rect, count, colorkey)
        self.i = 0
        self.loop = loop
        self.frames = frames
        self.f = frames
    def iter(self):
        self.i = 0
        self.f = self.frames
        return self
    def next(self):
        if self.i >= len(self.images):
            if not self.loop:
                raise StopIteration
            else:
                self.i = 0
        image = self.images[self.i]
        self.f -= 1
        if self.f == 0:
            self.i += 1
            self.f = self.frames
        return image
    def __add__(self, ss):
        self.images.extend(ss.images)
        return self
