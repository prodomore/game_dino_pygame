import random
from pygame.sprite import Sprite

from app.utils.constants import LARGE_CACTUS,SMALL_CACTUS


class Cactus(Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        if size == "large":
            self.image = random.choice(LARGE_CACTUS)
        elif size == "small":
            self.image = random.choice(SMALL_CACTUS)
        self.rect = self.image.get_rect() #la posisicon a dibujar
        self.rect.x = x
        self.rect.y = y
        self.speed = 10

    def update(self, game_speed, cactus):
        self.rect.x -= (game_speed + self.speed)
        if self.rect.right < 0:
            cactus.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)