import pygame as pg
import sys
from pygame.locals import *
import pygame.mouse as mouse
import math
from obstacles import ObstacleSet
from player import Player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

def main():
    plr = Player()
    plr.rect.centerx = 2 * SCREEN_WIDTH / 3
    plr.rect.centery = SCREEN_HEIGHT / 2

    running = True
    clock = pg.time.Clock()
    obs: ObstacleSet = ObstacleSet()
    while running:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Check if mouse down, update size of player sprite
        plr.update(mouse.get_pressed()[0], SCREEN_HEIGHT - 10)

        # Check for collisions here


        # Generate and clean up obstacles
        obs.clear_trash()
        obs.generate()

        # Draw the actual content
        screen.fill((255, 255, 255))
        for obstacle in obs.get_obstacles():
            for block in obstacle.get_blocks():
                screen.blit(block.surface, (block.pos_x, block.pos_y))
        screen.blit(plr.surf, plr.rect)
        pg.display.flip()
        obs.update()

if __name__ == "__main__":
    main()
