from pygame.sprite import Sprite
import pygame


class Pacman(Sprite):

    def __init__(self, screen):
        super(Pacman, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.size = 30

        self.image = pygame.image.load('images/pacman/pac0.png')
        self.image_mode = 0
        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = 285
        self.center = float(self.rect.centerx)

        self.last_update_time = 0

        self.cardinal = "West"

    def blitme(self):
        if pygame.time.get_ticks() - self.last_update_time > 100:
            # Update mouth position
            if self.image_mode == 0:
                self.image = pygame.image.load('images/pacman/pac1.png')
                self.image_mode = 1
            elif self.image_mode == 1:
                self.image = pygame.image.load('images/pacman/pac2.png')
                self.image_mode = 2
            elif self.image_mode == 2:
                self.image = pygame.image.load('images/pacman/pac3.png')
                self.image_mode = 3
            elif self.image_mode == 3:
                self.image = pygame.image.load('images/pacman/pac0.png')
                self.image_mode = 0

            # Update cardinal position
            if self.cardinal == "North":
                self.image = pygame.transform.rotate(self.image, 90)
            elif self.cardinal == "East":
                self.image = pygame.transform.rotate(self.image, 0)
            elif self.cardinal == "South":
                self.image = pygame.transform.rotate(self.image, 270)
            elif self.cardinal == "West":
                self.image = pygame.transform.rotate(self.image, 180)

            self.last_update_time = pygame.time.get_ticks()
            self.screen.blit(self.image, self.rect)

