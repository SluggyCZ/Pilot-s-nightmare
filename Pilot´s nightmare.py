import sys
import pygame
import random

pygame.init()


ROZLISENI_X = 1920
ROZLISENI_Y = 1020


FPS = 60
velikost_x = 150
velikost_y = 100
pozice_x = (ROZLISENI_X - velikost_x) / 2
pozice_y = (ROZLISENI_Y - velikost_y) / 2
rychlost = 3
smer_x = 0
smer_y = 0
mr1_x = 50
mr1_y = 50
nebe = (0, 220, 255)


letadlo = pygame.image.load('vrtadlo.png')
letadlo = pygame.transform.scale(letadlo, (velikost_x, velikost_y))
pozadi = pygame.image.load('pozadi.png')
pozadi = pygame.transform.scale(pozadi, (ROZLISENI_X, ROZLISENI_Y))

letadlo_l = pygame.transform.rotate(letadlo, 15)
letadlo_p = pygame.transform.rotate(letadlo, -15)
letadlo_n = letadlo
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
        letadlo = letadlo_n
    
    if klavesy[pygame.K_DOWN]:
        smer_y += 0.5
        letadlo = letadlo_n
    
    if klavesy[pygame.K_LEFT]:
        smer_x -= 0.5
        letadlo = letadlo_l
        
    if klavesy[pygame.K_RIGHT]:
        smer_x += 0.5
        letadlo = letadlo_p
    
    
    
    
    
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
    
    
    
    if pozice_x > ROZLISENI_X - velikost_x:
        pozice_x = ROZLISENI_X - velikost_x
    if pozice_y > ROZLISENI_Y - velikost_y:
        pozice_y = ROZLISENI_Y - velikost_y
    if pozice_x < 0:
        pozice_x = 0
    if pozice_y < 0:
        pozice_y = 0
    
    okno.fill(nebe)
    okno.blit(letadlo, (pozice_x, pozice_y))
    
    pygame.display.update()
    hodiny.tick(FPS)