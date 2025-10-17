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
        snapped_pos = self.snap_rect()
        self.rect = pygame.Rect(
                snapped_pos[0],
                snapped_pos[1],
                SQUARE_WIDTH,
                SQUARE_WIDTH)

    def collide_with(self, other):
        return self.rect.colliderect(other)

    def set_color(self, new_color):
        self.color = new_color

    def snap_rect(self):
        x_i = self.position[0]
        y_i = self.position[1]

        half_step = SQUARE_WIDTH // 2
        move_fwd_x = x_i % SQUARE_WIDTH >= half_step
        move_fwd_y = y_i % SQUARE_WIDTH >= half_step

        column = (x_i // SQUARE_WIDTH)
        row = (y_i // SQUARE_WIDTH)

        if move_fwd_x:
            column += 1
        if move_fwd_y:
            row += 1

        return pygame.Vector2(column * SQUARE_WIDTH, row * SQUARE_WIDTH)
