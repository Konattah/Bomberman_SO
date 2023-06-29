import pygame
import os

class jugador(pygame.sprite.Sprite):
    def __init__(self, c, f, tamanio):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('Imagenes', 'Lucy', 'Abajo', '1.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (tamanio, tamanio))
        self.rect = self.image.get_rect()
        self.rect.x =  c * tamanio
        self.rect.y = f * tamanio
        self.posicion_y = c
        self.posicion_x = f
        self.tamanio = tamanio

        self.mover_arriba = False
        self.mover_abajo = False
        self.mover_izquierda = False
        self.mover_derecha = False

    def update(self, tecla, suelo):
        if tecla[pygame.K_w]:
            if suelo[self.posicion_x-1][self.posicion_y] == 0:
                self.posicion_x -= 1
                self.rect.y -= self.tamanio

        elif tecla[pygame.K_s]:
            if suelo[self.posicion_x+1][self.posicion_y] == 0:
                self.posicion_x += 1
                self.rect.y += self.tamanio

        elif tecla[pygame.K_d]:
            if suelo[self.posicion_x][self.posicion_y+1] == 0:
                self.posicion_y += 1
                self.rect.x += self.tamanio

        elif tecla[pygame.K_a]:
            if suelo[self.posicion_x][self.posicion_y-1] == 0:
                self.posicion_y -= 1
                self.rect.x -= self.tamanio