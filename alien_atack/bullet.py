import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """classe que representa os disparos da nave do jogador"""
    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(r"images\missil.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.speed = ai_settings.bullet_speed
        
    
    def update(self):
        """move o bullet para cima"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Desenha o bullet na tela"""
        self.screen.blit(self.image, self.rect)