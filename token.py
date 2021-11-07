import pygame as pg
from random import randint

class Token:
    rect: pg.Rect
    surface: pg.Surface

    def __init__(self, img: str, x_pos: int, y_pos: int):
        pg.sprite.Sprite.__init__(self)
        self.surface = pg.image.load(img)
        self.rect = self.surface.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

    def update(self) -> None:
        self.rect.x -= 5

class TokenSet:
    tokens: list[Token]

    def __init__(self):
        self.tokens = []
    
    def add_token(self, tok: Token) -> None:
        self.tokens.append(tok)
    
    def get_token_y() -> int:
        if (randint(0, 1) == 1):
            return randint(10, 200)
        else:
            y = 600

    def generate(self) -> None:
        y: int
        if (randint(0, 1) == 1):
            y = 0
        else:
            y = 600
        self.add_token(Token("intro_ball.gif", 800, y))