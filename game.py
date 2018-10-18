import pygame
from eventloop import EventLoop
from maze import Maze
from pacman import Pacman
from settings import Settings


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((460, 510))
        pygame.display.set_caption("Pacman Portal")

        self.settings = Settings()

        self.maze = Maze(self.screen, mazefile='pacmap.txt')

        self.pacman = Pacman(self.screen)

    def __str__(self): return 'Game(Pacman Portal), maze=' + str(self.maze) + ')'

    def play(self):
        eloop = EventLoop(finished=False)
        while not eloop.finished:
            eloop.check_events(self.pacman)
            self.update_screen()
            self.maze.check_pac_pills(self.pacman, self.settings)

    def update_screen(self):
        self.maze.blitme()
        self.pacman.blitme(self.settings)
        pygame.display.flip()


game = Game()
game.play()
