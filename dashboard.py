import pygame


class Dashboard:

    def __init__(self, screen):
        self.screen = screen

        pygame.font.init()

        self.score_font = pygame.font.SysFont('tlwgtypo', 50)
        print(pygame.font.get_fonts())
        self.scorelabel = self.score_font.render('SCORE:', False, (255, 255, 255))
        self.currentscore = self.score_font.render('0', False, (255, 255, 0))

    def update_score(self, settings):
        self.currentscore = self.score_font.render(str(settings.score_current), False, (255, 255, 0))

    def blitme(self, settings):
        self.update_score(settings)
        self.screen.blit(self.scorelabel, (0, 565))
        self.screen.blit(self.currentscore, (180, 565))
