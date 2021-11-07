import pygame as pg
from random import randint
        
class Block(pg.sprite.Sprite):
    pos_x: int
    pos_y: int
    surface: pg.Surface

    def __init__(self, img: str, x_pos: int, y_pos: int):
        pg.sprite.Sprite.__init__(self)
        self.surface = pg.image.load(img)
        self.pos_x = x_pos
        self.pos_y = y_pos

    def update(self):
        self.pos_x -= 5

    def inside(self, x: int, y: int) -> bool:
        if self.pos_x <= x <= self.pos_x + self.surface.get_width():
            if self.pos_y <= y <= self.pos_y + self.surface.get_height():
                return True
        return False


class Obstacle:
    blocks: list[Block]
    num_blocks: int
    first_block: Block

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
        if self.first_block.pos_x < 0:
            return True
        else:
            return False
    
    def collision_check(self) -> bool: #Checks if the four corners of some other surface is inside any of the blocks in the obstacle
        return False


class ObstacleSet:
    obstacles: list[Obstacle]

    def __init__(self):
        self.obstacles = []
    
    def add_obstacle(self, obs: Obstacle) -> None:
        self.get_obstacles().append(obs)
    
    def generate(self) -> None:
        if (randint(0, 4) < 1):
            self.add_obstacle(Obstacle())
    
    def clear_trash(self) -> None:
        for obstacle in self.get_obstacles():
            if obstacle.check_for_removal():
                self.obstacles.remove(obstacle)      

    def get_obstacles(self) -> list[Obstacle]:
        return self.obstacles

    def update(self) -> None:
        for obstacle in self.get_obstacles():
            obstacle.update()