"""
Matariki Game
"""

import pygame
import random
import time

# define the size of the game board
bounds = (1000, 1000)

# directions
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


def main():
    # create the game
    pygame.init()
    window = pygame.display.set_mode(size=bounds, flags=pygame.SCALED)  # game window
    pygame.display.set_caption("Waka Game")  # title the game window

    # load images
    waka_img1 = pygame.image.load('waka1.png')
    waka_img2 = pygame.image.load('waka2.png')
    star_img = pygame.image.load('star.png')
    taniwha_img = pygame.image.load('taniwha.png')
    background_img = pygame.image.load('night_sky.png')
    game_over = pygame.image.load('game_over.png')

    # TODO: create the waka

    # initialise variables
    run = True  # to keep window open

    # game loop
    while run:
        """Update game"""
        # pause between loops
        pygame.time.delay(150)

        # get the next event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # check if user wants to quit (by pressing "Close Window")
                run = False

        """Moving the waka"""
        # TODO: change the direction of the waka
        keys = pygame.key.get_pressed()  # list of booleans of the keys that the user pressed/pressing
        if keys[pygame.K_LEFT]:
            pass
        elif keys[pygame.K_RIGHT]:
            pass
        elif keys[pygame.K_UP]:
            pass
        elif keys[pygame.K_DOWN]:
            pass
        # TODO: move the waka

        """Stars"""
        # TODO: spawn a star every 1 second

        """Drawing"""
        # draw the background
        window.blit(background_img, (0, 0))
        # TODO: draw the waka
        # TODO draw stars

        # update the game window
        pygame.display.flip()

        """Check boundaries"""
        # TODO: check if waka has hit boundary

    # end of the game
    print("Game over!")
    if run:
        window.blit(game_over, (375, 300))
        pygame.display.flip()
        t = time.time()
        while time.time() - t < 5:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return


class Waka:
    def __init__(self, coords):
        self.coords = coords
        self.direction = UP

    def draw(self, window, waka_img):
        """Draw the waka in the game window"""
        # TODO: rotate the waka to head in the correct direction
        pass

        # rotate the image
        waka_img = pygame.transform.rotate(waka_img, angle=0)

        # draw the waka
        x_waka, y_waka = self.coords  # coordinates of the waka
        window.blit(waka_img, (x_waka, y_waka))

    def move(self):
        """Move the waka in the direction it is heading"""
        x, y = self.coords  # x,y coordinates of the waka before moving
        # TODO

    def turn(self, direction):
        """Change the direction of the waka"""
        pass  # TODO

    def check_for_star(self, x_star, y_star):
        """True if waka has hit star, False otherwise"""
        x, y = self.coords  # x,y coordinates of the waka
        pass  # TODO

    def check_bounds(self, x_limit, y_limit):
        """True if waka has hit boundary, False otherwise"""
        x, y = self.coords  # x,y coordinates of the waka
        pass  # TODO


if __name__ == '__main__':
    main()
