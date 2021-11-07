import pygame as pg
import sys
from pygame.locals import *
from obstacles import ObstacleSet

screen = pg.display.set_mode([800, 600])

def main():
    obs: ObstacleSet = ObstacleSet()
    clock = pg.time.Clock()
    while 1:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()
        
        obs.clear_trash()
        obs.generate()
        screen.fill((0, 0, 0))
        for obstacle in obs.get_obstacles():
            for block in obstacle.get_blocks():
                screen.blit(block.surface, (block.pos_x, block.pos_y))
        pg.display.flip()
        obs.update()
        print(len(obs.get_obstacles()))

if __name__ == "__main__":
    main()
