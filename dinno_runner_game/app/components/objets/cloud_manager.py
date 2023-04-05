import pygame
import random
from app.components.objets.cloud import Cloud
from app.utils.constants import SCREEN_WIDTH

class Cloud_Manager:
    def __init__(self, max_clouds=4):

        self.clouds = pygame.sprite.Group()
        self.spawn_delay = 0
        self.min_spawn_delay = 100
        self.max_spawn_delay = 300
        self.max_clouds = max_clouds

    def update(self, game_speed):
        self.spawn_delay -= 1
        if len(self.clouds) < self.max_clouds and self.spawn_delay <= 0:
            x = SCREEN_WIDTH + 50
            y = 30
            self.clouds.add(Cloud(x, y))
            self.spawn_delay = random.randint(self.min_spawn_delay, self.max_spawn_delay)

        for cloud in self.clouds:
            cloud.update(game_speed, self.clouds)
            if cloud.rect.right < 0:
                self.clouds.remove(cloud)


    def draw(self, screen):
        for cloud in self.clouds:
            cloud.draw(screen)
