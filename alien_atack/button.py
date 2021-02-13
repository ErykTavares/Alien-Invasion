import pygame.font


class Button():
    """Classe que representa os bottoes na tela do game"""
    def __init__(self, ai_settings, screen, msg):
        super(Button, self).__init__()
        self.screen = screen
        self.screen_rect =  screen.get_rect()
        self.width, self.height = 200, 50
        self.buttom_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48, True, False)
        self.rect = pygame.Rect(0, 0 , self.width, self.height)
        self.rect.center = self.screen_rect.center 
        self.prep_msg(msg)

    
    def prep_msg(self, msg):
        """Prepara o texto do botão"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.buttom_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def  draw_button(self):
        """Desenha o texto e o botão na tela"""
        self.screen.fill(self.buttom_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

# copyright ErykTavares © 2020-2021