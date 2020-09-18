import pygame
from pygame import *

size_square = 50
count_row = 5

width=800
height=600

screen = pygame.display.set_mode((width,height))

surface = Surface((size_square,size_square))
surface.fill((0,0,255))

while 1:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break
    screen.fill((255,0,0))
    

    for ind in range(width//size_square//2):
        screen.blit(surface,(size_square*2*ind,200))
    for ind in range(3,height//size_square//2):
        screen.blit(surface,(0,size_square*2*ind))
    for ind in range(width//size_square//2):
        screen.blit(surface,(size_square*2*ind, height -  size_square))
    for ind in range(3,height//size_square//2):
        screen.blit(surface,(width-size_square*2,size_square*2*ind))
    for ind in range(3):
        screen.blit(surface,(0+size_square*2)
        pos = 0
    while pos < size_square*(count_row)*2:
        t = 200-pos/2
 
        
        #print(t)
        screen.blit(surface,(pos,t))
        pos=pos+size_square*2


    #print(pos)


  

    
    
    
        
        
            

    
    pygame.display.update()
    

