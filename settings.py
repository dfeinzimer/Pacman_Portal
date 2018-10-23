class Settings:

    def __init__(self) -> object:
        self.fruit_remaining = None
        self.lives_remaining = None
        self.mode = None  # Game | Menu
        self.pacman_speed = None
        self.pill_regular_value = None
        self.pill_power_value = None
        self.score_current = None
        self.screen_height = None  # Map stops at 560
        self.screen_width = None

    def reset(self):
        self.fruit_remaining = 1
        self.lives_remaining = 2
        self.mode = "Game"  # Game | Menu
        self.pacman_speed = 3
        self.pill_regular_value = 10
        self.pill_power_value = 100
        self.score_current = 0
        self.screen_height = 630  # Map stops at 560
        self.screen_width = 505
