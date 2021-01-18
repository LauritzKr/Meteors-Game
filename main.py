import pygame
import sys
import random
from threading import Thread
from src import meteor, shuttle, space


class Main(Thread):

	def __init__(self):
		Thread.__init__(self)	
		pygame.init()
		
		self.space = space.Space()
		self.all_shots = pygame.sprite.Group()

		# Shuttle Object
		self.shuttle = shuttle.Shuttle()
		self.all_shuttles = pygame.sprite.Group()
		self.all_shuttles.add(self.shuttle)

		# Meteor Objects
		self.all_meteors = pygame.sprite.Group()
		for _ in range(7):
			self.all_meteors.add(meteor.Meteor(60, 30, random.randint(500, 1000), random.randint(300, 700)))

		while True:
			pygame.time.delay(100)

			self.space.root.fill((0, 0, 0))
			self.keys = pygame.key.get_pressed()

			# Moving objects and checking for collisions
			self.check_quit()
			self.update_shuttle()
			self.update_shots()
			self.update_meteors()
			self.check_collision()			

			# Updating and redrawing all objects on the screen
			self.all_shuttles.update()
			self.all_shuttles.draw(self.space.root)
			self.all_shots.update()
			self.all_shots.draw(self.space.root)
			self.all_meteors.update()
			self.all_meteors.draw(self.space.root)

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
			self.all_shots.add(self.shuttle.shoot(self.shuttle.rect.x+50, self.shuttle.rect.y+50, "up"))

		if self.keys[pygame.K_LEFT]:
			self.all_shots.add(self.shuttle.shoot(self.shuttle.rect.x, self.shuttle.rect.y, "left"))

		if self.keys[pygame.K_DOWN]:
			self.all_shots.add(self.shuttle.shoot(self.shuttle.rect.x, self.shuttle.rect.y, "down"))

		if self.keys[pygame.K_RIGHT]:
			self.all_shots.add(self.shuttle.shoot(self.shuttle.rect.x+100, self.shuttle.rect.y+100, "right"))                 
		
		for shot in self.all_shots:
			#shot.update()
			if pygame.sprite.spritecollide(shot, self.all_meteors, True):
				self.space.add_score()
				for _ in range(4):
					self.all_meteors.add(self.space.generate_meteor(30, 30, 500, 350))
				print("Treffer"), self.space.score

	def update_meteors(self):
		for meteor in self.all_meteors:
			meteor.move()

	def check_collision(self):
		if pygame.sprite.spritecollide(self.shuttle, self.all_meteors, True):
			print("Collide")


if __name__ == "__main__":
	Main()
