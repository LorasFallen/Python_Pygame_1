import pygame

class Last_Boss(pygame.sprite.Sprite):
    #Последний босс
    def __init__(self, screen):
        super(Last_Boss, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/last_boss.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.left + 1000
        self.rect.y = self.rect.top + 450
        self.x = float(self.rect.x)
    def draw(self):
        self.screen.blit(self.image, self.rect)
    def update(self):
        self.x -= 1
        self.rect.x = self.x
