import pygame as pg
from random import randint

class Token:
    def __init__(self, img: str, x_pos: int, y_pos: int):
        pg.sprite.Sprite.__init__(self)
        self.surface = pg.image.load(img)
        self.rect = self.surface.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

    def update(self) -> None:
        self.rect.x -= 5

class TokenSet:
    def __init__(self):
        self.tokens = []
    
    def generate_token(self) -> None:
        y: int = self.get_token_y()
        self.tokens.append(Token("intro_ball.gif", 800, y))
    
    def get_token_y(self) -> int:
        if (randint(0, 1) == 1):
            return randint(10, 200)
        else:
            return randint(400, 590)

    def clear_trash(self) -> None:
        for token in self.tokens:
            if token.rect.x < 0:
                self.tokens.remove(token)
    
    def get_tokens(self) -> list[Token]:
        return self.tokens
    
    def update(self) -> None:
        for token in self.get_tokens():
            token.update()