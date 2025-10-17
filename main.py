import sys
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, BACKGROUND_COLOR_1, \
    BACKGROUND_COLOR_2, SQUARE_WIDTH
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
    background = pygame.Surface(screen.get_size())
    tiles = get_checkered_bg()
    [pygame.draw.rect(background, color, rect) for rect, color in tiles]

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

        updatable.update(dt)

        if player_1.collides_with_border(SCREEN_WIDTH, SCREEN_HEIGHT):
            print("Game Over!")
            sys.exit()

        if feed_square.collide_with(player_1.squares[0].rect):
            player_1.add_square(feed_square)
            feed_square = field.spawn_new_square()

        # Draw the background first
        screen.blit(background, (0, 0))

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


def get_checkered_bg():
    tile_size = SQUARE_WIDTH
    color_1 = BACKGROUND_COLOR_1
    color_2 = BACKGROUND_COLOR_2
    tiles = []

    for x in range((SCREEN_WIDTH + tile_size-1) // tile_size):
        for y in range((SCREEN_HEIGHT + tile_size-1) // tile_size):
            tiles.append((
                (x*tile_size, y*tile_size, tile_size, tile_size),
                color_1 if (x+y) % 2 == 0 else color_2
            ))
    return tiles


if __name__ == "__main__":
    main()
