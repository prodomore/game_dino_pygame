import pygame
from pygame.sprite import Sprite
from app.utils.constants import DEFAULT_TYPE, RUNNING, JUMPING, DUCKING
from app.components.objets.text_manager import Text


DUCK_IMG = {DEFAULT_TYPE: DUCKING, }
RUN_IMG = {DEFAULT_TYPE: RUNNING, }
JUMP_IMG = {DEFAULT_TYPE: JUMPING, }

class Dinosaur(Sprite):
    X_POS = 80       #la posición horizontal inicial del jugador en el juego.
    Y_POS = 280        #la posición vertical inicial del jugador en el juego cuando no está agachado.
    Y_POS_DUCK = 320    #
    JUMP_VELOCITY = 8
    

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.reset_dino_rect()
        self.jump_velocity = self.JUMP_VELOCITY
        self.step_index = 0
        self.running = True
        self.jumping = False
        self.ducking = False
        self.speed = 5 #
    
        self.cactus_group = pygame.sprite.Group()
        self.actions = {
                        "running": self.run,
                        "jumping": self.jump,
                        "ducking": self.duck,
                        }


    def update(self, user_input):
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()
        if user_input[pygame.K_x] and self.dino_rect.x < self.screen_width - self.dino_rect.width:
            self.dino_rect.x += self.speed
        if user_input[pygame.K_c] and self.dino_rect.x > 0:
            self.dino_rect.x -= self.speed
        if user_input[pygame.K_SPACE]:
            self.jumping = True
        elif user_input[pygame.K_z]:
            self.ducking = True
        elif user_input[pygame.K_w] and self.dino_rect.y > 0:
            self.dino_rect.y -= self.speed
        elif user_input[pygame.K_q] and self.dino_rect.y < self.screen_height - self.dino_rect.height:
            self.dino_rect.y += self.speed
        else:
            self.ducking = False
        self.running = bool(user_input[pygame.K_r])

        #comprueba si el personaje está corriendo, saltando o agachándose
        action = None
        if self.running:
            action = "running"
        elif self.jumping:
            action = "jumping"
        elif self.ducking:
            action = "ducking"
   
        if action:
            self.actions[action]()
            
        if not self.jumping and not self.ducking:
            if user_input[pygame.K_SPACE]:
                self.jumping = True
                self.running = False
                self.ducking = False
            elif user_input[pygame.K_DOWN]:
                self.ducking = True
                self.running = False
                self.jumping = False
            else:
                self.running = True
                self.jumping = False
                self.ducking = False      

        if self.step_index >= 10:
            self.step_index = 0
        
        

    def run(self):
        image_index = self.step_index // 5 % len(RUN_IMG[self.type])
        self.image = RUN_IMG[self.type][image_index]
        self.reset_dino_rect()
        self.step_index += 1    

    def jump(self):
        if self.jumping:
            self.image = JUMP_IMG[self.type]
            self.dino_rect.y -= self.jump_velocity * 4
            self.jump_velocity -= 1
            if self.jump_velocity < -self.JUMP_VELOCITY:
                self.dino_rect.y = self.Y_POS
                self.jumping = False
                self.jump_velocity = self.JUMP_VELOCITY

    def duck(self):
        if self.ducking:
            self.image = DUCK_IMG[self.type][0] if self.step_index < 5 else DUCK_IMG[self.type][1]
            self.reset_dino_rect()
            self.dino_rect.y = self.Y_POS_DUCK
            self.step_index += 1




    def reset_dino_rect(self):
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))



