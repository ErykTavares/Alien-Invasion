class GameStats():
    def __init__(self, ai_settings):
        """Armazena e inicializa dados estatisticos """
        super(GameStats, self).__init__()
        self.ai_settings =  ai_settings
        self.high_score = None
        self.load_high_score()
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        self.score = 0
        self.ships_left = self.ai_settings.ship_limit
        self.level = 1

    
    def load_high_score(self):
        """Carrega a pontuação maxima"""
        with open(r"high_score.txt", "r") as hscore:
            for line in hscore:
                self.high_score = int(line)

    
    
