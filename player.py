import pygame as pg

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pg.Surface((75, 25))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()

    def update(self, mouseDown, maxHeight):
        currentHeight = self.surf.get_height()
        newHeight = min(max(self.surf.get_height() + 10 * ((2 * mouseDown)-1), 25), maxHeight)
        self.rect.move_ip(0, (currentHeight - newHeight)/2)
        self.surf = pg.Surface((self.surf.get_width(), newHeight))

    def increaseLength(self):
        self.surf = pg.Surface((self.surf.get_width() + 25, self.surf.get_height()))
        self.rect.move_ip(-25, 0)
