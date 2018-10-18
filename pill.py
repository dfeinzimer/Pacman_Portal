from pygame.sprite import Sprite
import pygame


class Pill(Sprite):

    def __init__(self, screen):
        super(Pill, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.size = 10

        self.image = pygame.image.load('images/pill/pill_regular.png')
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class PowerPill(Pill):

    def __init__(self, screen):
        Pill.__init__(self, screen)
        self.image = pygame.image.load('images/pill/pill_power.png')
        self.rect = self.image.get_rect()
