import pygame
from constants import SQUARE_WIDTH, INITIAL_PLAYER_SPEED, PLAYER_COLOR
from tailsquare import TailSquare


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.__speed = pygame.Vector2(0, 0)
        self.squares = [TailSquare(x, y)]
        self.squares[0].set_color(PLAYER_COLOR)
        self.__is_move_v = False

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and not self.__is_move_v:
            self.__speed = pygame.Vector2(0, INITIAL_PLAYER_SPEED * -1)
            self.__is_move_v = True
        if keys[pygame.K_DOWN] and not self.__is_move_v:
            self.__speed = pygame.Vector2(0, INITIAL_PLAYER_SPEED)
            self.__is_move_v = True
        if keys[pygame.K_LEFT] and self.__is_move_v:
            self.__speed = pygame.Vector2(INITIAL_PLAYER_SPEED * -1, 0)
            self.__is_move_v = False
        if keys[pygame.K_RIGHT] and self.__is_move_v:
            self.__speed = pygame.Vector2(INITIAL_PLAYER_SPEED, 0)
            self.__is_move_v = False

        self.squares[0].position += self.__speed * dt

        if len(self.squares) > 1:
            for i in range(1, len(self.squares)):
                self.squares[i].position = self.get_position(self.squares[i-1])

    def collides_with_border(self, width, height):
        return (self.squares[0].position[1] <= 0
                or self.squares[0].position[1] + SQUARE_WIDTH >= height
                or self.squares[0].position[0] <= 0
                or self.squares[0].position[0] + SQUARE_WIDTH >= width)

    def add_square(self, tail_square):
        tail_square.set_color(PLAYER_COLOR)
        tail_square.position = self.get_position(self.squares[-1])
        self.squares.append(tail_square)

    def get_position(self, sq1):
        normal = self.__speed.normalize()
        new_position = None

        if normal == pygame.Vector2(0, -1):  # going up, new square below
            new_position = pygame.Vector2(
                    sq1.position[0],
                    sq1.position[1] + SQUARE_WIDTH)
        elif normal == pygame.Vector2(0, 1):  # gowing down, new square top
            new_position = pygame.Vector2(
                    sq1.position[0],
                    sq1.position[1] - SQUARE_WIDTH)
        elif normal == pygame.Vector2(1, 0):  # going right, new square left
            new_position = pygame.Vector2(
                    sq1.position[0] - SQUARE_WIDTH,
                    sq1.position[1])
        else:  # going left, new square right
            new_position = pygame.Vector2(
                    sq1.position[0] + SQUARE_WIDTH,
                    sq1.position[1])

        return new_position
