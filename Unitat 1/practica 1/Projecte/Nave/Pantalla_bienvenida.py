import pygame
import Juego
import bases_de_datos

from pygame.locals import (
    K_ESCAPE,
    K_p,
    KEYDOWN,
    QUIT,
)

# color palette
import variables

BLANCO = (255, 255, 255)
AZUL = (135, 206, 250)
ROJO = (255, 0, 0)

SCREEN_WIDTH = 800


def draw(screen, clock):
    pygame.font.init()
    while True:
        texto_intro = pygame.font.SysFont('console', 30, True)
        clock.tick(27)
        screen.fill(ROJO)
        titulo = texto_intro.render("Bienvenido ", True, AZUL)
        instrucciones = texto_intro.render('Pulse p para continuar ', True, BLANCO)

        screen.blit(titulo, ((SCREEN_WIDTH // 2) - (titulo.get_width() // 2), 10))
        screen.blit(instrucciones, ((SCREEN_WIDTH // 2) - (instrucciones.get_width() // 2), 300))

        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    quit()
                if event.key == K_p:
                    try:
                        Juego.set_punt_max_ant(bases_de_datos.sql_read())
                    except:
                        Juego.set_punt_max_ant(0)
                    Juego.set_running(True)
                    return
        pygame.display.update()
