import pygame
from constants import *
from player import Player

def main():
  pygame.init()
  print("Starting Sneak!")
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  drawable = pygame.sprite.Group()
  Player.containers = (drawable)
  player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    for item in drawable:
      item.draw(screen)
    
    screen.fill(BACKGROUND_COLOR)
    pygame.display.flip()

if __name__ == "__main__":
  main()
