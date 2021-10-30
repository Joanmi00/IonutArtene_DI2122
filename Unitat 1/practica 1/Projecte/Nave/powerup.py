import pygame
import os
import random
from variables import carpeta, SCREEN_WIDTH, SCREEN_HEIGHT,color
from pygame import RLEACCEL


class Power_up(pygame.sprite.Sprite):
    def __init__(self):
        """Funcion que inicia la class Power_up cuando llamas a la class Power_up"""
        super(Power_up, self).__init__()
        self.surf = pygame.transform.scale(
            pygame.image.load(os.path.join(carpeta, "shield.png")).convert(),
            (40, 30))
        self.surf.set_colorkey(color, RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 20),
                random.randint(0, SCREEN_HEIGHT)
            )
        )

        self.speed = 5

    # Move the sprite based on speed
    def update(self):
        """Funcion que mueve el enemigo en funcion de la velocidad
        y borrara(.kill) el enemigo una vez pase de la parte izquierda de la pantalla"""
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
