import random
import pygame
from app.components.dinosaur import Dinosaur
from app.components.objets.sun_manager import SunManager
from app.components.objets.cloud_manager import Cloud_Manager
from app.components.objets.obstacle_game_manager import Obstacle_game_man
from app.utils.constants import BG, BG_GAME , FPS, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE
from app.components.objets.text_manager import Text


class Game:
    def __init__(self):

        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.background_image = pygame.transform.scale(BG_GAME, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 7
        self.x_pos_bg = 0
        self.y_pos_bg = 360
        self.text = Text(SCREEN_WIDTH/2, 20, 50, (0, 0, 0))

        self.sun_manager = SunManager()
        self.cloud_manager = Cloud_Manager()
        self.obstacles = Obstacle_game_man()
        self.dino_name = "pepe"
        self.player = Dinosaur()   


    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()
            

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.cloud_manager.update(self.game_speed)
        self.sun_manager.update(self.game_speed)
        self.obstacles.update_birds(self.game_speed)
        self.obstacles.update_cactus(self.game_speed)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.blit(self.background_image, (0, 0))
        self.draw_background()
        self.sun_manager.draw(self.screen)
        self.cloud_manager.draw(self.screen)
        self.obstacles.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()
        

    def draw_background(self):
        image_width = BG.get_width()
        self.text.show(self.screen,self.dino_name)
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
