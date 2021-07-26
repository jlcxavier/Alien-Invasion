import pygame
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf


def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    # definiu o tamanho da tela
    c_settings = Settings()
    screen = pygame.display.set_mode(
        (c_settings.screen_width, c_settings.screen_height))
    # definiu o nome da janela
    pygame.display.set_caption("Invasão Alienígena")

    # Cria o botão play
    play_button = Button(c_settings, screen, "Play")

    # Cria uma espaçonave
    ship = Ship(c_settings, screen)
    # Cria um grupo no qual serão armazenados os projéteis
    bullets = Group()
    aliens = Group()

    # Cria a frota de alienígenas
    gf.create_fleet(c_settings, screen, ship, aliens)

    # Cria uma instância para armazenar dados estatísticos do jogo
    stats = GameStats(c_settings)
    sb = Scoreboard(c_settings, screen, stats)

    # Inicia o laço principal do jogo
    while True:

        gf.check_events(c_settings, screen, stats, sb,
                        play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(c_settings, screen, stats,
                              sb, ship, aliens, bullets)
            gf.update_aliens(c_settings, stats, screen,
                             sb, ship, aliens, bullets)

        gf.update_screen(c_settings, screen, stats, sb,
                         ship, aliens, bullets, play_button)


run_game()
