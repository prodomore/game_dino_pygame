import random
import pygame
from app.utils.constants import SCREEN_WIDTH
from app.components.objets.cactus import Cactus
from app.components.objets.text_manager import Text

class Cactus_Manager:
    def __init__(self, max_num_cactus = 6):
        self.cactus = pygame.sprite.Group()
        self.spawn_delay = 0 # timpo restante para generar el cactus
        self.min_spawn_delay = 50#tiempos minimos y maximos para generar un nuevo catus
        self.max_spawn_delay = 200
        self.max_cactus = max_num_cactus
        self.cactus_figth = 0
        self.text = Text(40, 90, 40, (255, 0, 0))

    def update(self, game_speed):
        self.spawn_delay -= 1 # si la cantidad de cactus en el juego es menor al numero maximo
        if len(self.cactus) < self.max_cactus and self.spawn_delay <= 0:
            x = SCREEN_WIDTH + 10
            y = 280
            size = random.choice(['small', 'large'])
            self.spawn_delay = random.randint(self.min_spawn_delay, self.max_spawn_delay)
            self.new_cactus = Cactus(x, y, size)
            self.cactus.add(self.new_cactus)
            self.cactus_figth +=1

        for cactus in self.cactus:
            cactus.update(game_speed, self.cactus)
            if cactus.rect.right <=0:
                self.cactus.remove(cactus)

    def draw(self, screen):
        for cactus in self.cactus:
            cactus.draw(screen)
        self.text.show(screen, f"Cactus generate: {self.cactus_figth}")
    



        






