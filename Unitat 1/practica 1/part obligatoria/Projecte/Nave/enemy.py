import pygame
import os
import random
from pygame import RLEACCEL

import juego
from variables import carpeta, SCREEN_WIDTH, SCREEN_HEIGHT, BLANCO


class Enemy(pygame.sprite.Sprite):
    def __init__(self, nivel):
        """Funcion que iniciara al enemigo cuando sea llamada la class Enemy en posiciones aletorias"""
        super(Enemy, self).__init__()
        self.surf = pygame.image.load(os.path.join(carpeta, "missile.png")).convert()
        self.surf.set_colorkey(BLANCO, RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(20, SCREEN_HEIGHT-20)
            )
        )

        self.speed = random.randint(2 * nivel, 10 + 3 * nivel)
        self.arriba = True

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen

    def update(self):
        """Funcion que actualizara el movimiento del enemigo por la pantalla"""
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
            return True
