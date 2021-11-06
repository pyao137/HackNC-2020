import pygame as pg
from pygame.locals import *
import pygame.mouse as mouse
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pg.Surface((75, 25))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()

    def update(self, mouseDown):
        currentHeight = self.surf.get_height()
        newHeight = min(max(self.surf.get_height() + 10 * ((2 * mouseDown)-1), 25), SCREEN_HEIGHT - 10)
        self.rect.move_ip(0, (currentHeight - newHeight)/2)
        self.surf = pg.Surface((self.surf.get_width(), newHeight))

    def increaseLength(self):
        self.surf = pg.Surface((self.surf.get_width() + 25, self.surf.get_height()))

screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

def main():
    plr = Player()
    plr.rect.centerx = SCREEN_WIDTH / 2
    plr.rect.centery = SCREEN_HEIGHT / 2

    running = True
    clock = pg.time.Clock()
    while running:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Check if mouse down, update size of player sprite
        plr.update(mouse.get_pressed()[0])

        # Check for collisions here


        # Draw the actual content
        screen.fill((255, 255, 255))
        screen.blit(plr.surf, plr.rect)
        pg.display.flip()

    pg.quit()

if __name__ == "__main__": main()
