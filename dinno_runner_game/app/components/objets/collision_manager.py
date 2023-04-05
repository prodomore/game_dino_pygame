import pygame

class CollisionManager:
    def __init__(self):
        self.score = 0

    def check_collision(self, dinosaur, cacti_group):
        # Verificar si el dinosaurio colisiona con un cactus
        for cactus in cacti_group:
            if pygame.sprite.collide_rect(dinosaur, cactus):
                self.score += 1
                print("¡Choque!")
                # Aquí puedes agregar cualquier otra acción que desees tomar cuando ocurra una colisión
