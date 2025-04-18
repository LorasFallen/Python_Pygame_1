import pygame

class Ino(pygame.sprite.Sprite):
    #Класс врага 1 уровня
    def __init__(self, screen):
        #Инициализируем, задаём начальную позицию
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/Monster1.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    def draw(self):
        #Вывод зомби на экран
        self.screen.blit(self.image, self.rect)

    def update(self):
        #Перемещает врагов
        self.x -= 2.5
        self.rect.x = self.x