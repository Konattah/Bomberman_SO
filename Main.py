# Librerias necesarias
import pygame
from Jugador import lucy
from Escenario import escenario

# Inicializamos pygame
pygame.init()

# Cosas de la ventana
ancho_ventana = 1280
alto_ventana = 720
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Bomberman")

#Reloj
clock = pygame.time.Clock()
fps = 60

game_over = False
jugador_1 = lucy(ancho_ventana, alto_ventana)
laberinto = escenario(ancho_ventana, alto_ventana)

while(game_over == False):
    # Eventitos que van sucediendo
    for evento in pygame.event.get():
        # Evento por si apretan la X de la ventana
        if evento.type == pygame.QUIT:
            game_over = True

    ventana.fill((255, 255, 255))

    # Se guarda la tecla que se vaya a presionar
    tecla = pygame.key.get_pressed()
    jugador_1.update(tecla)

    # Dibujos
    laberinto.dibujar(ventana)
    jugador_1.dibujar(ventana)

    # Se renderiza el juego desde acá
    pygame.display.flip()
    
    # Limita el juego a 60 FPS
    clock.tick(fps) 

pygame.quit()