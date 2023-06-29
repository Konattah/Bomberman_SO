import pygame
import os

class irrompible(pygame.sprite.Sprite):
    def __init__(self, c, f, tamanio):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('Imagenes', 'Escenario', 'crate_19.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (tamanio, tamanio))
        self.rect = self.image.get_rect()
        self.rect.x =  c * tamanio
        self.rect.y = f * tamanio


class rompible(pygame.sprite.Sprite):
    def __init__(self, c, f, tamanio):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('Imagenes', 'Escenario', 'crate_10.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (tamanio, tamanio))
        self.rect = self.image.get_rect()
        self.rect.x =  c * tamanio
        self.rect.y = f * tamanio
        self.posicion_x = c
        self.posicion_y = f

    '''
    def dibujar(self, ventana):
        cantidad_bordes_ancho = self.ancho // self.rect_fondo.height
        cantidad_bordes_alto = self.alto // self.rect_fondo.height
        for x in range(0, cantidad_bordes_ancho):
            for y in range(0, cantidad_bordes_alto):
                ventana.blit(self.escenario_imagenes[0], (x * self.rect_fondo.width, y * self.rect_fondo.height))

        cantidad_irrompible_ancho = cantidad_bordes_ancho - 1
        cantidad_irrompible_alto = cantidad_bordes_alto - 1
        for x in range(1, cantidad_irrompible_ancho, 2):
            for y in range(1, cantidad_irrompible_alto, 2):
                ventana.blit(self.escenario_imagenes[1], (x * self.rect_irrompible.width, y * self.rect_irrompible.height))'''


