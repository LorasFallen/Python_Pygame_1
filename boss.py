import pygame

class Boss(pygame.sprite.Sprite):
    # Класс босса 1 уровня
    def __init__(self, screen):
        # Инициализируем, задаём начальную позицию
        super(Boss, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/Boss.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width + 800
        self.rect.y = self.rect.height + 300
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        # Вывод босса на экран
        self.screen.blit(self.image, self.rect)

    def update(self):
        # Перемещает врагов
        self.x -= 1.5
        self.rect.x = self.x

