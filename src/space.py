import pygame
from src import meteor, shot, shuttle


class Weltraum:
  
    def __init__(self):
        self.fenster = pygame.display.set_mode([1000, 700])
        self.meteorliste = []
        self.schiff = shuttle.Schiff()
        self.punkte = 0

    def generateMeteor(self, x, y, a, b):
        return meteor.Meteor(x, y, a, b)

    def schiessen(self, direction, x, y):
        return shot.Schuss(x, y, direction)

    def punktezaehler(self):
        self.punkte += 1
