from ghost import Ghost
import pygame


class Intro:
    def __init__(self, screen, settings):
        pygame.font.init()
        self.screen = screen
        self.settings = settings
        self.settings.mode = "Intro"
        self.inkey = Ghost(self.screen, 0, 150, 'images/ghost/inkey/inkey1.png', "Inkey")
        self.pinky = Ghost(self.screen, 0, 250, 'images/ghost/pinky/pinky1.png', "Pinky")
        self.blinky = Ghost(self.screen, 0, 350, 'images/ghost/blinky/blinky1.png', "Blinky")
        self.clyde = Ghost(self.screen, 0, 450, 'images/ghost/clyde/clyde1.png', "Clyde")

    def blitme(self):
        if pygame.time.get_ticks() > self.settings.max_intro_lifetime:
            self.settings.mode = "Menu"
        if pygame.time.get_ticks() > .75 * self.settings.max_intro_lifetime:
            self.inkey.cardinal = "Stopped"
            self.pinky.cardinal = "Stopped"
            self.blinky.cardinal = "Stopped"
            self.clyde.cardinal = "Stopped"
        self.inkey.blitme(self.settings)
        self.pinky.blitme(self.settings)
        self.blinky.blitme(self.settings)
        self.clyde.blitme(self.settings)
