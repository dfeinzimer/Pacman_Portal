from pygame.sprite import Group
from brick import Brick
from pill import Pill
from pill import PowerPill


class Maze:
    SQUARE_SIZE = 10

    def __init__(self, screen, mazefile, pillfile, powerpillfile):
        self.screen = screen
        self.filename = mazefile
        self.deltax = self.deltay = Maze.SQUARE_SIZE
        sz = Maze.SQUARE_SIZE
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        self.bricks = Group()

        self.pills = Group()

        self.powerpills = Group()

        self.build(screen)

    def __str__(self): return 'maze(' + self.filename + ')'

    def build(self, screen):
        dx, dy = self.deltax, self.deltay

        for number_of_rows in range(len(self.rows)):
            row = self.rows[number_of_rows]
            for number_of_columns in range(len(row)):
                location = row[number_of_columns]
                if location == 'W':
                    brick = Brick(screen)
                    brick.rect.x = number_of_columns * dx
                    brick.rect.y = number_of_rows * dy
                    self.bricks.add(brick)
                if location == 'R':
                    pill = Pill(screen)
                    pill.rect.x = number_of_columns * dx
                    pill.rect.y = number_of_rows * dy
                    self.pills.add(pill)
                if location == 'P':
                    powerpill = PowerPill(screen)
                    powerpill.rect.x = number_of_columns * dx
                    powerpill.rect.y = number_of_rows * dy
                    self.powerpills.add(powerpill)

    def blitme(self):
        for brick in self.bricks:
            self.screen.blit(brick.image, brick.rect)
        for pill in self.pills:
            self.screen.blit(pill.image, pill.rect)
        for powerpill in self.powerpills:
            self.screen.blit(powerpill.image, powerpill.rect)
