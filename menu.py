import pygame
from button import Button


class Menu:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        pygame.font.init()
        self.menu_font = pygame.font.SysFont('tlwgtypo', 30)
        self.GameTitle = self.menu_font.render('Pacman Portal', False, settings.color_yellow)
        self.button_play = Button(self.settings, self.screen, "Play Game")
        self.button_hiscores = Button(self.settings, self.screen, "High Scores")
        self.button_hiscores.make_high_scores_button("High Scores")

    def check_events(self, mouse_x, mouse_y):
        button_play_clicked = self.button_play.rect.collidepoint(mouse_x, mouse_y)
        button_hiscores_clicked = self.button_hiscores.rect.collidepoint(mouse_x, mouse_y)
        if button_play_clicked:
            self.settings.mode = "Game"
        elif button_hiscores_clicked:
            print(self.settings.score_high)

    def blitme(self):
        self.screen.blit(self.GameTitle, (130, 90))
        self.button_play.draw_button()
        self.button_hiscores.draw_button()
        pass
