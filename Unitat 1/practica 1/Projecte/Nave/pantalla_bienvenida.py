import pygame
from variables import BLANCO, AZUL, ROJO, SCREEN_WIDTH

from pygame.locals import (
    K_ESCAPE,
    K_p,
    KEYDOWN,
    QUIT,
)


def draw(screen, clock):
    """Funcion que dibuja en pantalla la ventana de bienvenida y espera que pulses
     una tecla para salir(K_ESCAPE) o para continuar (K_p)"""
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
                    return True

        pygame.display.update()
