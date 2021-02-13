import pygame.font, pygame
from pygame.sprite import Group
from ship import Ship 

class ScoreBoard():
    """Classe que armazena a pontuação do jogo"""
    def __init__(self, ai_settings, screen, stats):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        
        self.font = pygame.font.SysFont("Verdana", 25, True)
    
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ship_life()

    
    def prep_score(self):
        """Trasforma a pontuação em uma imagem"""
        self.score_color = (140, 7, 7)
        round_score = round(self.stats.score, -1)
        score = "Score " + f"{round_score:,}"
        
        self.score_image = self.font.render(score, True,self.score_color , None)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    

    def prep_high_score(self):
        """Transforma a pontuação maxima em uma imagem"""
        self.highscore_color = (0, 99, 14 )
        round_high_score = round(self.stats.high_score, -1)
        high_score = "High Score " + f"{round_high_score:,}"
        self.high_score_image = self.font.render(high_score, True,self.highscore_color, None)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top


    def prep_level(self):
        """Trasforma o level em uma imagem renderizada"""
        self.level_color = (11, 22 , 162)
        self.level_image = self.font.render("Level " + str(self.stats.level), True,self.level_color, None)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = 70


    def prep_ship_life(self):
        """Mostra a quantidade de vidas da nave"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.image = pygame.image.load("images\ship_life.png")
            ship.rect.x = 10 + ship_number * ship.rect.width 
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """Desenha a pontuação na tela"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

# copyright ErykTavares © 2020-2021