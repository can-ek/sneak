import pygame
from constants import PLAYER_WIDTH, INITIAL_PLAYER_SPEED
from squareshape import SquareShape


class Player(SquareShape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.__speed = pygame.Vector2(0, 0)

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
        self.position += self.__speed * dt

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.square())

    def square(self):
        return pygame.Rect(
            self.position[0],
            self.position[1],
            PLAYER_WIDTH,
            PLAYER_WIDTH)

    def collides_with_border(self, width, height):
        return self.position[1] <= 0 \
            or self.position[1] + PLAYER_WIDTH >= height \
            or self.position[0] <= 0 \
            or self.position[0] + PLAYER_WIDTH >= width
