from pygame.sprite import Group
from brick import Brick
from pill import Pill
from pill import PowerPill
from ghost import Ghost
import pygame


class Maze:

    def __init__(self, screen, mazefile):
        # Define maze screen
        self.screen = screen

        self.SQUARE_SIZE = 11

        # Read maze layout
        self.filename = mazefile
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        self.deltax = self.deltay = self.SQUARE_SIZE

        self.bricks = Group()
        self.pills = Group()
        self.powerpills = Group()
        self.ghosts = Group()

        self.build(screen)

        self.spawn_ghosts()

    def __str__(self): return 'maze(' + self.filename + ')'

    def spawn_ghosts(self):
        inkey = Ghost(self.screen, -35, 260, 'images/ghost/inkey/inkey1.png')
        self.ghosts.add(inkey)
        pinky = Ghost(self.screen, 0, 260, 'images/ghost/pinky/pinky1.png')
        self.ghosts.add(pinky)
        blinky = Ghost(self.screen, 0, 204, 'images/ghost/blinky/blinky1.png')
        self.ghosts.add(blinky)
        clyde = Ghost(self.screen, 35, 260, 'images/ghost/clyde/clyde1.png')
        self.ghosts.add(clyde)

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

    def check_pac_conditions(self, pacman, settings):

        if pygame.sprite.spritecollideany(pacman, self.pills):
            for _ in pygame.sprite.spritecollide(pacman, self.pills, True):
                settings.score_current += settings.pill_regular_value

        if pygame.sprite.spritecollideany(pacman, self.powerpills):
            for _ in pygame.sprite.spritecollide(pacman, self.powerpills, True):
                settings.score_current += settings.pill_power_value

        if pygame.sprite.spritecollideany(pacman, self.bricks):
            if pacman.cardinal == "North":
                pacman.move_south(settings)

            if pacman.cardinal == "South":
                pacman.move_north(settings)

            if pacman.cardinal == "East":
                pacman.move_west(settings)

            if pacman.cardinal == "West":
                pacman.move_east(settings)

        if pacman.rect.right <= 0:
            pacman.rect.left = 505
        elif pacman.rect.left >= 505:
            pacman.rect.right = 0

    def blitme(self):
        for brick in self.bricks:
            self.screen.blit(brick.image, brick.rect)
        for pill in self.pills:
            self.screen.blit(pill.image, pill.rect)
        for powerpill in self.powerpills:
            powerpill.animate()
            self.screen.blit(powerpill.image, powerpill.rect)
        for ghost in self.ghosts:
            self.screen.blit(ghost.image, ghost.rect)
