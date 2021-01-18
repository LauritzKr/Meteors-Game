import pygame
from src import meteor


class Space:
  
    def __init__(self):
        self.root = pygame.display.set_mode([1000, 700])
        self.score = 0

    def add_score(self):
        self.score += 1

    def generate_meteor(self, x, y, a, b):
        return meteor.Meteor(x, y, a, b)
