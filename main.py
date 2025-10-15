import sys
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, BACKGROUND_COLOR
from player import Player


def main():
    pygame.init()
    print("Starting Sneak!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(BACKGROUND_COLOR)
        updatable.update(dt)

        if player_1.collides_with_border(SCREEN_WIDTH, SCREEN_HEIGHT):
            print("Game Over!")
            sys.exit()

        # print(f'Player position: {player_1.position}')

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
