import pygame


class Settings:
    """classe que representa as funçoes do jogo"""
    def __init__(self):
        #screen configs
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = pygame.image.load("images\space.png")
        self.fps = 60
        self.game_icon = pygame.image.load(r"images\alien_icon.png")
        
        self.dynamic_configs()
        self.ship_limit = 3
        self.aliens_allowed = 24
        self.speedup_scale = 1.1
        self.alien_scale = 1.5


    def dynamic_configs(self):
        """Armazena as configuraçoes dinamica"""
        self.ship_speed_factor = 3
        self.bullet_speed = 3
        self.alien_speed_factor = 1
        self.bullet_allowed = 3
        self.alien_points = 50
    
    
    def increase_speed(self):
        """Aumenta a velocidade do game"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.alien_scale)
        
        if self.alien_speed_factor == 5:
            self.bullet_allowed += 1
        elif self.alien_speed_factor == 10:
            self.bullet_allowed += 1
