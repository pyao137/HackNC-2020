import pygame as pg
from tokens import TokenSet
from player import Player
from random import randint
from obstacles import ObstacleSet

class Map:
    def __init__(self, obs: ObstacleSet, toks: TokenSet):
        self.obstacle_set: ObstacleSet = obs
        self.token_set: TokenSet = toks
    
    def clear_trash(self) -> None:
        self.obstacle_set.clear_trash()
        self.token_set.clear_trash()
    
    def generate(self) -> None:
        if (randint(0, 10) > 8):
            if (randint(0, 1) == 1):
                self.token_set.generate_token()
            else:
                self.obstacle_set.generate()
        
    def check_for_collision(self, other: Player) -> bool:
        return self.obstacle_set.check_for_collisions(other)
    
    def check_for_token_eat(self, other: Player):
        self.token_set.check_eat(other)
    
    def update(self):
        self.token_set.update()
        self.obstacle_set.update()