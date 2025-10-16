import pygame
from constants import SQUARE_WIDTH, INITIAL_PLAYER_SPEED, PLAYER_COLOR
from tailsquare import TailSquare


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.__speed = pygame.Vector2(0, 0)
        self.squares = [TailSquare(x, y)]
        self.squares[0].set_color(PLAYER_COLOR)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.__speed = pygame.Vector2(0, INITIAL_PLAYER_SPEED * -1)
        if keys[pygame.K_DOWN]:
            self.__speed = pygame.Vector2(0, INITIAL_PLAYER_SPEED)
        if keys[pygame.K_LEFT]:
            self.__speed = pygame.Vector2(INITIAL_PLAYER_SPEED * -1, 0)
        if keys[pygame.K_RIGHT]:
            self.__speed = pygame.Vector2(INITIAL_PLAYER_SPEED, 0)

        if len(self.squares) > 1:
            for i in range(1, len(self.squares)):
                self.squares[i].position = self.squares[i-1].position
        self.squares[0].position += self.__speed * dt

    def collides_with_border(self, width, height):
        return (self.squares[0].position[1] <= 0
                or self.squares[0].position[1] + SQUARE_WIDTH >= height
                or self.squares[0].position[0] <= 0
                or self.squares[0].position[0] + SQUARE_WIDTH >= width)

    def add_square(self, tail_square):
        tail_square.set_color(PLAYER_COLOR)
        normal = self.__speed.normalize()

        if normal == pygame.Vector2(0, -1):  # going up, new square below
            tail_square.position = pygame.Vector2(
                    self.squares[-1].position[0],
                    self.squares[-1].position[1] + SQUARE_WIDTH)

        self.squares.append(tail_square)
