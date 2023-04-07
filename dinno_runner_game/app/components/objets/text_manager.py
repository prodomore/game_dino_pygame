import pygame
from app.utils.constants import FONT_STYLE

class Text:
    def __init__(self, x, y, font_size, fon_text = FONT_STYLE):
        self.x = x
        self.y = y
        self.font_size = font_size
        self.font_color =  (0,0,0)
        self.font_family = fon_text
        self.font = pygame.font.SysFont(self.font_family, self.font_size)
    #es para generar la imagen de texto de un mensaje que se va a mostrar en la pantalla
    def send_messague(self, message): 
        self.text_send = self.font.render(message, True, self.font_color)

    #se encarga de mostrar el mensaje en la pantalla. Recibe como argumento el objeto screen
    def show(self, screen, message):
        self.send_messague(message)
        screen.blit(self.text_send, (self.x, self.y))
