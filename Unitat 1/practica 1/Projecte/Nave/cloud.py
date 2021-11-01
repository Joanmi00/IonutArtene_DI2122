import pygame
import os
import random
from pygame import RLEACCEL
from variables import carpeta, NEGRO, SCREEN_HEIGHT, SCREEN_WIDTH


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        """Funcion que iniciara Cloud cuando llame a la class Cloud y los iniciara en posiciones aleatorias"""
        super(Cloud, self).__init__()
        self.surf = pygame.image.load(os.path.join(carpeta, "cloud.png")).convert()
        self.surf.set_colorkey(NEGRO, RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(20, SCREEN_HEIGHT-50),
            )

        )
        self.speed = 5

        # Move the sprite based on speed
        # remove the sprite when it passes the left edge of the screen

    def update(self):
        """"Funcion que acutalizara el movimiento de Cloud en la pantalla."""
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
