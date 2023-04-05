
import random
from pygame.sprite import Sprite

from app.utils.constants import SUN1


class Sun(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = SUN1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, game_speed, sun_list):
        self.rect.x -= game_speed
        if self.rect.right < -3:
            sun_list.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
