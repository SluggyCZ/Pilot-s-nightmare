import sys
import pygame
import random

pygame.init()


ROZLISENI_X = 1920
ROZLISENI_Y = 1020


FPS = 60
velikost_x = 180
velikost_y = 100
pozice_x = (ROZLISENI_X - velikost_x) / 2
pozice_y = (ROZLISENI_Y - velikost_y) / 2
rychlost = 3
smer_x = 0
smer_y = 0
mr1_x = 50
mr1_y = 50
nebe = (0, 220, 255)
uhel = 0

letadlo = pygame.image.load('vrtadlo1.png')
letadlo = pygame.transform.scale(letadlo, (velikost_x, velikost_y))
pozadi = pygame.image.load('pozadi.png')
pozadi = pygame.transform.scale(pozadi, (ROZLISENI_X, ROZLISENI_Y))



hodiny = pygame.time.Clock()
okno = pygame.display.set_mode((ROZLISENI_X, ROZLISENI_Y))
pygame.display.set_caption("Pilot´s nightmare")

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    klavesy = pygame.key.get_pressed()
    
    
    if klavesy[pygame.K_UP]:
        smer_y -= 0.5
        
    
    if klavesy[pygame.K_DOWN]:
        smer_y += 0.5
        
    
    if klavesy[pygame.K_LEFT]:
        smer_x -= 0.5
        uhel += 1
        
    if klavesy[pygame.K_RIGHT]:
        smer_x += 0.5
        uhel -= 1
    
    
    
    
    
    pozice_x += smer_x
    pozice_y += smer_y
    if smer_x < -3:
        smer_x = -3
    if smer_x > 3:
        smer_x = 3
    if smer_y < -3:
        smer_y = -3
    if smer_y > 3:
        smer_y = 3
    
    if uhel > 15:
        uhel = 15
    if uhel < -15:
        uhel = -15
    
    
    
    if pozice_x > ROZLISENI_X - velikost_x:
        pozice_x = ROZLISENI_X - velikost_x
    if pozice_y > ROZLISENI_Y - velikost_y:
        pozice_y = ROZLISENI_Y - velikost_y
    if pozice_x < 0:
        pozice_x = 0
    if pozice_y < 0:
        pozice_y = 0
    letadlo1 = pygame.transform.rotate(letadlo, uhel)
    okno.fill(nebe)
    okno.blit(letadlo1, (pozice_x, pozice_y))
    
    pygame.display.update()
    hodiny.tick(FPS)