import pygame


class Game_menu():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.text_color = (0,0,0)
        self.image_go = pygame.image.load('images/menu.jpg')
        self.font_name = pygame.font.Font('font/Kereru.otf', 90)
        self.font = pygame.font.Font('font/Kereru.otf', 40)
        self.welcome_label = self.font_name.render('The Last Stronghold', True, self.text_color,)
        self.batton_start = self.font.render('Начать', True, self.text_color, (205,92,92))
        self.bs_rect = self.batton_start.get_rect(topleft = (500, 300))
        self.batton_exit = self.font.render('Выход', True, self.text_color, (205,92,92))
        self.be_rect = self.batton_exit.get_rect(topleft = (500, 400))
        self.batton_FAQ = self.font.render('Правила', True, self.text_color,(205,92,92))
        self.bf_rect = self.batton_FAQ.get_rect(topleft = (500, 350))
        self.game_menu()
    def game_menu(self):
        self.screen.blit(self.image_go,(0,0))
        self.screen.blit(self.welcome_label, (260, 100))
        self.screen.blit(self.batton_start, self.bs_rect)
        self.screen.blit(self.batton_exit, self.be_rect)
        self.screen.blit(self.batton_FAQ, self.bf_rect)