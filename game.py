from dashboard import Dashboard
from eventloop import EventLoop
from intro import Intro
from maze import Maze
from pacman import Pacman
from settings import Settings
import pygame


class Game:

    settings: Settings

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.settings.reset()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.intro = Intro(self.screen, self.settings)
        pygame.display.set_caption("Pacman Portal")

        self.maze = Maze(self.screen, mazefile='pacmap.txt')

        self.pacman = Pacman(self.screen)

        self.dashboard = Dashboard(self.screen)

    def __str__(self): return 'Game(Pacman Portal), maze=' + str(self.maze) + ')'

    def play(self):
        eloop = EventLoop(finished=False)
        while not eloop.finished:
            eloop.check_events(self.pacman)
            self.update_screen()

    def update_screen(self):
        self.screen.fill((0, 0, 0))
        if self.settings.mode == "Game":
            self.maze.check_pac_conditions(self.pacman, self.settings)
            self.maze.blitme(self.settings)
            self.pacman.blitme(self.settings)
            self.dashboard.blitme(self.settings)
        elif self.settings.mode == "Menu":
            pass
        elif self.settings.mode == "Intro":
            self.intro.blitme()
        pygame.display.flip()


game = Game()
game.play()
