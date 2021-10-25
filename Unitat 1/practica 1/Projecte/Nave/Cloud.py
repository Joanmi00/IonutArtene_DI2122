import pygame
import os
import random
from pygame import RLEACCEL
from variables import carpeta, NEGRO, SCREEN_HEIGHT, SCREEN_WIDTH


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load(os.path.join(carpeta, "cloud.png")).convert()
        self.surf.set_colorkey(NEGRO, RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )

        )
        self.speed = 5

        # Move the sprite based on speed
        # remove the sprite when it passes the left edge of the screen

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
