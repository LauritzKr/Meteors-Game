import pygame


class Shot(pygame.sprite.Sprite):

    def __init__(self, x, y, direction):
        super(Shot, self).__init__()
        self.image = pygame.transform.scale(pygame.image.load("img\\shot.gif"), (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction
        self.speed = 50
    
    def update(self):
        # Movement
        if self.direction == "left":
            self.rect.x -= self.speed
        if self.direction == "right":
            self.rect.x += self.speed
        if self.direction == "up":
            self.rect.y -= self.speed
        if self.direction == "down":
            self.rect.y += self.speed
