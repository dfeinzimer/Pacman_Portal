import pygame
from eventloop import EventLoop
from maze import Maze
from pacman import Pacman


class Game:
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((460, 510))
        pygame.display.set_caption("Pacman Portal")

        self.maze = Maze(self.screen,
                         mazefile='pacmap.txt',
                         brickfile='brick.png',
                         pillfile='pill/pill_regular.png',
                         powerpillfile='pill/pill_power.png')

        self.pacman = Pacman(self.screen)

    def __str__(self): return 'Game(Pacman Portal), maze=' + str(self.maze) + ')'

    def play(self):
        eloop = EventLoop(finished=False)
        while not eloop.finished:
            eloop.check_events()
            self.update_screen()

    def update_screen(self):
        self.maze.blitme()
        self.pacman.blitme()
        pygame.display.flip()


game = Game()
game.play()
