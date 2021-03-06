import pygame
import sys
import random
from time import sleep
from threading import Thread
from src import gui, shuttle, meteor


class Main(Thread):

	def __init__(self):
		Thread.__init__(self)	
		pygame.init()
		
		self.gui = gui.Gui()
		self.score = 0
		self.run = True

		# Shuttle Object
		self.shuttle = shuttle.Shuttle(self.gui.shuttle_img)
		self.all_shuttles = pygame.sprite.Group()
		self.all_shuttles.add(self.shuttle)

		# Meteor Objects
		self.all_meteors = pygame.sprite.Group()
		for _ in range(3):
			self.all_meteors.add(meteor.Meteor(random.randint(500, 1000), random.randint(300, 700), self.gui.big_meteor_img))

		self.all_shots = pygame.sprite.Group()

		# Planet Objects
		self.all_planets = pygame.sprite.Group()
		for _ in range(2):
			self.all_planets.add(meteor.Meteor(random.randint(500, 1000), random.randint(300, 700), self.gui.planet1_img))
			self.all_planets.add(meteor.Meteor(random.randint(500, 1000), random.randint(300, 700), self.gui.planet2_img))
			self.all_planets.add(meteor.Meteor(random.randint(500, 1000), random.randint(300, 700), self.gui.planet3_img))

		while self.run:
			pygame.time.delay(100)

			self.gui.root.fill((0, 0, 0))
			self.keys = pygame.key.get_pressed()

			# Moving objects and checking for collisions
			self.check_quit()
			self.update_shuttle()
			self.update_shots()
			self.update_obstacles()
			self.check_collision()			

			# Updating and redrawing all objects on the screen
			self.all_shuttles.update()
			self.all_shuttles.draw(self.gui.root)
			self.all_shots.update()
			self.all_shots.draw(self.gui.root)
			self.all_meteors.update()
			self.all_meteors.draw(self.gui.root)
			self.all_planets.update()
			self.all_planets.draw(self.gui.root)

			# Updating screen
			pygame.display.flip()
	
	def check_quit(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
	
	def update_shuttle(self):
		if self.keys[pygame.K_w]:
			self.shuttle.move("up")

		if self.keys[pygame.K_a]:
			self.shuttle.move("left")
			self.shuttle.speed -= 2

		if self.keys[pygame.K_s]:
			self.shuttle.move("down")
	
		if self.keys[pygame.K_d]:
			self.shuttle.move("right")
			self.shuttle.speed += 2

		self.shuttle.move("right")
		
	
	def update_shots(self):
		if self.keys[pygame.K_UP]:   
			self.all_shots.add(self.shuttle.shoot(self.shuttle.rect.x+90, self.shuttle.rect.y+70, "up", self.gui.shot_img))

		if self.keys[pygame.K_LEFT]:
			self.all_shots.add(self.shuttle.shoot(self.shuttle.rect.x+20, self.shuttle.rect.y+40, "left", self.gui.shot_img))

		if self.keys[pygame.K_DOWN]:
			self.all_shots.add(self.shuttle.shoot(self.shuttle.rect.x+90, self.shuttle.rect.y, "down", self.gui.shot_img))

		if self.keys[pygame.K_RIGHT]:
			self.all_shots.add(self.shuttle.shoot(self.shuttle.rect.x+50, self.shuttle.rect.y+40, "right", self.gui.shot_img))                 
		
		for shot in self.all_shots:
			if pygame.sprite.spritecollide(shot, self.all_meteors, True):
				self.add_score()
				for _ in range(3):
					self.all_planets.add(meteor.Meteor(500, 350, self.gui.small_meteor_img))
				print("Treffer"), self.score

	def update_obstacles(self):
		for meteor in self.all_meteors:
			meteor.move()

		for planet in self.all_planets:
			planet.move()

	def check_collision(self):
		if pygame.sprite.spritecollide(self.shuttle, self.all_planets, True):
			print("GAME OVER!!!")
			self.shuttle.image = pygame.transform.scale(pygame.image.load("img\\shot.gif"), (100, 100))
			self.shuttle.speed = 0
			self.run = False
	
	def add_score(self):
		self.score += 1


if __name__ == "__main__":
	Main()
