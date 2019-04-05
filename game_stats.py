class GameStats():
    """Armazena dados estatísticos"""

    def __init__(self, ai_settings):
        """Inicializa dados estatísticos"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # inicia em um estado inativo
        self.game_active = False

    def reset_stats(self):
        """Inicliaza dados que podem mudar durante o jogo"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0