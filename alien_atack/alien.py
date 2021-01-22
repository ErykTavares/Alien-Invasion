import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """classe que representa o alienigena"""
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image =  pygame.image.load(r"Projects\Alien-Invasion-\alien-\alien_atack\images\alien.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.moving = 1
        self.moving_down = self.rect.height

    def update(self): 
        """Atualiza a posição da frota """       
        self.x += self.ai_settings.alien_speed_factor * self.moving
        self.rect.x = self.x

    
    def blitme(self):
        """desenha o alienigena na tela"""
        self.screen.blit(self.image, self.rect)