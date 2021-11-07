import pygame as pg
from random import randint
from player import Player
        
class Block(pg.sprite.Sprite):
    def __init__(self, img: str, x_pos: int, y_pos: int):
        pg.sprite.Sprite.__init__(self)
        self.surface = pg.image.load(img)
        self.rect = self.surface.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

    def update(self) -> None:
        self.rect.x -= 5

class Obstacle:
    def __init__(self):
        self.num_blocks = randint(3, 5)
        self.blocks = []
        up_or_down: int = randint(0, 1)
        if up_or_down == 0:
            self.first_block = Block("img.png", 800, 0)
            self.blocks.append(self.first_block)
            self.build_obstacle_top()
        else:
            self.first_block = Block("img.png", 800, 600)
            self.blocks.append(self.first_block)
            self.build_obstacle_bottom()
    
    def build_obstacle_top(self) -> None:
        curr_x: int = 800
        curr_y: int = 0
        direction: int

        for i in range(1, self.num_blocks):
            direction = randint(0, 5)
            if direction <= 3:
                curr_y += self.first_block.surface.get_height()            
            elif direction == 4:
                curr_x += self.first_block.surface.get_width()
            else:
                curr_x -= self.first_block.surface.get_width()
            self.blocks.append(Block("img.png", curr_x, curr_y))
        
    def build_obstacle_bottom(self) -> None:
        curr_x: int = 800
        curr_y: int = 600
        direction: int

        for i in range(1, self.num_blocks):
            direction = randint(0, 5)
            if direction <= 3:
                curr_y -= self.first_block.surface.get_height()            
            elif direction == 4:
                curr_x += self.first_block.surface.get_width()
            else:
                curr_x -= self.first_block.surface.get_width()
            self.blocks.append(Block("img.png", curr_x, curr_y))
    
    def update(self) -> None:
        for block in self.blocks:
            block.update()
    
    def get_blocks(self) -> list[Block]:
        return self.blocks

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
        self.obstacles = []
    
    def generate(self) -> None:
        self.get_obstacles().append(Obstacle())
    
    def clear_trash(self) -> None:
        for obstacle in self.get_obstacles():
            if obstacle.check_for_removal():
                self.obstacles.remove(obstacle)      

    def get_obstacles(self) -> list[Obstacle]:
        return self.obstacles

    def update(self) -> None:
        for obstacle in self.get_obstacles():
            obstacle.update()

    def check_for_collisions(self, other: Player) -> bool:
        for obstacle in self.obstacles:
            if obstacle.collision_check(other):
                return True
        return False