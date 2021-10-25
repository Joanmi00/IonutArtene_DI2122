import pygame
import Juego
import os
import random
from pygame import RLEACCEL
from variables import carpeta,SCREEN_WIDTH,SCREEN_HEIGHT,BLANCO


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load(os.path.join(carpeta, "missile.png")).convert()
        self.surf.set_colorkey(BLANCO, RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(2 * Juego.nivel, 10 + 3 * Juego.nivel)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            Juego.set_punt(10)
            self.kill()
