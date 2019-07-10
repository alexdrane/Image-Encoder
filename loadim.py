import pygame
from pygame import *
import encoder
from encoder import *
import sys, os

WIDTH = 1200
HEIGHT = 700

pygame.init()
DISPLAY = pygame.display.set_mode((WIDTH,HEIGHT),FULLSCREEN)


image = Image.open(io.BytesIO(readfile('cat2',False)))
image.save('cat2.png')
img = pygame.image.load('cat2','.png')




while True:
  DISPLAY.fill((0,0,0))
  
  for event in pygame.event.get():
    if event.type == KEYDOWN:
      if event.key == K_ESCAPE:
        pygame.quit()
        sys.exit()
  
  DISPLAY.blit(img,(0,0))
  pygame.display.update()
