import pygame
import os

# Dimensiones de la ventana y cuadrados del escenario
ancho_ventana = 800
alto_ventana = 800
cuadro_tamano = 100

# Inicializar Pygame
pygame.init()

# Crear la ventana
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Tablero de Ajedrez")

# Cargar imágenes de los cuadrados del escenario
carpeta_imagenes = os.path.join('Imagenes', 'Escenario')
cuadro_blanco = pygame.image.load(os.path.join(carpeta_imagenes, 'ground_06.png')).convert_alpha()
cuadro_blanco = pygame.transform.scale(cuadro_blanco, (cuadro_tamano, cuadro_tamano))
cuadro_negro = pygame.image.load(os.path.join(carpeta_imagenes, 'ground_06.png')).convert_alpha()
cuadro_negro = pygame.transform.scale(cuadro_negro, (cuadro_tamano, cuadro_tamano))
cuadro_especial = pygame.image.load(os.path.join(carpeta_imagenes, "crate_04.png")).convert_alpha()
cuadro_especial = pygame.transform.scale(cuadro_especial, (cuadro_tamano, cuadro_tamano))

# Cargar imágenes del jugador animado
carpeta_jugador = os.path.join('Imagenes', 'Lucy')
jugador_derecha = pygame.image.load(os.path.join(carpeta_jugador, 'Derecha', '1.png')).convert_alpha()
jugador_derecha = pygame.transform.scale(jugador_derecha, (cuadro_tamano, cuadro_tamano))
jugador_izquierda = pygame.image.load(os.path.join(carpeta_jugador, 'Izquierda', '1.png')).convert_alpha()
jugador_izquierda = pygame.transform.scale(jugador_izquierda, (cuadro_tamano, cuadro_tamano))
jugador_arriba = pygame.image.load(os.path.join(carpeta_jugador, 'Arriba', '1.png')).convert_alpha()
jugador_arriba = pygame.transform.scale(jugador_arriba, (cuadro_tamano, cuadro_tamano))
jugador_abajo = pygame.image.load(os.path.join(carpeta_jugador, 'Abajo', '1.png')).convert_alpha()
jugador_abajo = pygame.transform.scale(jugador_abajo, (cuadro_tamano, cuadro_tamano))

# Definir la posición inicial del jugador
jugador_x = 0
jugador_y = 0

# Definir la velocidad del jugador
velocidad_jugador = cuadro_tamano

# Definir los cuadrados especiales (impenetrables)
cuadros_especiales = [(1, 0), (2, 2), (3, 1)]

# Variables para el control del bucle principal
game_over = False
clock = pygame.time.Clock()
fps = 20

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Obtener las teclas presionadas
    teclas_presionadas = pygame.key.get_pressed()

    # Mover al jugador
    if teclas_presionadas[pygame.K_LEFT] and jugador_x > 0:
        if (jugador_x - velocidad_jugador, jugador_y) not in cuadros_especiales:
            jugador_x -= velocidad_jugador
    elif teclas_presionadas[pygame.K_RIGHT] and jugador_x < ancho_ventana - cuadro_tamano:
        if (jugador_x + velocidad_jugador, jugador_y) not in cuadros_especiales:
            jugador_x += velocidad_jugador
    elif teclas_presionadas[pygame.K_UP] and jugador_y > 0:
        if (jugador_x, jugador_y - velocidad_jugador) not in cuadros_especiales:
            jugador_y -= velocidad_jugador
    elif teclas_presionadas[pygame.K_DOWN] and jugador_y < alto_ventana - cuadro_tamano:
        if (jugador_x, jugador_y + velocidad_jugador) not in cuadros_especiales:
            jugador_y += velocidad_jugador

    # Dibujar el escenario
    for fila in range(0, ancho_ventana, cuadro_tamano):
        for columna in range(0, alto_ventana, cuadro_tamano):
            if (columna // cuadro_tamano, fila // cuadro_tamano) in cuadros_especiales:
                ventana.blit(cuadro_especial, (columna, fila))
            elif (fila // cuadro_tamano) % 2 == (columna // cuadro_tamano) % 2:
                ventana.blit(cuadro_blanco, (columna, fila))
            else:
                ventana.blit(cuadro_negro, (columna, fila))

    # Dibujar al jugador
    jugador_rect = pygame.Rect(jugador_x, jugador_y, cuadro_tamano, cuadro_tamano)
    ventana.blit(jugador_derecha, jugador_rect)

    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(fps)

# Salir de Pygame
pygame.quit()