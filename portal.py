from pygame.sprite import Sprite
import pygame


class Portal(Sprite):
    def __init__(self, portal_type, screen, settings):
        super(Portal, self).__init__()
        self.settings = settings
        self.portal_type = portal_type  # Enter || Exit
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.size = 30
        if self.portal_type == "Enter":
            self.image = pygame.image.load('images/portal/blue.png')
        else:
            self.image = pygame.image.load('images/portal/orange.png')
        self.image_mode = 0
        self.rect = self.image.get_rect()
        self.center = None
        self.last_update_time = None
        self.cardinal = None
        self.time_set_active = None

    def __str__(self):
        return 'Portal: ' + str(self.portal_type)

    def attempt_spawn(self, pacman):
        if not self.settings.portal_enter_active:
            self.settings.portal_enter_active = True
            self.time_set_active = pygame.time.get_ticks()
            self.rect.x = pacman.rect.x
            self.rect.y = pacman.rect.y
            return
        elif self.settings.portal_exit_active == False and self.settings.portal_enter_active == True:
            self.settings.portal_exit_active = True
            self.time_set_active = pygame.time.get_ticks()
            self.rect.x = pacman.rect.x
            self.rect.y = pacman.rect.y
            return
        else:
            print("Enter and exit portals already active")

    def blitme(self):
        if self.portal_type == "Enter" and self.settings.portal_enter_active:
            self.screen.blit(self.image, self.rect)
        elif self.portal_type == "Exit" and self.settings.portal_exit_active:
            self.screen.blit(self.image, self.rect)
