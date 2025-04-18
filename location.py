import pygame

class Location():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/Location1.jpg')
        self.image2 = pygame.image.load('images/Location2.jpg')
        self.image3 = pygame.image.load('images/Location_Boss.jpg')
        self.image_icon = pygame.image.load('images/icon.png')
    def draw_l_1(self):
        self.screen.blit(self.image, (0,0))
    def draw_l_2(self):
        self.screen.blit(self.image2, (0,0))
    def draw_l_3(self):
        self.screen.blit(self.image3,(0,0))