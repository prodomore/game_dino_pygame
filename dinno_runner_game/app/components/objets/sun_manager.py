
import pygame
from app.components.objets.sun import Sun
from app.utils.constants import SCREEN_WIDTH


class SunManager:
    def __init__(self):
        self.suns = pygame.sprite.Group()
        self.spawn_rate = 300
        self.counter = 0

    def update(self, game_speed):
        self.counter += 1
        if self.counter >= self.spawn_rate:
            x = SCREEN_WIDTH + 50
            y = 30
            self.suns.add(Sun(x, y))
            self.counter = 0

        for sun in self.suns:
            sun.update(game_speed, self.suns)

    def draw(self, screen):
        for sun in self.suns:
            sun.draw(screen)
