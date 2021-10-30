import pygame
import os
import cloud
import enemy
import pantalla_bienvenida
import variables
from variables import SCREEN_HEIGHT, SCREEN_WIDTH, carpeta, ROJO, AZUL, NEGRO
import pantalla_final
import player as pl
import shots
import powerup as sh
import bases_de_datos

from pygame.locals import (
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,

)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Juego():
    def __init__(self):
        """Funcion que inicia unas variables cuando es llamada la class Juego"""
        self.nivel = 1
        self.puntuacion = 0
        self.punt_max_ant = 0
        self.punt_max = 0
        self.bol = 0
        self.VC = int(50 + 200 / self.nivel)

    def set_nivel(self, level):
        self.nivel = level

    def set_punt(self, points):
        self.puntuacion += points

    def set_punt_max(self, points):
        self.punt_max = points

    def set_punt_max_ant(self, points):
        self.punt_max_ant = points

    def set_bol(self, bol2):
        self.bol = bol2

    def mostrar_texto(self):
        """Funcion que mostrara en la parte izquierda arriba, la puntuacion y el nivel """
        texto_punt = pygame.font.SysFont('console', 30, True)
        punt = texto_punt.render("Points: {}".format(str(self.puntuacion)), True, ROJO)
        if self.puntuacion > 500:
            self.set_nivel(int(self.puntuacion / 500) + 1)
        nivell = texto_punt.render("LVL: {}".format(str(self.nivel)), True, ROJO)
        screen.blit(punt, (SCREEN_WIDTH - punt.get_width(), 40))
        screen.blit(nivell, (SCREEN_WIDTH - nivell.get_width(), 15))

    def draw_shield(self, x, y):
        """Funcion quedibujara un escudo(circulo) alrededor de la nave cuando es llamada """
        pygame.draw.circle(screen, ROJO, (x, y), 32, 1)
        pygame.display.update()

    def jugar(self):
        """Funcion que contiene la logica del juego"""
        shield = True
        var_shield = 0
        var_shield2 = 0
        while True:
            # If shield is true will draw a shield around the player
            if shield:
                self.draw_shield(player.rect.centerx, player.rect.y + 13)

            # for loop through the event queue
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # if the Esc key is pressed then exit the main loop
                    if event.key == K_ESCAPE:
                        self.set_punt_max(self.puntuacion)
                        bases_de_datos.sql_insert(self.punt_max, self.punt_max_ant)
                        pantalla_final.dibujar(screen, clock, self.nivel, self.puntuacion, self.punt_max,
                                               self.punt_max_ant)
                    # if the SPACE key is pressed shot a missile
                    if event.key == K_SPACE:
                        new_bullet = shots.Shots(player.rect.centerx + 20, player.rect.y + 13)
                        bullets.add(new_bullet)
                        all_sprites.add(new_bullet)
                        if shield:
                            new_bullet2 = shots.Shots(player.rect.centerx, player.rect.top)
                            bullets.add(new_bullet2)
                            all_sprites.add(new_bullet2)
                        if var_shield2 != 0:
                            new_bullet3 = shots.Shots(player.rect.centerx, player.rect.bottom)
                            bullets.add(new_bullet3)
                            all_sprites.add(new_bullet3)

                # Check for QUIT event.If QUIT,then initiate final screen
                elif event.type == QUIT:
                    pantalla_final.dibujar(screen, clock, self.nivel, self.puntuacion, self.punt_max, self.punt_max_ant)

                # Add a new enemy
                elif event.type == ADDENEMY:
                    # Create the new enemy and add it to spite groups
                    new_enemy = enemy.Enemy(self.nivel)
                    enemies.add(new_enemy)
                    all_sprites.add(new_enemy)
                # Add a new cloud
                elif event.type == ADDCLOUD:
                    # Create the new cloud and add it to sprite groups
                    new_cloud = cloud.Cloud()
                    clouds.add(new_cloud)
                    all_sprites.add(new_cloud)
                # the next 3 CHANGEDAY will modify a number to change the screen color
                elif event.type == CHANGEDAY:
                    if self.bol == 0:
                        self.set_bol(1)
                    elif self.bol == 3:
                        self.set_bol(2)

                elif event.type == CHANGEDAY1:
                    if self.bol == 1:
                        self.set_bol(2)
                    elif self.bol == 2:
                        self.set_bol(1)

                elif event.type == CHANGEDAY2:
                    if self.bol == 2:
                        self.set_bol(3)
                    elif self.bol == 1:
                        self.set_bol(0)

                # If you kill 10 enemies it will create a power_up
                elif var_shield == 10:
                    new_shield = sh.Power_up()
                    escudos.add(new_shield)
                    all_sprites.add(new_shield)
                    var_shield = 0

            # Get the set of keys pressed and check for user input
            pressed_keys = pygame.key.get_pressed()
            player.update(pressed_keys)

            # Update positions
            for enem in enemies:
                if enem.update():
                    juegoini.puntuacion += 10
            clouds.update()
            bullets.update()
            escudos.update()

            # Fill the screen
            if self.bol == 0:
                screen.fill(AZUL)
            if self.bol == 1:
                screen.fill((0, 76, 153))
            if self.bol == 2:
                screen.fill((0, 25, 51))
            if self.bol == 3:
                screen.fill(NEGRO)
            # Controls is a player collides with a enemy ,if it's true will kill que enemy and the player
            # if it not have a shield, if it have a shield will disappear the shield
            if pygame.sprite.spritecollide(player, enemies, True):

                if not shield:
                    collision_sound.play()
                    player.kill()
                    self.set_punt_max(self.puntuacion)
                    bases_de_datos.sql_insert(self.punt_max, self.punt_max_ant)
                    pantalla_final.dibujar(screen, clock, self.nivel, self.puntuacion, self.punt_max, self.punt_max_ant)
                else:
                    shield = False
                    var_shield2 = 0
            # Controls if a player collides with a power_up if it have it will increase a variable that will activate
            # a new shot,if haven't a shield it will appear one.
            if pygame.sprite.spritecollide(player, escudos, True):
                if shield:
                    var_shield2 += 1

                if not shield:
                    shield = True
            # Controls if a bullet collides with a enemy and if it true will kill both and increase points in 50 points
            if pygame.sprite.groupcollide(bullets, enemies, True, True):
                var_shield += 1

                collision_sound.play()
                self.set_punt(50)
            # Will go through the loop and will draw them in the screen
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)

            self.mostrar_texto()

            # Update the display
            pygame.display.flip()
            # Controls the frame rate
            clock.tick(30)


if __name__ == '__main__':
    juegoini = Juego()
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    # pygame.mixer.music.load(os.path.join(carpeta, "Apoxode_-_Electric_1.ogg"))
    # pygame.mixer.music.play(loops=-1)
    collision_sound = pygame.mixer.Sound(os.path.join(carpeta, "Collision.ogg"))

    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, juegoini.VC)
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
    escudos = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    player = pl.Player()
    all_sprites.add(player)

    # setup the clock for a decent framerate
    clock = pygame.time.Clock()

    bases_de_datos.sql_conection()
    juegoini.punt_max_ant = bases_de_datos.sql_table()
    pygame.mixer.music.pause()

    juegoini.set_punt_max_ant(bases_de_datos.sql_read())
    pygame.mixer.music.unpause()
    if pantalla_bienvenida.draw(screen, clock):
        juegoini.jugar()
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    pygame.quit()
