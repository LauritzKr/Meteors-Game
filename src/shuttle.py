import pygame


class Schiff(pygame.sprite.Sprite):

    def __init__(self):
        super(Schiff, self).__init__()
        self.image = pygame.image.load("img\\shuttle.gif")
        self.rect = self.image.get_rect()
        self.rect.y = 100
        self.speed = 1

    def move(self, direction):
        if self.rect.x>1000:
            self.rect.x=0
        if self.rect.y>700:
            self.rect.y=0
        if self.rect.x<0:
            self.rect.x=1000
        if self.rect.y<0:
            self.rect.y=700

        if direction == "left":
            self.rect.x = self.rect.x - self.speed
        if direction == "right":      
            self.rect.x = self.rect.x + self.speed
        if direction == "up":
            self.rect.y = self.rect.y + self.speed
        if direction == "down":
            self.rect.y = self.rect.y - self.speed
