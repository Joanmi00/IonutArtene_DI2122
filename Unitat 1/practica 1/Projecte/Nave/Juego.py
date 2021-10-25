import pygame
import os
import Cloud
import Enemy
import Pantalla_bienvenida
import variables
from variables import SCREEN_HEIGHT, SCREEN_WIDTH, carpeta, ROJO, AZUL, NEGRO
import Pantalla_final
import Player
import Shots
import bases_de_datos

from pygame.locals import (
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,

)

nivel = 1
puntuacion = 0
punt_max_ant = 0
punt_max = 0
bol = 0
shield = True
running = True

VC = 100 + (450 - 50 + nivel)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def set_running(valor):
    global running
    running = valor


def set_nivel(level):
    global nivel
    nivel = level


def set_punt(points):
    global puntuacion
    puntuacion += points


def set_punt_max(points):
    global punt_max
    punt_max = points


def set_punt_max_ant(points):
    global punt_max_ant
    punt_max_ant = points


def set_bol(bol2):
    global bol
    bol = bol2


def set_shield(valor):
    global shield
    shield = valor


def mostrar_texto():
    texto_punt = pygame.font.SysFont('console', 30, True)
    punt = texto_punt.render("Points: {}".format(str(puntuacion)), True, ROJO)
    if puntuacion > 500:
        set_nivel(int(puntuacion / 500) + 1)
    nivell = texto_punt.render("LVL: {}".format(str(nivel)), True, ROJO)
    screen.blit(punt, (SCREEN_WIDTH - punt.get_width(), 40))
    screen.blit(nivell, (SCREEN_WIDTH - nivell.get_width(), 15))


def jugar():
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(carpeta, "Apoxode_-_Electric_1.ogg"))
    pygame.mixer.music.play(loops=-1)
    collision_sound = pygame.mixer.Sound(os.path.join(carpeta, "Collision.ogg"))

    shield = True

    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, VC)
    ADDCLOUD = pygame.USEREVENT + 2
    pygame.time.set_timer(ADDCLOUD, 1000)
    CHANGEDAY = pygame.USEREVENT + 3
    pygame.time.set_timer(CHANGEDAY, 20000)
    CHANGEDAY1 = pygame.USEREVENT + 4
    pygame.time.set_timer(CHANGEDAY1, 22000)
    CHANGEDAY2 = pygame.USEREVENT + 5
    pygame.time.set_timer(CHANGEDAY2, 25000)

    clouds = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    player = Player.Player()
    all_sprites.add(player)

    # setup the clock for a decent framerate
    clock = pygame.time.Clock()

    bases_de_datos.sql_conection()
    bases_de_datos.sql_table()
    pygame.mixer.music.pause()
    Pantalla_bienvenida.draw(screen, clock)
    pygame.mixer.music.unpause()

    while running:

        if shield:
            variables.draw_shield(screen, player.rect.centerx, player.rect.y + 13)

        # for loop through the event queue
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # if the Esc key is pressed then exit the main loop
                if event.key == K_ESCAPE:
                    set_punt_max(puntuacion)
                    bases_de_datos.sql_insert(punt_max, punt_max_ant)
                    Pantalla_final.dibujar(screen, clock, nivel, puntuacion, punt_max, punt_max_ant)
                # if the SPACE key is pressed shot a missile
                if event.key == K_SPACE:
                    new_bullet = Shots.Shots(player.rect.centerx + 20, player.rect.y + 13)
                    bullets.add(new_bullet)
                    all_sprites.add(new_bullet)

            # Check for QUIT event.If QUIT,then initiate final screen
            elif event.type == QUIT:
                Pantalla_final.dibujar(screen, clock, nivel, puntuacion, punt_max, punt_max_ant)

            # Add a new enemy
            elif event.type == ADDENEMY:
                # Create the new enemy and add it to spite groups
                new_enemy = Enemy.Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

            elif event.type == ADDCLOUD:
                # Create the new cloud and add it to sprite groups
                new_cloud = Cloud.Cloud()
                clouds.add(new_cloud)
                all_sprites.add(new_cloud)

            elif event.type == CHANGEDAY:
                if bol == 0:
                    set_bol(1)
                elif bol == 3:
                    set_bol(2)

            elif event.type == CHANGEDAY1:
                if bol == 1:
                    set_bol(2)
                elif bol == 2:
                    set_bol(1)

            elif event.type == CHANGEDAY2:
                if bol == 2:
                    set_bol(3)
                elif bol == 1:
                    set_bol(0)

        # Get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        # Update positions
        enemies.update()
        clouds.update()
        bullets.update()

        # Fill the screen
        if bol == 0:
            screen.fill(AZUL)
        if bol == 1:
            screen.fill((0, 76, 153))
        if bol == 2:
            screen.fill((0, 25, 51))
        if bol == 3:
            screen.fill(NEGRO)

        if pygame.sprite.spritecollide(player, enemies, True):

            if not shield:
                collision_sound.play()
                player.kill()
                set_punt_max(puntuacion)
                bases_de_datos.sql_insert(punt_max, punt_max_ant)
                Pantalla_final.dibujar(screen, clock, nivel, puntuacion, punt_max, punt_max_ant)
            else:
                shield = False

        if pygame.sprite.groupcollide(bullets, enemies, True, True):
            collision_sound.play()
            set_punt(50)

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        mostrar_texto()

        # Update the display
        pygame.display.flip()

        clock.tick(30)

    pygame.mixer.music.stop()
    pygame.mixer.quit()
    pygame.quit()


if __name__ == '__main__':
    jugar()
