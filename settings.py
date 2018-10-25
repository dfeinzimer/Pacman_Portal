class Settings:

    def __init__(self) -> object:
        self.color_black = None
        self.color_white = None
        self.color_yellow = None
        self.fruit_remaining = None
        self.lives_remaining = None
        self.max_intro_lifetime = None
        self.mode = None  # Game || Menu || Intro
        self.speed_ghost = None
        self.speed_pacman = None
        self.pill_regular_value = None
        self.pill_power_value = None
        self.score_current = None
        self.screen_height = None  # Map stops at 560
        self.screen_width = None

    def reset(self):
        self.color_black = (0, 0, 0)
        self.color_white = (255, 255, 255)
        self.color_yellow = (255, 255, 0)
        self.fruit_remaining = 1
        self.lives_remaining = 2
        self.max_intro_lifetime = 10000
        self.mode = "Game"  # Game || Menu || Intro
        self.speed_ghost = 2
        self.speed_pacman = 3
        self.pill_regular_value = 10
        self.pill_power_value = 100
        self.score_current = 0
        self.screen_height = 630  # Map stops at 560
        self.screen_width = 505
