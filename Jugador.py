import pygame
import os

class lucy(pygame.sprite.Sprite):
    def __init__(self, ancho, alto):
        super().__init__()
        carpeta_imagenes = os.path.join('Imagenes_de_prueba', 'Lucy')
        self.derecha_imagenes   = [pygame.image.load(os.path.join(carpeta_imagenes, 'Derecha', '1.png')).convert_alpha(),
                                   pygame.image.load(os.path.join(carpeta_imagenes, 'Derecha', '2.png')).convert_alpha(),
                                   pygame.image.load(os.path.join(carpeta_imagenes, 'Derecha', '3.png')).convert_alpha(),
                                   pygame.image.load(os.path.join(carpeta_imagenes, 'Derecha', '4.png')).convert_alpha()]
        
        self.izquierda_imagenes = [pygame.image.load(os.path.join(carpeta_imagenes, 'Izquierda', '1.png')).convert_alpha(),
                                   pygame.image.load(os.path.join(carpeta_imagenes, 'Izquierda', '2.png')).convert_alpha(),
                                   pygame.image.load(os.path.join(carpeta_imagenes, 'Izquierda', '3.png')).convert_alpha(),
                                   pygame.image.load(os.path.join(carpeta_imagenes, 'Izquierda', '4.png')).convert_alpha()]
        
        
        self.arriba_imagenes    = [pygame.image.load(os.path.join(carpeta_imagenes, 'Arriba', '1.png')).convert_alpha(),
                                   pygame.image.load(os.path.join(carpeta_imagenes, 'Arriba', '2.png')).convert_alpha(),
                                   pygame.image.load(os.path.join(carpeta_imagenes, 'Arriba', '3.png')).convert_alpha(),
                                   pygame.image.load(os.path.join(carpeta_imagenes, 'Arriba', '4.png')).convert_alpha()]
        
        
        self.abajo_imagenes     = [pygame.image.load(os.path.join(carpeta_imagenes, 'Abajo', '1.png')).convert_alpha(),
                                   pygame.image.load(os.path.join(carpeta_imagenes, 'Abajo', '2.png')).convert_alpha(),
                                   pygame.image.load(os.path.join(carpeta_imagenes, 'Abajo', '3.png')).convert_alpha(),
                                   pygame.image.load(os.path.join(carpeta_imagenes, 'Abajo', '4.png')).convert_alpha()]
        
        lucy.redimensionar(self)

        self.alto = alto
        self.ancho = ancho
        self.indice_animacion = 0
        self.imagen_actual = self.abajo_imagenes[self.indice_animacion]
        self.rect = self.imagen_actual.get_rect()
        self.rect.center = (ancho // 2 ,alto // 2)
        self.velocidad = 4


    def redimensionar(self):
        redimension = (60, 60)
        for i in range(0, 4):
            self.abajo_imagenes[i]     = pygame.transform.scale(self.abajo_imagenes[i], redimension)
            self.arriba_imagenes[i]    = pygame.transform.scale(self.arriba_imagenes[i], redimension)
            self.derecha_imagenes[i]   = pygame.transform.scale(self.derecha_imagenes[i], redimension)
            self.izquierda_imagenes[i] = pygame.transform.scale(self.izquierda_imagenes[i], redimension)


    def update(self, teclas_presionadas):
        if teclas_presionadas[pygame.K_w] and self.rect.y > 40:
            self.rect.y -= self.velocidad
            self.indice_animacion += 1
            if self.indice_animacion >= len(self.arriba_imagenes):
                self.indice_animacion = 0
            self.imagen_actual = self.arriba_imagenes[self.indice_animacion]

        elif teclas_presionadas[pygame.K_s] and self.rect.y < (self.alto - (self.rect.height + 40)):
            self.rect.y += self.velocidad
            self.indice_animacion += 1
            if self.indice_animacion >= len(self.abajo_imagenes):
                self.indice_animacion = 0
            self.imagen_actual = self.abajo_imagenes[self.indice_animacion]

        elif teclas_presionadas[pygame.K_a] and self.rect.x > 40:
            self.rect.x -= self.velocidad
            self.indice_animacion += 1
            if self.indice_animacion >= len(self.izquierda_imagenes):
                self.indice_animacion = 0
            self.imagen_actual = self.izquierda_imagenes[self.indice_animacion]

        elif teclas_presionadas[pygame.K_d] and self.rect.x < (self.ancho - (self.rect.width + 40)) :
            self.rect.x += self.velocidad
            self.indice_animacion += 1
            if self.indice_animacion >= len(self.derecha_imagenes):
                self.indice_animacion = 0
            self.imagen_actual = self.derecha_imagenes[self.indice_animacion]

    def dibujar(self, ventana):
        ventana.blit(self.imagen_actual, self.rect)