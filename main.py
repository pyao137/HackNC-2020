import pygame as pg
from pygame.locals import *

screen = pg.display.set_mode([800, 600])

def main():
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            # Check if mouse down, update size of player sprite


        # Check for collisions here


        # Draw the actual content
        screen.fill((255, 255, 255))
        pg.draw.circle(screen, (0, 0, 255), (400, 300), 75)
        pg.display.flip()

    pg.quit()

if __name__ == "__main__": main()
