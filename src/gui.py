import pygame
from random import randint


class Gui:
  
    def __init__(self):
        self.root = pygame.display.set_mode([1000, 700])
        self.shuttle_img = pygame.image.load("img\\shuttle.gif")
        self.meteor_img = pygame.transform.scale(pygame.image.load("img\\meteor.gif"), (randint(30, 60), 30))
        self.shot_img = pygame.transform.scale(pygame.image.load("img\\shot.gif"), (20, 20))
