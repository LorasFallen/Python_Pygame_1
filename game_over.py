import pygame
from sounds import Sounds
from stats import Stats


class Game_over():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.text_color = (0,0,0)
        self.image_go = pygame.image.load('images/go_fone.jpg')
        self.font = pygame.font.Font('font/Kereru.otf', 44)
        self.fon_label = pygame.font.Font('font/Kereru.otf', 150)
        self.restart_label = self.fon_label.render('Game Over', True, (139,0,0))
        self.batton_restart = self.font.render('Заново', True, self.text_color, (205,92,92))
        self.br_rect = self.batton_restart.get_rect(topleft = (500, 400))
        self.batton_menu = self.font.render('Меню', True, self.text_color, (205,92,92))
        self.bm_rect = self.batton_menu.get_rect(topleft = (500, 450))
        self.game_over()
    def game_over(self):
        self.screen.blit(self.image_go,(0,0))
        self.screen.blit(self.restart_label, (300, 100))
        self.screen.blit(self.batton_restart, self.br_rect)
        self.screen.blit(self.batton_menu, self.bm_rect)




