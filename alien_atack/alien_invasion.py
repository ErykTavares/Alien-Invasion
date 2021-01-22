import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from score_board import ScoreBoard


def run_game(): 
    """inicializa o jogo"""
    pygame.init()

#inicializa o botão na tela 
pygame.font.init()

#configuraçoes, status
ai_settings = Settings()
stats = GameStats(ai_settings)
fps = pygame.time.Clock()

#janela 
screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
pygame.display.set_caption("Alien Invasion")
pygame.display.set_icon(pygame.image.load(r"Projects\Alien-Invasion-\alien-\alien_atack\images\alien.png"))
play_button = Button(ai_settings, screen, "Play")
sb = ScoreBoard(ai_settings, screen, stats)
#nave, aliens, projeteis 
ship = Ship(ai_settings, screen)
bullets = Group()
aliens = Group()
gf.create_fleet(ai_settings, screen, ship, aliens) 

#loop de eventos principal do jogo
while True:
    if stats.game_active: 
        #atualiza a nave
        ship.update()
        #atualiza os projeteis
        gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
        #atualiza a frota
        gf.update_aliens(ai_settings, stats, screen,  ship,  aliens, bullets)
    
    #verifica os eventos do game
    gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
    #atualiza a tela 
    gf.Update_screen(ai_settings, stats, sb, screen, ship, aliens, bullets, play_button)
    #v-sync
    fps.tick(ai_settings.fps)
    run_game()
