import pygame


class Gui:
  
    def __init__(self):
        self.root = pygame.display.set_mode([1000, 700])
        self.shuttle_img = pygame.image.load("img\\shuttle.gif")
        self.big_meteor_img = pygame.transform.scale(pygame.image.load("img\\meteor.gif"), (60, 30))
        self.small_meteor_img = pygame.transform.scale(pygame.image.load("img\\meteor.gif"), (20, 20))
        self.shot_img = pygame.transform.scale(pygame.image.load("img\\shot.gif"), (20, 20))
        self.planet1_img = pygame.transform.scale(pygame.image.load("img\\planet_1.gif"), (40, 40))
        self.planet2_img = pygame.transform.scale(pygame.image.load("img\\planet_2.gif"), (40, 40))
        self.planet3_img = pygame.transform.scale(pygame.image.load("img\\planet_3.gif"), (40, 40))
