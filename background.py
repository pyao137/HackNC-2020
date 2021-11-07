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

class Cloud:
    def __init__(self, img: str, x_pos: int, y_pos: int):
        self.surface = pg.image.load(img)
        self.surface = pg.transform.scale(pg.image.load(img), (100, 100))
        self.rect = self.surface.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

    def update(self) -> None:
        self.rect.x -= constants.CLOUD_MOVEMENT_SPEED

class CloudSet:
    def __init__(self):
        self.clouds: List[Cloud] = []
        for i in range(0, randint(3, 4)):
            self.clouds.append(Cloud("assets/cloud.png", randint(0, constants.SCREEN_WIDTH), randint(0, constants.SCREEN_HEIGHT)))

    def generate_cloud(self):
        x_pos: int = constants.SCREEN_WIDTH
        y_pos: int = randint(0, constants.SCREEN_HEIGHT)
        self.clouds.append(Cloud("assets/cloud.png", x_pos, y_pos))
    
    def clear_trash(self):
        for cloud in self.clouds:
            if cloud.rect.x <= 0:
                self.clouds.remove(cloud)
                del cloud
    
    def update(self):
        for cloud in self.clouds:
            cloud.update()

class StarSet:
    def __init__(self):
        self.stars: List[Star] = []
        for i in range(4, 6):
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