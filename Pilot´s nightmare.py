import sys
import pygame
pygame.init()


ROZLISENI_X = 800
ROZLISENI_Y = 600
FPS = 60

nebe = (0, 220, 255)


hodiny = pygame.time.Clock()
okno = pygame.display.set_mode((ROZLISENI_X, ROZLISENI_Y))
pygame.display.set_caption("Pilot´s nightmare")

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    klavesy = pygame.key.get_pressed()
    
    
    
    
    
    okno.fill(nebe)
    
    pygame.display.update()
    hodiny.tick(FPS)