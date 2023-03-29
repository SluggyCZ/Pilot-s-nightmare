#základy
import sys
import pygame
import random

pygame.init()

#proměnné
ROZLISENI_X = 1600
ROZLISENI_Y = 900

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
cerna = (0, 0, 0)
uhel = 0
poradi = 0
pad = 12
heal_x = random.randint(50, ROZLISENI_X - 5)
heal_y = 0
padheal = 6
zivot = 5
font = pygame.font.SysFont('Consolas', 30)
counter, text = 0, '0'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
bomba_x = random.randint(50, ROZLISENI_X - 50)
bomba_y = 8000
bomba_v_x = 40
bomba_v_y = 70

#načtení obrázků
letadlo1 = pygame.image.load('vrtadlo1.png')
letadlo1 = pygame.transform.scale(letadlo1, (velikost_x, velikost_y))
letadlo2 = pygame.image.load('vrtadlo2.png')
letadlo2 = pygame.transform.scale(letadlo2, (velikost_x, velikost_y))
konec = pygame.image.load('konec.png')
konec = pygame.transform.scale(konec, (ROZLISENI_X, ROZLISENI_Y))
bomba = pygame.image.load('bomba.png')
bomba = pygame.transform.scale(bomba, (bomba_v_x, bomba_v_y))
heal = pygame.image.load('padacek.png')
heal = pygame.transform.scale(heal, (bomba_v_x + (bomba_v_x / 2), bomba_v_y + (bomba_v_y / 2)))
z5 = pygame.image.load("5zivotu.png")
z4 = pygame.image.load("4zivoty.png")
z3 = pygame.image.load("3zivoty.png")
z2 = pygame.image.load("2zivoty.png")
z1 = pygame.image.load("1zivot.png")
animace = [letadlo1,
           letadlo1,
           letadlo2,
           letadlo2]

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
        if udalost.type == pygame.USEREVENT: 
            counter += 1
            text = str(counter).rjust(3) 
    #ovládání
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
    
    
    #kontroly
    pozice_x += smer_x
    pozice_y += smer_y
    
    if smer_x < -7:
        smer_x = -7
    if smer_x > 7:
        smer_x = 7
    if smer_y < -7:
        smer_y = -7
    if smer_y > 7:
        smer_y = 7
    
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
    
    #animace obrázku
    if poradi >= len(animace):
        poradi = 0
    vyberletadla = animace[poradi]
    letadlo = pygame.transform.rotate(vyberletadla, uhel)
    
    #vykreslení obrazu
    okno.fill(nebe)
    
    if bomba_y > ROZLISENI_Y:    
        bomba_y = 0
        bomba_x = random.randint(50, ROZLISENI_X - 50)
    hitbox_b = pygame.draw.rect(okno, nebe, (bomba_x, bomba_y , bomba_v_x , bomba_v_y))
    okno.blit(bomba, (bomba_x, bomba_y))    
    
    hitbox_l = pygame.draw.rect(okno, nebe, (pozice_x + 10, pozice_y + 10, velikost_x - 10, velikost_y))
    okno.blit(font.render(text, True, (0, 0, 0)), (ROZLISENI_X - ROZLISENI_X/1.05, ROZLISENI_Y - ROZLISENI_Y/1.05))
    
    okno.blit(heal, (heal_x, heal_y))
    hitbox_h = pygame.draw.rect(okno, nebe, (heal_x, heal_y, bomba_v_x + (bomba_v_x / 2) , bomba_v_y + (bomba_v_y / 2)))
    
    
    kolize = pygame.Rect.colliderect(hitbox_b, hitbox_l)
    kolize_h = pygame.Rect.colliderect(hitbox_h, hitbox_l)
    
    
    if kolize:
        zivot -= 1
        bomba_y = -750
        bomba_x = random.randint(50, ROZLISENI_X - 50)
    if zivot == 5:
        okno.blit(z5, ((ROZLISENI_X/2)-127.5, ROZLISENI_Y-30))
    if zivot == 4:
        okno.blit(z4, ((ROZLISENI_X/2)-127.5, ROZLISENI_Y-30))
    if zivot == 3:
        okno.blit(z3, ((ROZLISENI_X/2)-127.5, ROZLISENI_Y-30))
    if zivot == 2:
        okno.blit(z2, ((ROZLISENI_X/2)-127.5, ROZLISENI_Y-30))
    if zivot == 1:
        okno.blit(z1, ((ROZLISENI_X/2)-127.5, ROZLISENI_Y-30))
    
    
    okno.blit(letadlo, (pozice_x, pozice_y))
    
    
    if zivot <= 0:
        okno.blit(konec, (0, 0))
    if counter == 10:
        pad += 0.1
    if counter == 20:
        pad += 0.1
    if counter == 30:
        pad += 0.1
    if counter == 40:
        pad += 0.1
    bomba_y += pad
    poradi += 1
    pygame.display.update()
    hodiny.tick(FPS)