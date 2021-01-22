import pygame 

class Ship:
    """classe que representa a nave do jogador"""
    def __init__(self,ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load(r"alien_atack\images\ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect() 
        self.rect.centerx = self.screen_rect.centerx 
        self.rect.bottom = self.screen_rect.bottom 
        self.moving_right, self.moving_left, self.moving_up, self.moving_down = False, False, False, False
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.bottom)
    
    
    def update(self):
        """atualiza a posição da nave"""
        if self.moving_up and self.rect.top > 0:
            self.center_y -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.ai_settings.ship_speed_factor 
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0 :
            self.center_x -= self.ai_settings.ship_speed_factor
        
        self.rect.centerx = self.center_x
        self.rect.bottom = self.center_y
    

    def center_ship(self):
        """Centraliza a nave na tela"""
        self.center_x = self.screen_rect.centerx
        self.center_y = self.screen_rect.bottom

        
    def blitme(self):
        """desenha a nave na tela""" 
        self.screen.blit(self.image, self.rect)

