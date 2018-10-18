from pygame.sprite import Group
from brick import Brick
from pill import Pill
from pill import PowerPill
import pygame


class Maze:

    def __init__(self, screen, mazefile):
        # Define maze screen
        self.screen = screen

        self.SQUARE_SIZE = 10

        # Read maze layout
        self.filename = mazefile
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        self.deltax = self.deltay = self.SQUARE_SIZE

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

    def check_pac_pills(self, pacman, settings):

        if pygame.sprite.spritecollideany(pacman, self.pills):
            for _ in pygame.sprite.spritecollide(pacman, self.pills, True):
                settings.score_current += settings.pill_regular_value

        if pygame.sprite.spritecollideany(pacman, self.powerpills):
            for _ in pygame.sprite.spritecollide(pacman, self.powerpills, True):
                settings.score_current += settings.pill_power_value

    def blitme(self):
        for brick in self.bricks:
            self.screen.blit(brick.image, brick.rect)
        for pill in self.pills:
            self.screen.blit(pill.image, pill.rect)
        for powerpill in self.powerpills:
            self.screen.blit(powerpill.image, powerpill.rect)
