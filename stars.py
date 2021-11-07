import constants
import pygame as pg
from random import randint
from typing import List

class Star:
    def __init__(self, img: str, x_pos: int, y_pos: int):
        self.surface = pg.image.load(img)
        self.rect = self.surface.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

    def update(self) -> None:
        self.rect.x -= constants.STAR_MOVEMENT_SPEED

class StarSet:
    def __init__(self):
        self.stars: List[Star] = []
        for i in range(0, 5):
            self.stars.append(Star("assets/star.png", randint(0, constants.SCREEN_WIDTH), randint(0, constants.SCREEN_HEIGHT)))

    def generate_star(self):
        x_pos: int = constants.SCREEN_WIDTH
        y_pos: int = randint(0, constants.SCREEN_HEIGHT)
        self.stars.append(Star("assets/star.png", x_pos, y_pos))
    
    def clear_trash(self):
        for star in self.stars:
            if star.rect.x <= 0:
                self.stars.remove(star)
                del star
    
    def update(self):
        for star in self.stars:
            star.update()