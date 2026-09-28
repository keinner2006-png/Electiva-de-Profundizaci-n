import pygame
import sys

pygame.init()

pantalla = pygame.display.set_mode((800,600))
pygame.display.set_caption("Simulación de mi panatlla - UNIDAD 2")
AZUL = (0, 0, 255)

reloj = pygame.time.Clock()

ejecutando = True
while ejecutando:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            ejecutando=False

    pantalla.fill((166,132,128))
    pygame.draw.rect(pantalla, AZUL, (350, 250, 100, 100),width=2)


    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
sys.exit()


