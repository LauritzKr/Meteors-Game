import pygame
from src import shot


class Shuttle(pygame.sprite.Sprite):

    def __init__(self):
        super(Shuttle, self).__init__()
        self.image = pygame.image.load("img\\shuttle.gif")
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 300
        self.speed = 1

    def move(self, direction):
        # Screen edge transition
        if self.rect.x > 1000:
            self.rect.x = 0
        if self.rect.y > 700:
            self.rect.y = 0 
        if self.rect.x < 0:
            self.rect.x = 1000
        if self.rect.y < 0:
            self.rect.y = 700

        # Movement
        if direction == "left":
            self.rect.x -= self.speed
        if direction == "right":      
            self.rect.x += self.speed
        if direction == "up":
            self.rect.y -= self.speed
        if direction == "down":
            self.rect.y += self.speed

    def shoot(self, x, y, direction):
        return shot.Shot(x, y, direction)
