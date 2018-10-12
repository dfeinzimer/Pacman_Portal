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

        brick_r = self.brick.rect
        brick_w, brick_h = brick_r.width, brick_r.height

        pill_r = self.pill.rect
        pill_w, pill_h = pill_r.width, pill_r.height

        powerpill_r = self.pill.rect
        powerpill_w, powerpill_h = powerpill_r.width, powerpill_r.height

        for num_rows in range(len(self.rows)):
            row = self.rows[num_rows]
            for num_cols in range(len(row)):
                location = row[num_cols]
                if location == 'W':
                    self.bricks.append(pygame.Rect(num_cols * dx, num_rows * dy, brick_w, brick_h))
                if location == 'R':
                    self.pills.append(pygame.Rect(num_cols * dx, num_rows * dy, pill_w, pill_h))
                if location == 'P':
                    self.powerpills.append(pygame.Rect(num_cols * dx, num_rows * dy, powerpill_w, powerpill_h))

    def blitme(self):
        for rect in self.bricks:
            self.screen.blit(self.brick.image, rect)
        for rect in self.pills:
            self.screen.blit(self.pill.image, rect)
        for rect in self.powerpills:
            self.screen.blit(self.powerpill.image, rect)
