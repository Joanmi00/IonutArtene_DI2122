import os
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

directorio = os.path.dirname(__file__)
carpeta = os.path.join(directorio, 'resources')

# color palette
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (135, 206, 250)
ROJO = (255, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def draw_shield(screen,x,y):
    pygame.draw.circle(screen,ROJO,(x,y),32,1)
    pygame.display.update()