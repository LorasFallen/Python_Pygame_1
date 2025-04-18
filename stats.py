import pickle
class Stats():
    #Отслеживание статистики
    def __init__(self):
        # Инициализирует статистику
        self.reset_stats()
        self.run_game = 1
        self.boss_life = False
        self.wave_life = True
        self.lboss_life = False
    def reset_stats(self):
        #Изменение статистики
        self.guns_left = 0
        self.score = 0
        self.wave_ines = 0
        self.boss_hp = 0
        self.last_boss_hp = 0