import pygame
import random


class Meteor(pygame.sprite.Sprite):

	def __init__(self, posx, posy, image):
		super(Meteor, self).__init__()
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = posx
		self.rect.y = posy
		self.speed = random.randint(1, 10)
		self.directionx = random.choice(["right", "left"])
		self.directiony = random.choice(["down", "up"])
		
	def move(self):
		if self.directionx == "right":
			if self.rect.x >= 1000:
				self.directionx = "left"
			else:
				self.rect.x += self.speed
		elif self.directionx == "left":
			if self.rect.x <= 0:
				self.directionx = "right"
			else:
				self.rect.x -= self.speed
		if self.directiony == "down":
			if self.rect.y >= 700:
				self.directiony = "up"
			else:
				self.rect.y += self.speed
		elif self.directiony == "up":
			if self.rect.y <= 0:
				self.directiony = "down"
			else:
				self.rect.y -= self.speed
