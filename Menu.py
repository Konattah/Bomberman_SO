import pygame
import os
from Main import main

pygame.init()

# Cosas de la ventana
ancho_ventana = 760
alto_ventana = 600
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Bomberman")

#Reloj
clock = pygame.time.Clock()
fps = 30

fondo_img = pygame.image.load(os.path.join('Imagenes', 'Boton', 'fondo.png')).convert_alpha()
iniciar_img = pygame.image.load(os.path.join('Imagenes', 'Boton', 'iniciar.png')).convert_alpha()
salir_img = pygame.image.load(os.path.join('Imagenes', 'Boton', 'salir.png')).convert_alpha()

ancho_botones = iniciar_img.get_width()
alto_botones = iniciar_img.get_height()

# Definir las posiciones de los botones
posicion_abrir = (((ancho_ventana - ancho_botones) // 2), ((alto_ventana - alto_botones) // 2))
posicion_cerrar = (((ancho_ventana - ancho_botones) // 2), ((alto_ventana - alto_botones) // 2 + 180))



game_over = False

while(game_over == False):
    # Eventitos que van sucediendo
    for evento in pygame.event.get():
        # Evento por si apretan la X de la ventana
        if evento.type == pygame.QUIT:
            game_over = True
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if posicion_abrir[0] < evento.pos[0] < posicion_abrir[0] + ancho_botones and posicion_abrir[1] < evento.pos[1] < posicion_abrir[1] + alto_botones:
                main()
                game_over = True
            
            elif posicion_cerrar[0] < evento.pos[0] < posicion_cerrar[0] + ancho_botones and posicion_cerrar[1] < evento.pos[1] < posicion_cerrar[1] + alto_botones:
                game_over = True

    ventana.blit(fondo_img, (0, 0))
    ventana.blit(iniciar_img, posicion_abrir)
    ventana.blit(salir_img, posicion_cerrar)

    # Se renderiza el juego desde acá
    pygame.display.flip()
    
    # Limita los fps del juego
    clock.tick(fps) 

pygame.quit()