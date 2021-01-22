import pygame.font 

class ScoreBoard():
    def __init__(self, ai_settings, screen, stats):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        
        self.text_color = (34, 139, 34)
        self.font = pygame.font.SysFont(None, 48)
    
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    
    def prep_score(self):
        """Trasforma a pontuação em uma imagem"""
        round_score = round(self.stats.score, -1)
        score = f"{round_score:,}"
        self.score_image = self.font.render(score, True, self.text_color, None)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    

    def prep_high_score(self):
        """Transforma a pontuação maxima em uma imagem"""
        round_high_score = round(self.stats.high_score, -1)
        high_score = f"{round_high_score:,}"
        self.high_score_image = self.font.render(high_score, True, self.text_color, None)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top


    def prep_level(self):
        """Trasforma o level em uma imagem renderizada"""
        self.level_image = self.font.render(self.stats.level, True, self.text_color, None)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = +10


    def show_score(self):
        """Desenha a pontuação na tela"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)