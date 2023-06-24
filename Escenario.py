import pygame
import os

class escenario(pygame.sprite.Sprite):
    def __init__(self, ancho, alto):
        super().__init__()
        self.ancho = ancho
        self.alto = alto
        carpeta_imagenes = os.path.join('Imagenes', 'Escenario')
        self.escenario_imagenes = [pygame.image.load(os.path.join(carpeta_imagenes, 'ground_06.png')).convert_alpha(),
                                   pygame.image.load(os.path.join(carpeta_imagenes, 'crate_19.png')).convert_alpha()]
                                
        
        self.redimensionar()

        self.rect_fondo = self.escenario_imagenes[0].get_rect()
        self.rect_irrompible = self.escenario_imagenes[1].get_rect()

    def redimensionar(self):
        dimension = (40, 40)
        for i in range(0, len(self.escenario_imagenes)):
            self.escenario_imagenes[i] = pygame.transform.scale(self.escenario_imagenes[i], dimension)

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
                ventana.blit(self.escenario_imagenes[1], (x * self.rect_irrompible.width, y * self.rect_irrompible.height))


