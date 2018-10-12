from imagerect import ImageRect
class Pacman:

    def __init__(self, screen):
        self.screen = screen
        self.size = 30
        self.pacfile = 'pacman/pac0.png'
        self.brick = ImageRect(screen, self.pacfile, self.size, self.size)
