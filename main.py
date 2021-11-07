import pygame as pg
import sys
from pygame.locals import *
import pygame.mouse as mouse
import math
from player import Player
from obstacles import ObstacleSet
from map import Map
from tokens import TokenSet

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

def main():
    plr = Player()
    plr.rect.centerx = SCREEN_WIDTH / 2
    plr.rect.centery = SCREEN_HEIGHT / 2

    running = True
    clock = pg.time.Clock()
    map: Map = Map(ObstacleSet(), TokenSet())
    while running:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Check if mouse down, update size of player sprite
        plr.update(mouse.get_pressed()[0])

        # Check for collisions here
        if map.check_for_collision(plr):
            print("test")
            break

        # Generate and clean up obstacles
        map.clear_trash()
        map.generate()

        # Draw the actual content
        screen.fill((255, 255, 255))
        for obstacle in map.obstacle_set.get_obstacles():
            for block in obstacle.get_blocks():
                screen.blit(block.surface, block.rect)
        for token in map.token_set.get_tokens():
            screen.blit(token.surface, token.rect) 
        screen.blit(plr.surf, plr.rect)
        pg.display.flip()
        map.update()

if __name__ == "__main__":
    main()
