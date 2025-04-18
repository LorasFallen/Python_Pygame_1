from PIL.ImageChops import screen
from pygame.sprite import Group
import pygame.font
from hp import HP

class Scrores():
    #Игровой счёт
    def __init__(self, screen, stats):
        #Инициализируем очки
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (0, 0, 0)
        self.font = pygame.font.Font('font/Kereru.otf', 44)
        self.font_boss = pygame.font.Font('font/Kereru.otf', 50)
        self.image_life_men()
        self.image_wave()
        self.image_hp_boss()
        self.image_hp_lboss()

    def image_wave(self):
        self.wave_img = self.font.render(str(self.stats.wave_ines), True,(139,0,0))
        self.text_wave_img = self.font.render('Уничтожено волн:', True,self.text_color)
        self.text_wave_rect = self.text_wave_img.get_rect(topleft = (0, 10))
        self.wave_img_rect = self.wave_img.get_rect(topleft = (310, 10))
    def show_wave(self):
        self.screen.blit(self.wave_img, self.wave_img_rect)
        self.screen.blit(self.text_wave_img, self.text_wave_rect)

    def image_hp_boss(self):
        self.boss_hp_image = self.font_boss.render(str(self.stats.boss_hp), True, (139,0,0))
        self.text_boss_hp_image = self.font_boss.render('Здоровье босса:', True, self.text_color)
        self.boss_hp_image_rect = self.boss_hp_image.get_rect(topleft = (700, 100))
        self.text_boss_hp_image_rect = self.text_boss_hp_image.get_rect(topleft = (400, 100))
    def show_hp_boss(self):
        self.screen.blit(self.boss_hp_image, self.boss_hp_image_rect)
        self.screen.blit(self.text_boss_hp_image, self.text_boss_hp_image_rect)

    def image_hp_lboss(self):
        self.lboss_hp_image = self.font_boss.render(str(self.stats.last_boss_hp), True, (139,0,0))
        self.text_lboss_hp_image = self.font_boss.render('Здоровье босса:', True, self.text_color)
        self.lboss_hp_image_rect = self.lboss_hp_image.get_rect(topleft = (700, 100))
        self.text_lboss_hp_image_rect = self.text_lboss_hp_image.get_rect(topleft = (400, 100))
    def show_hp_lboss(self):
        self.screen.blit(self.lboss_hp_image, self.boss_hp_image_rect)
        self.screen.blit(self.text_lboss_hp_image, self.text_boss_hp_image_rect)

    def image_life_men(self):
        #Кол-во жизней
        self.lifes = Group()
        for life_number in range(self.stats.guns_left):
            men = HP(self.screen)
            men.rect.x = + 950 + life_number * men.rect.width
            men.rect.y = 10
            self.lifes.add(men)
    def show_life_men(self):
        self.lifes.draw(self.screen)