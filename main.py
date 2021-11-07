import pygame as pg
import pygame.mouse as mouse
import constants
from pygame.locals import *
from player import Player
from obstacles import ObstacleSet
from player import Player
from map import Map
from tokens import TokenSet
from stars import StarSet

screen = pg.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])

def main():
    plr = Player()
    plr.rect.centerx = 2 * constants.SCREEN_WIDTH / 3
    plr.rect.centery = constants.SCREEN_HEIGHT / 2

    running = True
    clock = pg.time.Clock()
    map: Map = Map(ObstacleSet(), TokenSet(), StarSet())
    while running:
        clock.tick(constants.FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        # Update map
        map.update()

        # Check if mouse down, update size of player sprite
        plr.update(mouse.get_pressed()[0], constants.SCREEN_HEIGHT - 10)

        #Generate content
        map.clear_trash()
        map.generate()

        # Check for collisions here
        if map.check_for_collision(plr):
            break
        map.check_for_token_eat(plr)

        # Draw the actual content
        screen.fill(constants.WHITE)
        for obstacle in map.obstacle_set.obstacles:
            for block in obstacle.blocks:
                screen.blit(block.surface, block.rect)
        for token in map.token_set.get_tokens():
            screen.blit(token.surface, token.rect) 
        for star in map.star_set.stars:
            screen.blit(star.surface, star.rect)
        screen.blit(plr.surf, plr.rect)
        pg.display.flip()

if __name__ == "__main__":
    main()
