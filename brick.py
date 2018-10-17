from pygame.sprite import Sprite
import pygame


class Brick(Sprite):

    def __init__(self, screen):
        super(Brick, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.size = 10

        self.image = pygame.image.load('images/brick.png')
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
