# Librerias necesarias
import pygame
import os
import random
from Escenario import irrompible, rompible
from Jugador import jugador

# Constantes
bloques_tamanio = 40


suelo = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
         [-1, 3, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1],
         [-1, 0, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
         [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1],
         [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
         [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1],
         [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
         [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1],
         [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
         [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1],
         [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
         [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1],
         [-1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1],
         [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 4, -1],
         [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

# Cosas de la ventana
ancho_ventana = 760
alto_ventana = 600
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Bomberman")

#Reloj
clock = pygame.time.Clock()
fps = 30


# Grupos de sprites
all_rompibles = pygame.sprite.Group()
all_irrompibles = pygame.sprite.Group()
all_jugador = pygame.sprite.Group()
all_bombas = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


game_over = False

for f in range(len(suelo)):
    for c in range(len(suelo[f])):
        if suelo[f][c] == -1:
            all_irrompibles.add(irrompible(c, f, bloques_tamanio))
        elif suelo[f][c] == 1:
            azar = random.randint(1, 4)
            if azar == 1 or azar == 3:
                madera = rompible(c, f, bloques_tamanio)
                all_rompibles.add(madera)
                suelo[f][c] = 1
            else:
                suelo[f][c] = 0
        elif suelo[f][c] == 3:
            jugador1 = jugador(c, f, all_bombas, all_sprites, all_rompibles, bloques_tamanio, suelo, all_jugador)
            all_jugador.add(jugador1)
            suelo[f][c] = 0


all_sprites.add(all_irrompibles)
all_sprites.add(all_rompibles)
all_sprites.add(all_jugador)

while(game_over == False):
    # Eventitos que van sucediendo
    for evento in pygame.event.get():
        # Evento por si apretan la X de la ventana
        if evento.type == pygame.QUIT:
            game_over = True

    ventana.fill((255, 192, 203))

    # Se guarda la tecla que se vaya a presionar
    tecla = pygame.key.get_pressed()

    jugador1.update(tecla)
    all_bombas.update()

    # Dibujos
    all_sprites.draw(ventana)

    # Se renderiza el juego desde acá
    pygame.display.flip()
    
    # Limita los fps del juego
    clock.tick(fps) 

pygame.quit()
