import sys
import pygame
pygame.init()


ROZLISENI_X = 1920
ROZLISENI_Y = 1020


FPS = 60
velikostx = 150
velikosty = 100
pozicex = (ROZLISENI_X - velikostx) / 2
pozicey = (ROZLISENI_Y - velikosty) / 2
nebe = (0, 220, 255)
letadlo = pygame.image.load('letadlo.png')
letadlo = pygame.transform.scale(letadlo, (velikostx, velikosty))
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
    
    
    
    okno.blit(pozadi, (0, 0))
    okno.blit(letadlo, (pozicex, pozicey))
    
    
    pygame.display.update()
    hodiny.tick(FPS)