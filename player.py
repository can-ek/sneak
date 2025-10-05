import pygame
from constants import PLAYER_WIDTH
from squareshape import SquareShape

class Player(SquareShape):
  def __init__(self, x, y):
    super().__init__(x, y)
    
  def draw(self, screen):
    pygame.draw.polygon(screen, (0, 0, 0), self.square(), 2)

  def square(self):
    a = self.position
    b = self.position + pygame.Vector2(self.position[0] + PLAYER_WIDTH, self.position[1])
    c = self.position + pygame.Vector2(self.position[0] + PLAYER_WIDTH, self.position[1] + PLAYER_WIDTH)
    d = self.position + pygame.Vector2(self.position[0], self.position[1] + PLAYER_WIDTH)
    return [a, b, c, d]