from pygame.sprite import Sprite
import pygame


class Pill(Sprite):

    def __init__(self, screen):
        super(Pill, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.size = 10

        self.image = pygame.image.load('images/pill/regular.png')
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class PowerPill(Pill):

    def __init__(self, screen):
        Pill.__init__(self, screen)
        self.image = pygame.image.load('images/pill/power0.png')
        self.rect = self.image.get_rect()
        self.image_mode = 0
        self.last_update_time = 0

        self.screen.blit(self.image, self.rect)

    def animate(self):
        if pygame.time.get_ticks() - self.last_update_time > 200:
            # Update mouth position
            if self.image_mode == 0:
                self.image = pygame.image.load('images/pill/power0.png')
                self.image_mode = 1
            elif self.image_mode == 1:
                self.image = pygame.image.load('images/pill/power1.png')
                self.image_mode = 2
            elif self.image_mode == 2:
                self.image = pygame.image.load('images/pill/power2.png')
                self.image_mode = 3
            elif self.image_mode == 3:
                self.image = pygame.image.load('images/pill/power3.png')
                self.image_mode = 0
            self.last_update_time = pygame.time.get_ticks()
