import pygame
import sys


class EventLoop:

    def __init__(self, finished):
        self.finished = finished

    def __str__(self):
        return 'eventloop, finished=' + str(self.finished) + ')'

    @staticmethod
    def check_events(pacman, menu):
        menu = menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pacman.cardinal = "East"
                elif event.key == pygame.K_LEFT:
                    pacman.cardinal = "West"
                elif event.key == pygame.K_UP:
                    pacman.cardinal = "North"
                elif event.key == pygame.K_DOWN:
                    pacman.cardinal = "South"
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                menu.check_events(mouse_x, mouse_y)
