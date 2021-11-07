import pygame as pg
import constants

class Player:
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pg.Surface((constants.PLAYER_LENGTH, constants.PLAYER_WIDTH))
        self.surf.fill(constants.BLACK)
        self.rect = self.surf.get_rect()

    def update(self, mouseDown, maxHeight):
        currentHeight = self.surf.get_height()
        newHeight = min(max(self.surf.get_height() + 10 * ((2 * mouseDown)-1), 25), maxHeight)
        self.rect.move_ip(0, (currentHeight - newHeight)/2)
        self.surf = pg.Surface((self.surf.get_width(), newHeight))

    def increaseLength(self):
        self.surf = pg.Surface((self.surf.get_width() + constants.PLAYER_LENGTH_GROWTH, self.surf.get_height()))        
        self.rect.move_ip(-25, 0)
