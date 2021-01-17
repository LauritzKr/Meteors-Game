import pygame
import sys
from pygame.locals import *
import random
import threading

MOVE_SPEED = 5

class Weltraum(object):
  
  def __init__(self):
    self.size = [1000, 700]
    self.fenster = pygame.display.set_mode(self.size)
    self.meteorliste=[]
    self.schiff = Schiff()
    self.punkte=0

  def generateMeteor(self,x,y,a,b):
    return Meteor(x,y,a,b)

  def schiessen(self, direction, x, y):
    return Schuss(x,y, direction)

  def punktezaehler(self):
    self.punkte+=1

'''

Aufgabe 1: Parameter und Attribute

width und height: Dimension der Meteore beim Erstellen in Pixeln
posx und posy:    Position der Meteore Beim Erstellen (zufällig)

In self.image wird die Bilddatei des Meteors geladen, dessen Größe zunächst auf die angegebene Breite und Höhe angepasst wird.
self.rect ist ein das Bild komplett einschließendes Rechteck, mithilfe dessen der Meteor platziert wird.
self.speed ist eine zufällige Zahl zwischen 1 und 9. Um so viele Pixel wird der Meteor bei jedem Aufruf von move() bewegt (-> Schnelligkeit).
self.directionx ist entweder "right" oder "left", also eine zufällige Richtung auf der x-Achse, mithilfe dessen die Meteore in die richtigen Richtungen bewegt werden.
self.directiony das selbe, nur auf der y-Achse.

'''
class Meteor(pygame.sprite.Sprite):
  def __init__(self, width, height, posx, posy):
    super(Meteor, self).__init__()
    self.image=pygame.image.load("metgross.gif")
    self.image = pygame.transform.scale(self.image, (width, height))
    self.rect = self.image.get_rect()
    self.rect.x=posx
    self.rect.y=posy
    self.speed = random.randint(1, 10)
    self.directionx = random.choice(["right", "left"])
    self.directiony = random.choice(["down", "up"])

  def move(self):
    if self.directionx == "right":
      if self.rect.x >= 1000:
        self.directionx = "left"
      else:
        self.rect.x = self.rect.x + self.speed
    elif self.directionx == "left":
      if self.rect.x <= 0:
        self.directionx = "right"
      else:
        self.rect.x = self.rect.x - self.speed
    if self.directiony == "down":
      if self.rect.y >= 700:
        self.directiony = "up"
      else:
        self.rect.y = self.rect.y + self.speed
    elif self.directiony == "up":
      if self.rect.y <= 0:
        self.directiony = "down"
      else:
        self.rect.y = self.rect.y - self.speed
    
class Schiff(pygame.sprite.Sprite):

  '''

  Aufgabe 2:

  '''

  def __init__(self):
    super(Schiff, self).__init__()
    self.image = pygame.image.load("links.gif")   # STARTRICHTUNG
    self.rect = self.image.get_rect()
    self.rect.y = 100   # STARTPOSITION (HÖHE)
    self.speed=1

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

class Schuss(pygame.sprite.Sprite):
  def __init__(self,x , y, direction):
    super(Schuss, self).__init__()
    self.schiff=Schiff()
    self.image = pygame.transform.scale(pygame.image.load("schuss.gif"), (20, 20))
    self.rect = pygame.Rect(x, y, 10, 10)
    self.rect.x=x
    self.rect.y=y-20
    self.richtung=direction
    self.speed=50
    
  def update(self):
    if self.richtung == "left":

      self.rect.x = self.rect.x - self.speed
    if self.richtung == "right":
      
      self.rect.x = self.rect.x + self.speed
    if self.richtung == "up":
      
      self.rect.y = self.rect.y - self.speed
    if self.richtung == "down":
      
      self.rect.y = self.rect.y + self.speed
      
#Hauptprogramm  
pygame.init()
clock = pygame.time.Clock()
w = Weltraum()
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
  
  '''

  Aufgabe 3:

  Die Variable keys (pygame.key.get_pressed()) enthält ist eine LISTE mit BOOLEAN VALUES (True oder False)
  für jede Taste der Tastatur. Sie enthält also den Zustand der Tastatur. Anschließend wird diese Liste auf
  bestimmte Tastenanschläge (eigentlich dem Value True an einer bestimmten Stelle) geprüft und es folgen 
  Aktionen, wie das Schiff mit move(direction) zu bewegen oder die Schnelligkeit des Schiffes zu verändern
  (w.schiff.speed).

  '''

  keys = pygame.key.get_pressed()
  
  if keys[pygame.K_l]:    # L
    w.schiff.move("right")
    w.schiff.speed+=2

  if keys[pygame.K_j]:    # J
    w.schiff.move("left")
    w.schiff.speed-=2

  if keys[pygame.K_k]:    # K
    w.schiff.move("up")
    
  if keys[pygame.K_i]:    # I
    w.schiff.move("down")

  '''

  Aufgabe 4:

  Der unten stehende Befehl erhält ein 3-Tupel mit den RGB Werten des Hintergrundes ((255,255,255) = weiß).
  Diese Hintergrundfarbe muss in jedem Durchlauf der Spielschleife erneut gesetzt werden, da die Objekte
  im Spiel (Meteore, Schiff) nicht an sich bewegt, sondern eher ein bisschen weiter in einer Richtung hin-
  kopiert werden. Die "alte" Version des Objekts muss somit mit einem neuen Hintergrund überdeckt werden,
  damit keine Spuren hinterlassen werden.

  '''

  #w.fenster.fill((255,255,255))

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
