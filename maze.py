from imagerect import ImageRect
import pygame


class Maze:
    SQUARE_SIZE = 10

    def __init__(self, screen, mazefile, brickfile, pillfile, powerpillfile):
        self.screen = screen
        self.filename = mazefile
        self.deltax = self.deltay = Maze.SQUARE_SIZE
        sz = Maze.SQUARE_SIZE
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        self.bricks = []
        self.brick = ImageRect(screen, brickfile, sz, sz)

        self.pills = []
        self.pill = ImageRect(screen, pillfile, sz, sz)

        self.powerpills = []
        self.powerpill = ImageRect(screen, powerpillfile, sz, sz)

        self.build()

    def __str__(self): return 'maze(' + self.filename + ')'

    def build(self):
        dx, dy = self.deltax, self.deltay

        brick_rect = self.brick.rect
        brick_width, brick_height = brick_rect.width, brick_rect.height

        pill_rect = self.pill.rect
        pill_width, pill_height = pill_rect.width, pill_rect.height

        powerpill_rect = self.pill.rect
        powerpill_width, powerpill_height = powerpill_rect.width, powerpill_rect.height

        for num_row in range(len(self.rows)):
            row = self.rows[num_row]
            for num_cols in range(len(row)):
                location = row[num_cols]
                if location == 'W':
                    self.bricks.append(pygame.Rect(num_cols * dx, num_row * dy, brick_width, brick_height))
                if location == 'R':
                    self.pills.append(pygame.Rect(num_cols * dx, num_row * dy, pill_width, pill_height))
                if location == 'P':
                    self.powerpills.append(pygame.Rect(num_cols * dx, num_row * dy, powerpill_width, powerpill_height))

    def blitme(self):
        for rect in self.bricks:
            self.screen.blit(self.brick.image, rect)
        for rect in self.pills:
            self.screen.blit(self.pill.image, rect)
        for rect in self.powerpills:
            self.screen.blit(self.powerpill.image, rect)
