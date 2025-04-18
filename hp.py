import pygame
from pygame.sprite import Sprite


class HP(Sprite):
    def __init__(self, screen):
        super(HP, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/HP.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

    def draw(self):
        self.screen.blit(self.image, self.rect)