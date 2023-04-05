import pygame
from app.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Text:
    def __init__(self, x, y, font_size, font_color, fon_text = FONT_STYLE):
        self.x = x
        self.y = y
        self.font_size = font_size
        self.font_color = font_color
        self.font_family = fon_text
        self.font = pygame.font.SysFont(self.font_family, self.font_size)

    def send_messague(self, message): 
        self.text_send = self.font.render(message, True, self.font_color)

    def show(self, screen, message):
        self.send_messague(message)
        screen.blit(self.text_send, (self.x, self.y))
        
