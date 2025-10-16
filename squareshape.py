import pygame
from constants import SQUARE_WIDTH, SQUARE_COLOR


# Base class for the game objects
class SquareShape(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.color = SQUARE_COLOR
        self.rect = pygame.Rect(x, y, SQUARE_WIDTH, SQUARE_WIDTH)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self, dt):
        self.rect = pygame.Rect(
                self.position[0],
                self.position[1],
                SQUARE_WIDTH,
                SQUARE_WIDTH)

    def collide_with(self, other):
        return self.rect.colliderect(other)

    def set_color(self, new_color):
        self.color = new_color
