import pygame as pg
import pygame.mouse as mouse
import constants
import os
from pygame.locals import *
from player import Player
from obstacles import ObstacleSet
from player import Player
from map import Map
from tokens import TokenSet
from background import StarSet, CloudSet

pg.init()
font = pg.font.Font("assets/slkscre.ttf", 32)
screen = pg.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])

def main():
    plr = Player()
    plr.rect.centerx = 2 * constants.SCREEN_WIDTH / 3
    plr.rect.centery = constants.SCREEN_HEIGHT / 2

    running = True
    clock = pg.time.Clock()
    map: Map = Map(ObstacleSet(), TokenSet(), StarSet(), CloudSet())
    score: int = 0
    while running:
        clock.tick(constants.FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        # Update map
        map.update()

        # Check if mouse down, update size of player sprite
        plr.update(mouse.get_pressed()[0], constants.SCREEN_HEIGHT - 10)

        # Check for collisions here
        if map.check_for_collision(plr):
            break

        score += map.check_for_token_eat(plr)

        # Draw the actual content
        screen.fill(constants.BGCOLOR)
        for star in map.star_set.stars:
            screen.blit(star.surface, star.rect)
        for cloud in map.cloud_set.clouds:
            screen.blit(cloud.surface, cloud.rect)
        for obstacle in map.obstacle_set.obstacles:
            for block in obstacle.blocks:
                screen.blit(block.surface, block.rect)
        for token in map.token_set.get_tokens():
            screen.blit(token.surface, token.rect) 

        facePosition = (plr.surf.get_width() - constants.PLAYER_WIDTH, plr.surf.get_height()/2 - constants.PLAYER_WIDTH/2)
        faceSize = (constants.PLAYER_WIDTH, constants.PLAYER_WIDTH)
        plr.surf.fill(constants.PLAYER_COLOR)
        plr.surf.blit(pg.transform.scale(pg.image.load(os.path.join("assets", "face.png")), faceSize), facePosition)
        screen.blit(plr.surf, plr.rect)
        pg.display.flip()
    
    game_over_running = True
    while game_over_running: 
        clock.tick(constants.FPS)
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over_running = False
        screen.fill(constants.GAME_OVER_COLOR)
        img = pg.image.load("assets/game_over.png")
        text = font.render('Score: ' + str(score), True, (0, 0, 0))
        screen.blit(text, (constants.SCREEN_WIDTH / 2 - text.get_width() / 2, constants.SCREEN_HEIGHT / 2 + (img.get_height() / 2) + 20))
        screen.blit(img, (constants.SCREEN_WIDTH / 2 - (img.get_width() / 2), constants.SCREEN_HEIGHT / 2 - (img.get_height() / 2)))
    print(score)

if __name__ == "__main__":
    main()
