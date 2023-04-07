import pygame
import random
from app.utils.constants import SCREEN_WIDTH
from app.components.dinosaur import Dinosaur
from pygame.sprite import Sprite
from app.utils.constants import LARGE_CACTUS,SMALL_CACTUS
from pygame.sprite import Sprite
from app.components.objets.text_manager import Text
from app.utils.constants import BIRD
from app.utils.constants import FONT_STYLE

class Obstacle(Sprite):
    def __init__(self, image: pygame.Surface):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH  
        self.passed = False
        self.has_collided = False 

    def update(self, game_sped, obstacles):
        self.rect.x -= game_sped
        if self.rect.x < -self.rect.width:
            obstacles.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def collide(self, player):
        if self.rect.colliderect(player.rect) and not self.collided:
            self.collided = True
            return True
        return False

class Cactus(Obstacle):
    def __init__(self, size):
        super().__init__(random.choice(LARGE_CACTUS if size == "large" else SMALL_CACTUS))
        self.rect = self.image.get_rect()

    def update(self, game_speed, cacti):
        self.rect.x -= (game_speed + Dinosaur.speed)
        if self.rect.right < 0:
            cacti.remove(self)


    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Bird(Obstacle):
    def __init__(self ):
        self.image = random.choice(BIRD)
        self.rect = self.image.get_rect()

    def update(self, game_speed, birds):
        self.rect.x -= (game_speed + Dinosaur.speed)
        if self.rect.right < 0:
            birds.remove(self)


    def draw(self, screen):
        screen.blit(self.image, self.rect)


class ObstacleManager():
    def __init__(self):
        self.obstacles = []
        self.cactus_bang = 0
        self.cactus_count = 0
        self.cactus_evaded = 0
        self.bird_bang = 0
        self.bird_count = 0
        self.bird_evaded = 0
        self.score_cactus = 0
        self.score_bird = 0
        self.score = 0
        self.text = Text(40,40,30)
        self.text1 = Text(40,70,30)
        self.text2 = Text(40,100,30)
        self.text3 = Text(40,130,30)
        self.text4 = Text(40,160,30)
        
    def update(self, game_speed, player, game):
        if not self.obstacles:
            probability = random.randint(0, 7)
            if probability <= 6:
                self.obstacles.append(Cactus("small"))
                self.cactus_count +=  1
            if probability <= 3:
                self.obstacles.append(Bird())
                self.bird_count += 1

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if obstacle.rect.right < player.rect.left and not obstacle.passed:
                obstacle.passed = True
                if isinstance(obstacle, Cactus):
                    self.cactus_evaded += 1
                    self.score_cactus += 100
                elif isinstance(obstacle, Bird):
                    self.bird_evaded += 1
                    self.score_bird += 75

            if obstacle.collide(player):
                if isinstance(obstacle, Cactus):
                    self.cactus_bang += 1
                    self.score_cactus -= 100
                elif isinstance(obstacle, Bird):
                    self.bird_bang += 1
                    self.score_bird -= 25
            
        self.score = self.score_cactus + self.score_bird
        
        #if self.score == -100:
            #game.playing = False
        
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
            if isinstance(obstacle, Cactus):
                self.text.render(f"Cactus Deaths: {self.cactus_bang}", (255, 255, 255))
                self.text1.render(f"Cactus Number: {self.cactus_count}", (255, 255, 255))
                self.text2.render(f"Cactus Evaded: {self.cactus_evaded}", (255, 255, 255))
            elif isinstance(obstacle, Bird):
                self.text3.render(f"Bird Deaths: {self.bird_bang}", (255, 255, 255))
                self.text4.render(f"Bird Number: {self.bird_count}", (255, 255, 255))
                self.text.render(f"Bird Evaded: {self.bird_evaded}", (255, 255, 255))
        self.text.render(f"Score: {self.score}", (255, 255, 255))











