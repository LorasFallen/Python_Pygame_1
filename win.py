import pygame


class Win():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.text_color = (0, 0, 0)
        self.image_win = pygame.image.load('images/win.jpg')
        self.font_gratitude = pygame.font.SysFont('arial',20)
        self.font_name = pygame.font.Font('font/Kereru.otf', 90)
        self.font = pygame.font.Font('font/Kereru.otf', 40)
        self.win_label = self.font_name.render('Ты победил!!!', True, self.text_color)
        self.wbatton_menu = self.font.render('Меню', True, self.text_color, (205, 92, 92))
        self.bwm_rect = self.wbatton_menu.get_rect(topleft=(500, 450))
        self.wbatton_exit = self.font.render('Выход', True, self.text_color, (205, 92, 92))
        self.bwe_rect = self.wbatton_exit.get_rect(topleft=(500, 500))
        self.gratitude_label = self.font_gratitude.render('Спасибо большое, что ознакомился с игрой! Для меня это первый опыт, я много ошибался, но благодарю, что ты дошёл до конца', True, self.text_color)
        self.fgratitude_label = self.font_gratitude.render( 'Так же благодарность Фадееву Даниле за терпение во время компиляции', True, self.text_color)
        self.game_win()

    def game_win(self):
        self.screen.blit(self.image_win, (0, 0))
        self.screen.blit(self.win_label, (350, 50))
        self.screen.blit(self.wbatton_menu, self.bwm_rect)
        self.screen.blit(self.wbatton_exit, self.bwe_rect)
        self.screen.blit(self.gratitude_label, (10, 150))
        self.screen.blit(self.fgratitude_label,(10,170))