import pygame
import sys
import random
from src import space

MOVE_SPEED = 5 
#Hauptprogramm  
pygame.init()
clock = pygame.time.Clock()
w = space.Weltraum()
allmeteors = pygame.sprite.Group()
allschiff = pygame.sprite.Group()
allshoots = pygame.sprite.Group()
allschiff.add(w.schiff)

for i in range(0,7):
    w.meteorliste.append(w.generateMeteor(60,30,random.randint(500, 1000), random.randint(300, 700)))
    allmeteors.add(w.meteorliste[-1])

#Spielschleife
while True:
	pygame.time.delay(100)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
        	sys.exit()       

  	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_l]:
		w.schiff.move("right")
		w.schiff.speed+=2
		
	if keys[pygame.K_j]:    # J
		w.schiff.move("left")
		w.schiff.speed-=2

	if keys[pygame.K_k]:
		w.schiff.move("up")
		
	if keys[pygame.K_i]:
		w.schiff.move("down")

  	w.fenster.fill((255,255,255))
	  
	for meteor in allmeteors:
		meteor.move()
		
	if pygame.sprite.spritecollide(w.schiff, allmeteors, True):
		print("Collide")
	
	if keys[pygame.K_w]:   
		allshoots.add(w.schiessen("up",w.schiff.rect.x+50,w.schiff.rect.y+50))
	if keys[pygame.K_a]:
		allshoots.add(w.schiessen("left",w.schiff.rect.x,w.schiff.rect.y))
	if keys[pygame.K_s]:
		allshoots.add(w.schiessen("down",w.schiff.rect.x,w.schiff.rect.y))
	if keys[pygame.K_d]:
		allshoots.add(w.schiessen("right",w.schiff.rect.x+100,w.schiff.rect.y+100))                 
    
	for schuss in allshoots:
		schuss.update()
		if pygame.sprite.spritecollide(schuss, allmeteors, True):
			w.punktezaehler()
			for i in range(0,4):
				allmeteors.add(w.generateMeteor(30,30, 500, 350))
			print("Treffer"), w.punkte

      
	w.schiff.move("right")
	allshoots.draw(w.fenster)
	allmeteors.update()
	allmeteors.draw(w.fenster)
	allschiff.update()
	allschiff.draw(w.fenster)

	pygame.display.flip()
