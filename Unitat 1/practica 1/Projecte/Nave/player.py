import pygame
import os

from pygame.constants import RLEACCEL
from variables import SCREEN_WIDTH, SCREEN_HEIGHT, BLANCO, carpeta

pygame.mixer.init()

move_up_sound = pygame.mixer.Sound(os.path.join(carpeta, "Rising_putter.ogg"))
move_down_sound = pygame.mixer.Sound(os.path.join(carpeta, "Falling_putter.ogg"))

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        """Funcion que inicia el player y le pone la imagen al player"""
        super(Player, self).__init__()
        self.surf = pygame.transform.scale(
            pygame.image.load(os.path.join(carpeta, "jet.png")).convert(),
            (60, 30))
        self.surf.set_colorkey(BLANCO, RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        """Funcion para mover el player segun las teclas pulsadas"""
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            # move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            # move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
