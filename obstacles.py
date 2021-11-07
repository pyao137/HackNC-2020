import pygame as pg
import constants
from random import randint
import os
from random import randint, sample
from typing import List
from player import Player

blockAsset = os.path.join("assets", "block.png")

def getBlockColor():
    res = [255, 255, 255, 128]
    if randint(0, 1) == 0:
        for n in sample(range(0, 3), 2):
            res[n] = 0
    else:
        res[randint(0, 2)] = 0
    return res

class Block():
    def __init__(self, img: str, x_pos: int, y_pos: int, color: pg.Color):
        self.surface = pg.transform.scale(pg.image.load(img), (constants.BLOCK_SIZE, constants.BLOCK_SIZE))
        self.rect = self.surface.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

        colorSurface = pg.Surface((constants.BLOCK_SIZE, constants.BLOCK_SIZE), pg.SRCALPHA)
        colorSurface.fill(color)
        self.surface.blit(colorSurface, colorSurface.get_rect())

    def update(self) -> None:
        self.rect.x -= constants.MOVEMENT_SPEED

class Obstacle:
    def __init__(self, up_or_down: bool):
        self.num_blocks: int = randint(constants.MAX_BLOCKS_PER_OBSTACLE - 2, constants.MAX_BLOCKS_PER_OBSTACLE)
        self.blocks: List[Block] = []
        if up_or_down:
            self.first_block: Block = Block(blockAsset, constants.SCREEN_WIDTH, 0, getBlockColor())
            self.blocks.append(self.first_block)
            self.build_obstacle_top()
        else:
            self.first_block: Block = Block(blockAsset, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, getBlockColor())
            self.blocks.append(self.first_block)
            self.build_obstacle_bottom()

    def build_obstacle_top(self) -> None:
        curr_x: int = constants.SCREEN_WIDTH
        curr_y: int = 0
        direction: int
        num_horizontal_generations: int = 0

        for i in range(1, self.num_blocks):
            direction = randint(0, 5) #For determining whether to build vertically, left, or right
            if direction == 4 and num_horizontal_generations < constants.MAX_OBSTACLE_WIDTH:
                curr_x += self.first_block.surface.get_width()
                num_horizontal_generations += 1
            elif direction == 5 and num_horizontal_generations < constants.MAX_OBSTACLE_WIDTH:
                curr_x -= self.first_block.surface.get_width()
                num_horizontal_generations += 1
            else:
                curr_y += self.first_block.surface.get_height()
            self.blocks.append(Block(blockAsset, curr_x, curr_y, getBlockColor()))

    def build_obstacle_bottom(self) -> None:
        curr_x: int = constants.SCREEN_WIDTH
        curr_y: int = constants.SCREEN_HEIGHT
        num_horizontal_generations: int = 0
        direction: int

        for i in range(1, self.num_blocks):
            direction = randint(0, 5) #For determining whether to build vertically, left, or right
            if direction == 4 and num_horizontal_generations < constants.MAX_OBSTACLE_WIDTH:
                curr_x += self.first_block.surface.get_width()
                num_horizontal_generations += 1
            elif direction == 5 and num_horizontal_generations < constants.MAX_OBSTACLE_WIDTH:
                curr_x -= self.first_block.surface.get_width()
                num_horizontal_generations += 1
            else:
                curr_y -= self.first_block.surface.get_height()
            self.blocks.append(Block(blockAsset, curr_x, curr_y, getBlockColor()))

    def update(self) -> None:
        for block in self.blocks:
            block.update()

    def check_for_removal(self) -> bool:
        if self.first_block.rect.x < 0:
            return True
        else:
            return False

    def collision_check(self, other: Player) -> bool:
        for block in self.blocks:
            if block.rect.colliderect(other.rect):
                return True
        return False

class ObstacleSet:
    def __init__(self):
        self.obstacles: List[Obstacle] = []

    def generate(self) -> None:
        self.obstacles.append(Obstacle(True))
        self.obstacles.append(Obstacle(False))

    def clear_trash(self) -> None:
        for obstacle in self.obstacles:
            if obstacle.check_for_removal():
                self.obstacles.remove(obstacle) 
                del obstacle

    def get_obstacles(self) -> List[Obstacle]:
        return self.obstacles

    def update(self) -> None:
        for obstacle in self.obstacles:
            obstacle.update()

    def check_for_collisions(self, other: Player) -> bool:
        for obstacle in self.obstacles:
            if obstacle.collision_check(other):
                return True
        return False
