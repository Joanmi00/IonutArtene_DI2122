import pygame
import os
from variables import carpeta, BLANCO, SCREEN_WIDTH
from pygame import RLEACCEL


class Shots(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """Funcion que iniciara el disparo cuando sea llamado"""
        super(Shots, self).__init__()
        self.surf = pygame.transform.scale(
            pygame.image.load(os.path.join(carpeta, "missile_d.png")).convert(),
            (15, 7))
        self.surf.set_colorkey(BLANCO, RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.top = y
        self.rect.centerx = x
        self.speed = 20

    # Move the sprite based on speed
    def update(self):
        """Funcion que actualizara el movimiento del disparo por la pantalla"""
        self.rect.move_ip(self.speed, 0)
        if self.rect.left > SCREEN_WIDTH:
            self.kill()
