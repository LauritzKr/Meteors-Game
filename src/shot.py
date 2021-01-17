import pygame
from src import shuttle


class Shot(pygame.sprite.Sprite):
    def __init__(self,x , y, direction):
        super(Shot, self).__init__()
        self.shuttle = shuttle.Shuttle()
        self.image = pygame.transform.scale(pygame.image.load("img\\shot.gif"), (20, 20))
        self.rect = pygame.Rect(x, y, 10, 10)
        self.rect.x = x
        self.rect.y = y - 20
        self.direction = direction
        self.speed = 50
    
    def update(self):
        if self.direction == "left":
            self.rect.x = self.rect.x - self.speed

        if self.direction == "right":
            self.rect.x = self.rect.x + self.speed

        if self.direction == "up":
            self.rect.y = self.rect.y - self.speed

        if self.direction == "down":
            self.rect.y = self.rect.y + self.speed
