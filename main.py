import sys
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, BACKGROUND_COLOR
from player import Player
from tailsquare import TailSquare
from field import Field


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
    tailSquares = pygame.sprite.Group()
    TailSquare.containers = (tailSquares, updatable, drawable)
    Field.containers = (updatable)

    Player.containers = (updatable)
    player_1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = Field()
    feed_square = field.spawn_new_square()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(BACKGROUND_COLOR)
        updatable.update(dt)

        if player_1.collides_with_border(SCREEN_WIDTH, SCREEN_HEIGHT):
            print("Game Over!")
            sys.exit()

        if feed_square.collide_with(player_1.squares[0].rect):
            player_1.add_square(feed_square)
            feed_square = field.spawn_new_square()

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
