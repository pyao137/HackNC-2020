from tokens import TokenSet
from player import Player
from random import randint
import constants
from obstacles import ObstacleSet
from background import StarSet, CloudSet

class Map:
    def __init__(self, obs: ObstacleSet, toks: TokenSet, strs: StarSet, clds: CloudSet):
        self.obstacle_set: ObstacleSet = obs
        self.token_set: TokenSet = toks
        self.star_set: StarSet = strs
        self.cloud_set: CloudSet = clds
        self.interactable_count: int = 0
        self.background_count: int = 0

    def clear_trash(self) -> None:
        self.obstacle_set.clear_trash()
        self.token_set.clear_trash()
        self.star_set.clear_trash()
        self.cloud_set.clear_trash()

    def generate(self) -> None:
        if self.interactable_count % constants.INTERACTABLE_CYCLE == 0:
            i: int = randint(0, 40)
            if i <= 27:
                self.obstacle_set.generate()
            else:
                self.token_set.generate_token()
        if self.background_count % constants.BACKGROUND_CYCLE == 0:
            i: int = randint(0, 40)
            if i <= 30:
                self.star_set.generate_star()
            else:
                self.cloud_set.generate_cloud()
        self.interactable_count += 1
        self.background_count += 1
        if self.interactable_count == constants.RESET_GENERATION_COUNT:
            self.interactable_count = 0
        if self.background_count == constants.RESET_GENERATION_COUNT:
            self.background_Count = 0

    def check_for_collision(self, other: Player) -> bool:
        return self.obstacle_set.check_for_collisions(other)

    def check_for_token_eat(self, other: Player):
        self.token_set.check_eat(other)

    def update(self):
        self.token_set.update()
        self.obstacle_set.update()
        self.star_set.update()
        self.cloud_set.update()
        self.clear_trash()
        self.generate()
