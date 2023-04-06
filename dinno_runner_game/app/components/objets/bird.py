import random
from pygame.sprite import Sprite

from app.utils.constants import BIRD


class Bird(Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = random.choice(BIRD)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10

    def update(self, game_speed, bird):
        self.rect.x -= (game_speed + self.speed)
        if self.rect.right < 0:
            bird.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)