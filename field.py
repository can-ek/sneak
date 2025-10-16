import pygame
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SQUARE_WIDTH
from tailsquare import TailSquare


class Field(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)

    def spawn_new_square(self):
        x = random.randint(0, SCREEN_WIDTH - SQUARE_WIDTH - 1)
        y = random.randint(0, SCREEN_HEIGHT - SQUARE_WIDTH - 1)
        return TailSquare(x, y)
