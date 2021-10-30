import pygame
from variables import AZUL, BLANCO, ROJO, SCREEN_WIDTH
from pygame.locals import (QUIT, KEYDOWN, K_ESCAPE)


def dibujar(screen, clock, nivel, punt, punt_max, punt_max_ant):
    """Funcion que dibujaa en pantalla la pantalla final cuando es llamada"""
    pygame.mixer.music.pause()
    while True:
        texto_intro = pygame.font.SysFont('times', 30, True)
        clock.tick(27)
        screen.fill(AZUL)
        titulo = texto_intro.render('Finalizado ', True, ROJO)
        level = texto_intro.render("Nivel alcanzado {}".format(nivel), True, BLANCO)
        points = texto_intro.render('Puntuacion alcanzada {}'.format(punt), True, BLANCO)
        record = texto_intro.render('Un nuevo record {}'.format(punt_max), True, BLANCO)

        screen.blit(titulo, ((SCREEN_WIDTH // 2) - (titulo.get_width() // 2), 50))
        screen.blit(level, ((SCREEN_WIDTH // 2) - (level.get_width() // 2), 260))
        screen.blit(points, ((SCREEN_WIDTH // 2) - (points.get_width() // 2), 300))
        if punt_max > punt_max_ant:
            screen.blit(record, ((SCREEN_WIDTH // 2) - (record.get_width() // 2), 100))

        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    quit()
        pygame.display.update()
