from imagerect import ImageRect
import pygame
from pygame.sprite import Group
from brick import Brick


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

        self.pills = []
        self.pill = ImageRect(screen, pillfile, sz, sz)

        self.powerpills = []
        self.powerpill = ImageRect(screen, powerpillfile, sz, sz)

        self.build(screen)

    def __str__(self): return 'maze(' + self.filename + ')'

    def build(self, screen):
        dx, dy = self.deltax, self.deltay

        pill_rect = self.pill.rect
        pill_width, pill_height = pill_rect.width, pill_rect.height

        powerpill_rect = self.pill.rect
        powerpill_width, powerpill_height = powerpill_rect.width, powerpill_rect.height

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
                    self.pills.append(pygame.Rect(number_of_columns * dx, number_of_rows * dy, pill_width, pill_height))
                if location == 'P':
                    self.powerpills.append(pygame.Rect(number_of_columns * dx, number_of_rows * dy,
                                           powerpill_width, powerpill_height))

    def blitme(self):
        for brick in self.bricks:
            self.screen.blit(brick.image, brick.rect)
        for rect in self.pills:
            self.screen.blit(self.pill.image, rect)
        for rect in self.powerpills:
            self.screen.blit(self.powerpill.image, rect)
