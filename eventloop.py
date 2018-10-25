import pygame
import sys


class EventLoop:

    def __init__(self, finished):
        self.finished = finished

    def __str__(self):
        return 'eventloop, finished=' + str(self.finished) + ')'

    @staticmethod
    def check_events(pacman, menu, portal_enter, portal_exit, settings):
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
                elif event.key == pygame.K_SPACE:
                    print("Portal laying attempt")
                    if not settings.portal_enter_active:
                        portal_enter.attempt_spawn(pacman)
                        break
                    if not settings.portal_exit_active:
                        portal_exit.attempt_spawn(pacman)
                        break
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                menu.check_events(mouse_x, mouse_y)
