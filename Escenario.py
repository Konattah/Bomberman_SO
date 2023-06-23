import pygame
import os

class escenario(pygame.sprite.Sprite):
    def __init__(self, ancho, alto):
        super().__init__()
        self.ancho = ancho
        self.alto = alto
        carpeta_imagenes = os.path.join('Imagenes', 'Escenario')
        self.escenario_imagenes = [pygame.image.load(os.path.join(carpeta_imagenes, 'ground_06.png')).convert_alpha()]
                                
        
        escenario.redimensionar(self)

        self.rect_fondo = self.escenario_imagenes[0].get_rect()
    

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
            ventana.blit(self.escenario_imagenes[0], (x * self.rect_fondo.width, y * self.rect_fondo.height))