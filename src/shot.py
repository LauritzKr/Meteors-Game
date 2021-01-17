import pygame
from src import shuttle


class Schuss(pygame.sprite.Sprite):
    def __init__(self,x , y, direction):
        super(Schuss, self).__init__()
        self.schiff=shuttle.Schiff()
        self.image = pygame.transform.scale(pygame.image.load("img\\shot.gif"), (20, 20))
        self.rect = pygame.Rect(x, y, 10, 10)
        self.rect.x=x
        self.rect.y=y-20
        self.richtung=direction
        self.speed=50
    
    def update(self):
        if self.richtung == "left":
            self.rect.x = self.rect.x - self.speed

        if self.richtung == "right":
            self.rect.x = self.rect.x + self.speed

        if self.richtung == "up":
            self.rect.y = self.rect.y - self.speed

        if self.richtung == "down":
            self.rect.y = self.rect.y + self.speed
