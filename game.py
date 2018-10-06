import pygame
from eventloop import EventLoop
from maze import Maze


class Game:
    BLACK  = (0, 0, 0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((680, 740))
        pygame.display.set_caption("Pacman Portal")

        self.maze = Maze(self.screen, mazefile='pacmap.txt',
                         brickfile='brick.png')

    def __str__(self): return 'Game(Pacman Portal), maze=' + str(self.maze) + ')'

    def play(self):
        eloop = EventLoop(finished=False)

        while not eloop.finished:
            eloop.check_events()
            self.update_screen()

    def update_screen(self):
        self.screen.fill(Game.BLACK)
        self.maze.blitme()
        pygame.display.flip()


game = Game()
game.play()
