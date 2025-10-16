from squareshape import SquareShape


class TailSquare(SquareShape):
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, screen):
        super().draw(screen)
