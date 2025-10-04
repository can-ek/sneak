import pygame

# Base class for the game objects
class SquareShape(pygame.sprite.Sprite):
  def __init__(self, x, y):
    self.position = pygame.Vector2(x, y)

  def draw(self, screen):
    # sub-class must override
    pass

  def update(self, dt):
    # sub-class must overrid
    pass

  def collide_with(self,other):
    return self.position.distance_to(other.position) == 0