import pygame
from pygame.sprite import Sprite
class Gun(Sprite):
    def __init__(self, screen):
        '''Инициализация персонажа'''
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/man.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.left + 30
        self.rect.centery = self.screen_rect.bottom - 60
        self.centerlr = float(self.rect.centerx)
        self.centertb = float(self.rect.centery)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False
        self.mtop = False
        self.mbottom = False
        self.shot = False
    def output(self):
        '''Рисует Персонажа'''
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        '''обновление позиции персонажа'''
        if self.mright and self.rect.right < self.screen_rect.right - 100:
            self.centerlr += 3
        if self.mleft and self.rect.left > - 60:
            self.centerlr -= 3
        if self.mtop and self.rect.top > 550:
                self.centertb -= 3
        if self.mbottom and self.rect.bottom < self.screen_rect.bottom + 40:
                self.centertb += 3
        self.rect.centerx = self.centerlr
        self.rect.centery = self.centertb

    def create_gun(self):
        #Место спавна персонажа
        self.rect.centerx = self.screen_rect.left + 30
        self.rect.centery = self.screen_rect.bottom - 60
        self.centerlr = float(self.rect.centerx)
        self.centertb = float(self.rect.centery)
        self.rect.bottom = self.screen_rect.bottom
