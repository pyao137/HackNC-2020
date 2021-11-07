import pygame as pg
import constants
from random import randint
from player import Player
from typing import List

class Token:
    def __init__(self, img: str, x_pos: int, y_pos: int):
        pg.sprite.Sprite.__init__(self)
        self.surface = pg.image.load(img)
        self.rect = self.surface.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

    def update(self) -> None:
        self.rect.x -= constants.MOVEMENT_SPEED

class TokenSet:
    def __init__(self):
        self.tokens: List[Token] = []
    
    def generate_token(self) -> None:
        self.tokens.append(Token("assets/token.png", constants.SCREEN_WIDTH, self.get_token_y()))
    
    def get_token_y(self) -> int:
        if (randint(0, 1) == 1):
            return randint(constants.TOKEN_TOP_BOUND, constants.TOKEN_TOP_BOUND + constants.TOKEN_RANGE)
        else:
            return randint(constants.TOKEN_LOW_BOUND - constants.TOKEN_RANGE, constants.TOKEN_LOW_BOUND)

    def clear_trash(self) -> None:
        for token in self.tokens:
            if token.rect.x < 0:
                self.tokens.remove(token)
                del token

    def get_tokens(self) -> List[Token]:
        return self.tokens
    
    def update(self) -> None:
        for token in self.get_tokens():
            token.update()
    
    def check_eat(self, other: Player) -> bool:
        for token in self.tokens:
            if token.rect.colliderect(other.rect):
                other.increaseLength()
                self.tokens.remove(token)
