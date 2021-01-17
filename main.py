import pygame
import sys
import random
from threading import Thread
from src import space


class Main(Thread):

	def __init__(self):	
		Thread.__init__(self)	
		pygame.init()
		
		self.space = space.Space()
		self.all_meteors = pygame.sprite.Group()
		self.all_shoots = pygame.sprite.Group()
		self.all_shuttles = pygame.sprite.Group()
		self.all_shuttles.add(self.space.shuttle)

		for _ in range(0,7):
			self.space.meteors.append(self.space.generate_meteor(60,30,random.randint(500, 1000), random.randint(300, 700)))
			self.all_meteors.add(self.space.meteors[-1])

		
		while True:
			pygame.time.delay(100)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()       
					
			keys = pygame.key.get_pressed()
			
			if keys[pygame.K_w]:
				self.space.shuttle.move("up")

			if keys[pygame.K_a]:
				self.space.shuttle.move("left")
				self.space.shuttle.speed -= 2

			if keys[pygame.K_s]:
				self.space.shuttle.move("down")
		
			if keys[pygame.K_d]:
				self.space.shuttle.move("right")
				self.space.shuttle.speed += 2
				
			self.space.root.fill((255,255,255))
			
			for meteor in self.all_meteors:
				meteor.move()
				
			if pygame.sprite.spritecollide(self.space.shuttle, self.all_meteors, True):
				print("Collide")
			
			if keys[pygame.K_w]:   
				self.all_shoots.add(self.space.shoot("up",self.space.shuttle.rect.x+50,self.space.shuttle.rect.y+50))

			if keys[pygame.K_a]:
				self.all_shoots.add(self.space.shoot("left",self.space.shuttle.rect.x,self.space.shuttle.rect.y))

			if keys[pygame.K_s]:
				self.all_shoots.add(self.space.shoot("down",self.space.shuttle.rect.x,self.space.shuttle.rect.y))

			if keys[pygame.K_d]:
				self.all_shoots.add(self.space.shoot("right",self.space.shuttle.rect.x+100,self.space.shuttle.rect.y+100))                 
			
			for shot in self.all_shoots:
				shot.update()
				if pygame.sprite.spritecollide(shot, self.all_meteors, True):
					self.space.add_score()
					for _ in range(4):
						self.all_meteors.add(self.space.generate_meteor(30,30, 500, 350))
					print("Treffer"), self.space.score

			
			self.space.shuttle.move("right")
			self.all_shoots.draw(self.space.root)
			self.all_meteors.update()
			self.all_meteors.draw(self.space.root)
			self.all_shuttles.update()
			self.all_shuttles.draw(self.space.root)

			pygame.display.flip()


if __name__ == "__main__":
	Main()
