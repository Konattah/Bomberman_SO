import pygame
import os

class escenario(pygame.sprite.Sprite):
    def __init__(self, ancho, alto):
        super().__init__()
        self.ancho = ancho
        self.alto = alto
        carpeta_imagenes = os.path.join('kenney_tiny-town', 'Tiles')
        self.bordes_imagenes = [pygame.image.load(os.path.join(carpeta_imagenes, 'tile_0096.png')).convert_alpha(),
                                pygame.image.load(os.path.join(carpeta_imagenes, 'tile_0097.png')).convert_alpha(),
                                pygame.image.load(os.path.join(carpeta_imagenes, 'tile_0098.png')).convert_alpha(),
                                pygame.image.load(os.path.join(carpeta_imagenes, 'tile_0108.png')).convert_alpha(),
                                pygame.image.load(os.path.join(carpeta_imagenes, 'tile_0002.png')).convert_alpha()]
        
        escenario.redimensionar(self)

        self.rect_derecha      = self.bordes_imagenes[0].get_rect()
        self.rect_bordes       = self.bordes_imagenes[1].get_rect()
        self.rect_izquierda    = self.bordes_imagenes[2].get_rect()
        self.rect_bordes_lados = self.bordes_imagenes[3].get_rect()
        self.rect_fondo        = self.bordes_imagenes[4].get_rect()
    

    def redimensionar(self):
        dimension = (40, 40)
        for i in range(0, len(self.bordes_imagenes)):
            self.bordes_imagenes[i] = pygame.transform.scale(self.bordes_imagenes[i], dimension)

    def dibujar(self, ventana):
        ventana.blit(self.bordes_imagenes[0], self.rect_derecha)
        ventana.blit(pygame.transform.rotate(self.bordes_imagenes[2], 180), (0, self.alto - self.rect_derecha.height))

        ventana.blit(self.bordes_imagenes[2], (self.ancho - self.rect_izquierda.height, 0))
        ventana.blit(pygame.transform.rotate(self.bordes_imagenes[0], 180), (self.ancho - self.rect_izquierda.height, self.alto - self.rect_izquierda.height))

        cantidad_bordes_ancho = (self.ancho // self.rect_bordes.height) - 1
        for i in range(1, cantidad_bordes_ancho):
            ventana.blit(self.bordes_imagenes[1], (i * self.rect_bordes.height, 0))
            ventana.blit(pygame.transform.rotate(self.bordes_imagenes[1], 180), (i * self.rect_bordes.height, self.alto - self.rect_bordes.height))

        cantidad_bordes_lados = (self.alto // self.rect_bordes_lados.height) - 1
        for i in range(1, cantidad_bordes_lados):
            ventana.blit(self.bordes_imagenes[3], (0, self.rect_bordes_lados.height * i))
            ventana.blit(pygame.transform.rotate(self.bordes_imagenes[3], 180), (self.ancho - self.rect_bordes.height, i * self.rect_bordes.height))

        cantidad_fondo_ancho = (self.ancho // self.rect_fondo.height) - 1
        cantidad_fondo_alto  = (self.alto // self.rect_fondo.height) - 1
        for i in range(1, cantidad_fondo_ancho):
            for j in range(1, cantidad_fondo_alto):
                ventana.blit(self.bordes_imagenes[4], (i * self.rect_fondo.height, j * self.rect_fondo.height))
            ventana.blit(self.bordes_imagenes[4], (i * self.rect_fondo.height, j * self.rect_fondo.height))