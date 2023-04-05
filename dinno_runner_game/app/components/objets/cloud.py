import random
from pygame.sprite import Sprite

from app.utils.constants import CLOUDS


class Cloud(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = random.choice(CLOUDS)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2

    def update(self, game_speed, clouds):
        self.rect.x -= (game_speed + self.speed)
        if self.rect.right < 0:
            clouds.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
