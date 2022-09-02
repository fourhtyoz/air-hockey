from .settings import *
import pygame
pygame.init()

class Game:
    def __init__(self, screen, width, height):
        self.width = width
        self.height = height
        self.screen = screen
    
    def draw(self):
        self.screen.fill(BLACK)


