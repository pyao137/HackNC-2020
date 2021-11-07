import pygame as pg
import constants
import os

class Player:
    def __init__(self):
        self.surf = pg.Surface((constants.PLAYER_LENGTH, constants.PLAYER_WIDTH))
        self.surf.fill(constants.BLACK)
        self.rect = self.surf.get_rect()

    def update(self, mouseDown, maxHeight):
        currentHeight = self.surf.get_height()
        newHeight = min(max(self.surf.get_height() + 10 * ((2 * mouseDown)-1), constants.PLAYER_WIDTH), maxHeight)
        self.rect.move_ip(0, (currentHeight - newHeight)/2)
        self.rect.height = newHeight
        self.surf = pg.Surface((self.surf.get_width(), newHeight))

    def increaseLength(self):
        currentLength = self.surf.get_width()
        newLength = min(currentLength + constants.PLAYER_LENGTH_GROWTH, constants.PLAYER_MAX_LENGTH)
        self.surf = pg.Surface((newLength, self.surf.get_height()))
        self.rect.width = newLength
        self.rect.move_ip(currentLength - newLength, 0)
