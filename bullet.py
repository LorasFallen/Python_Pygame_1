import pygame
from sounds import Sounds
class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, gun):
      # Создаём пули внутри персонажа
      super(Bullet, self).__init__()
      self.screen = screen
      self.rect = pygame.Rect(0, 0, 20, 5)
      self.color = 255, 165, 0
      self.speed = 20
      self.rect.centerx = gun.rect.centerx
      self.rect.midright = gun.rect.midright
      self.x = float(self.rect.x)
    def update(self):
        #Перемещение пули вправо
        self.x += self.speed
        self.rect.x = self.x
    def draw_bullet(self):
        #Рисует пулю на экране
        pygame.draw.rect(self.screen, self.color, self.rect)

