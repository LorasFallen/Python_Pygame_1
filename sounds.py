import pygame

class Sounds():
    def __init__(self):
        #Иниаицилизируем музыку
        self.sound_path = pygame.mixer.music
        self.shot = pygame.mixer.Sound('sound/bam2.wav')
        self.death = pygame.mixer.Sound('sound/death.wav')
        self.demon = pygame.mixer.Sound('sound/demon_death.wav')
        self.wave = pygame.mixer.Sound('sound/win_wave.wav')
        self.restart = pygame.mixer.Sound('sound/restart.wav')
        self.start_game = pygame.mixer.Sound('sound/start_game.wav')
        self.boss_shot = pygame.mixer.Sound('sound/boss_shot.wav')
        self.boss_res = pygame.mixer.Sound('sound/bos_res.wav')
        self.boss_win = pygame.mixer.Sound('sound/boss_win.mp3')
        self.lboss_start = pygame.mixer.Sound('sound/lboss_start.wav')
        self.win_lboss = pygame.mixer.Sound('sound/win_lboss.wav')

    def play_shot(self):
        #Звук выстрела
        self.shot.set_volume(0.2)
        self.shot.play()
    def death_sound(self):
        #Звук смерти
        self.death.set_volume(0.7)
        self.death.play()
    def demon_death(self):
        #Убийство моба
        self.demon.set_volume(0.2)
        self.demon.play()
    def win_wave(self):
        #Победа волны
        self.wave.set_volume(0.7)
        self.wave.play()
    def restart_sound(self):
        self.restart.set_volume(0.7)
        self.restart.play()
    def started_game(self):
        self.start_game.set_volume(0.7)
        self.restart.play()
    def bosses_shot(self):
        self.boss_shot.set_volume(0.2)
        self.boss_shot.play()
    def bosses_res(self):
        self.boss_res.set_volume(1)
        self.boss_res.play()
    def bosses_win(self):
        self.boss_win.set_volume(1)
        self.boss_win.play()
    def start_lboss(self):
        self.lboss_start.set_volume(1)
        self.lboss_start.play()
    def lboss_win(self):
        self.win_lboss.set_volume(1)
        self.win_lboss.play()