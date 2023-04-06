import pygame
import random
from app.utils.constants import SCREEN_WIDTH
from app.components.objets.cactus import Cactus
from app.components.objets.bird import Bird
from app.components.objets.text_manager import Text
from app.components.dinosaur import Dinosaur


class Obstacle_game_man:
    def __init__(self):
        self.cactus = pygame.sprite.Group()
        self.birds = pygame.sprite.Group()
        self.spawn_delay = 0 
        self.min_spawn_delay = 50
        self.max_spawn_delay = 200
        self.min_spawn_delay_birds = 45
        self.max_spawn_delay_birds = 180
        self.max_cactus = 6
        self.max_birds = 2
        self.cactus_figth = 0
        self.bird_figth = 0
        self.total_points = 0
        self.text = Text(40, 100, 30, (0, 0, 0))
        self.text_bird = Text(40, 130, 30, (0, 0, 0))
        self.text_total = Text(40, 160, 30, (0, 0, 0))
        self.total_score = Text(800, 20, 30, (0, 0, 0))
        self.player = Dinosaur() 

    def update_cactus(self, game_speed):
        self.spawn_delay -= 1 
        if len(self.cactus) < self.max_cactus and self.spawn_delay <= 0:
            x = SCREEN_WIDTH + 5
            y = 280
            size = random.choice(['small', 'large'])
            self.spawn_delay = random.randint(self.min_spawn_delay, self.max_spawn_delay)
            new_cactus = Cactus(x, y, size)
            self.cactus.add(new_cactus)
            self.cactus_figth += 1

        for cactus in self.cactus:
            cactus.update(game_speed, self.cactus)
            if cactus.rect.right <=0:
                self.cactus.remove(cactus)

    def update_birds(self, game_speed):
        self.spawn_delay -= 1
        if len(self.birds) < self.max_birds and self.spawn_delay <= 0:
            x = SCREEN_WIDTH + 7
            y = 240
            self.spawn_delay = random.randint(self.min_spawn_delay_birds, self.max_spawn_delay_birds)
            new_bird = Bird(x, y)
            self.birds.add(new_bird)
            self.bird_figth += 1

        for bird in self.birds:
            bird.update(game_speed, self.birds)
            if bird.rect.right <=0:
                self.birds.remove(bird)

    def draw(self, screen):
        for cactus in self.cactus:
            cactus.draw(screen)
            if self.player.dino_rect.colliderect(cactus.rect):
                self.total_points += 1
                self.cactus_figth -= 1
                self.cactus.remove(cactus)
        for bird in self.birds:
            bird.draw(screen)
            if self.player.dino_rect.colliderect(bird.rect):
                self.total_points += 1
                self.bird_figth -= 1
                self.birds.remove(bird)
        self.text.show(screen, f"Total Cactus generados: {self.cactus_figth}")
        self.text_bird.show(screen, f"Total birds generados: {self.bird_figth}")
        self.text_total.show(screen, f"Total obstaculos generados: {self.total_points}")
