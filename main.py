import pygame as pg
import sys
from pygame.locals import *
import pygame.mouse as mouse
import math
from player import Player
from obstacles import ObstacleSet

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

def main():
    plr = Player()
    plr.rect.centerx = SCREEN_WIDTH / 2
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
        plr.update(mouse.get_pressed()[0])

        # Check for collisions here
        if obs.check_for_collisions(plr):
            print("test")
            break

        # Generate and clean up obstacles
        obs.clear_trash()
        obs.generate()

        # Draw the actual content
        screen.fill((255, 255, 255))
        for obstacle in obs.get_obstacles():
            for block in obstacle.get_blocks():
                screen.blit(block.surface, block.rect)
        screen.blit(plr.surf, plr.rect)
        pg.display.flip()
        obs.update()

if __name__ == "__main__":
    main()
