import pygame
import os
import time

class bomba(pygame.sprite.Sprite):
    def __init__(self, tamanio, posicion_y, posicion_x):
        pygame.sprite.Sprite.__init__(self)
        
        self.bomba = pygame.image.load(os.path.join('Imagenes/Bomba/bomb.png')).convert_alpha()
        self.bomba = pygame.transform.scale(self.bomba, (tamanio, tamanio))
        self.explosion_1 = pygame.image.load(os.path.join('Imagenes/Bomba/exp1.png')).convert_alpha()
        self.explosion_1 = pygame.transform.scale(self.explosion_1, (tamanio, tamanio))
        self.explosion_2 = pygame.image.load(os.path.join('Imagenes/Bomba/exp2.png')).convert_alpha()
        self.explosion_2 = pygame.transform.scale(self.explosion_2, (tamanio, tamanio))
        self.explosion_3 = pygame.image.load(os.path.join('Imagenes/Bomba/exp3.png')).convert_alpha()
        self.explosion_3 = pygame.transform.scale(self.explosion_3, (tamanio, tamanio))

        self.imagenes = [self.bomba, self.explosion_1, self.explosion_2, self.explosion_3]

        self.imagen_actual = 0
        self.image = self.imagenes[self.imagen_actual]
        self.rect = self.image.get_rect()
        self.rect.y = posicion_y
        self.rect.x = posicion_x

        self.tiempo_inicial = time.time()
        

    def update(self):
        tiempo_transcurrido = time.time() - self.tiempo_inicial
        if tiempo_transcurrido >= 3:
            self.imagen_actual += 1
            if(self.imagen_actual != len(self.imagenes) - 1):
                self.image = self.imagenes[self.imagen_actual]
            else:
                self.kill()