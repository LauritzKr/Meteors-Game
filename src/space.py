import pygame
from src import meteor, shot, shuttle


class Space:
  
    def __init__(self):
        self.root = pygame.display.set_mode([1000, 700])
        self.shuttle = shuttle.Shuttle()
        self.meteors = []
        self.score = 0

    def generate_meteor(self, x, y, a, b):
        return meteor.Meteor(x, y, a, b)

    def shoot(self, direction, x, y):
        return shot.Shot(x, y, direction)

    def add_score(self):
        self.score += 1
