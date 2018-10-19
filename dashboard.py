import pygame


class Dashboard:

    def __init__(self, screen):
        self.screen = screen

        pygame.font.init()

        self.score_font = pygame.font.SysFont('tlwgtypo', 30)
        print(pygame.font.get_fonts())
        self.scorelabel = self.score_font.render('SCORE:', False, (255, 255, 255))
        self.currentscore = self.score_font.render('0', False, (255, 255, 0))
        self.liveslabel = self.score_font.render('LIVES:', False, (255, 255, 255))

    def update_dash(self, settings):

        self.currentscore = self.score_font.render(str(settings.score_current), False, (255, 255, 0))

        for i in range(settings.lives_remaining):
            new_pac = pygame.image.load('images/pacman/pac2.png')
            self.screen.blit(new_pac, (320 + i * 40, 580))

        for i in range(settings.fruit_remaining):
            fruit = pygame.image.load('images/cherry.png')
            self.screen.blit(fruit, (455 + i * 40, 580))

    def blitme(self, settings):
        self.update_dash(settings)
        self.screen.blit(self.scorelabel, (10, 577))
        self.screen.blit(self.currentscore, (120, 577))
        self.screen.blit(self.liveslabel, (205, 577))
