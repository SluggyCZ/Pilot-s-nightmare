import sys
import pygame
pygame.init()


ROZLISENI_X = 1920
ROZLISENI_Y = 1020


FPS = 60
velikost_x = 150
velikost_y = 100
pozice_x = (ROZLISENI_X - velikost_x) / 2
pozice_y = (ROZLISENI_Y - velikost_y) / 2
rychlost = 3
smer_x = -3
smer_y = 0
nebe = (0, 220, 255)

letadlo = pygame.image.load('letadlo.png')
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
        if smer_x > 0:
            smer_y += 0.25
        elif smer_x < 0:
            smer_y -= 0.25
        
    if klavesy[pygame.K_DOWN]:
        if smer_x > 0:
            smer_y -= 0.25
        elif smer_x < 0:
            smer_y += 0.25
    
    
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
        pozice_x = 0
    if pozice_y > ROZLISENI_Y - velikost_y:
        pozice_y = ROZLISENI_Y - velikost_y
    if pozice_x < 0:
        pozice_x = ROZLISENI_X - velikost_x
    if pozice_y < 0:
        pozice_y = 0
    
    
    okno.blit(pozadi, (0, 0))
    okno.blit(letadlo, (pozice_x, pozice_y))
    
    
    pygame.display.update()
    hodiny.tick(FPS)