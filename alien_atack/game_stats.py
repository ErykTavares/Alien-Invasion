class GameStats():
    def __init__(self, ai_settings):
        """Armazena e inicializa dados estatisticos """
        super(GameStats, self).__init__()
        self.ai_settings =  ai_settings
        self.high_score = 0
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        self.score = 0
        self.ships_left = self.ai_settings.ship_limit
        self.level = 1
    
    
