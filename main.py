"""
Matariki Game
"""

import pygame
import random
import time

# define the size of the game board
bounds = (1000, 1000)
waka_width = waka_height = 40

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

    # create the waka
    waka = Waka(coords=(int(bounds[0] / 2), int(bounds[1] / 2)))

    # initialise variables
    run = True  # to keep window open
    stars = []  # list of stars currently in the game
    taniwhas = []  # list of taniwhas currently in the game
    speed = 1  # speed of the waka
    t_spawn_star = time.time()  # time when the last star was spawned
    t_remove_star = time.time()  # time when the last star was removed
    t_spawn_taniwha = time.time()  # time when the last taniwha was spawned
    t_remove_taniwha = time.time()  # time when the last taniwha was removed
    stars_collected = 0  # number of stars collected
    row_waka = True  # to change between waka images to give a 'rowing' effect

    # game loop
    while run:
        """Update game"""
        # pause between loops
        pygame.time.delay(int(150 - speed))

        # get the next event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # check if user wants to quit (by pressing "Close Window")
                run = False

        """Moving the waka"""
        # change the direction of the waka
        keys = pygame.key.get_pressed()  # list of booleans of the keys that the user pressed/pressing
        if keys[pygame.K_LEFT]:
            waka.turn(LEFT)
        elif keys[pygame.K_RIGHT]:
            waka.turn(RIGHT)
        elif keys[pygame.K_UP]:
            waka.turn(UP)
        elif keys[pygame.K_DOWN]:
            waka.turn(DOWN)

        # move the waka
        waka.move()

        """Stars"""
        # spawn a star every 1 second
        if time.time() - t_spawn_star > 1:
            x = random.randint(0, bounds[0] - 1)
            y = random.randint(0, bounds[1] - 1)
            stars.append((x, y))
            t_spawn_star = time.time()

        # check all stars currently in the game
        for i, (x_star, y_star) in enumerate(stars):
            if waka.check_hit(x_star, y_star):
                stars.pop(i)  # remove the star
                speed += 10  # increase the speed of the waka
                stars_collected += 1  # increment the star count
                break

            # remove stars at random
            if len(stars) > 3 and time.time() - t_remove_star > random.randint(2, 5):
                stars.pop(random.randint(0, len(stars) - 1))

        """Taniwhas"""
        # check all taniwhas in the game
        hit = False
        for i, (x_taniwha, y_taniwha) in enumerate(taniwhas):
            if waka.check_hit(x_taniwha, y_taniwha):
                hit = True  # end the game if a taniwha is hit
                break
        if hit:
            break

        # spawn a taniwha every 2 seconds
        if time.time() - t_spawn_taniwha > 2:
            x = random.randint(0, bounds[0] - 1)
            y = random.randint(0, bounds[1] - 1)
            taniwhas.append((x, y))
            t_spawn_taniwha = time.time()

        # remove a taniwha every 3 seconds
        if len(taniwhas) > 1 and time.time() - t_remove_taniwha > 3:
            taniwhas.pop(random.randint(0, len(taniwhas) - 1))
            t_remove_taniwha = time.time()

        """Drawing"""
        # draw the background
        window.blit(background_img, (0, 0))

        # draw the waka
        if row_waka:
            waka.draw(window, waka_img1)
            row_waka = False
        else:
            waka.draw(window, waka_img2)
            row_waka = True

        # draw stars
        for x_star, y_star in stars:
            window.blit(star_img, (x_star, y_star))

        # draw taniwhas
        for x_taniwha, y_taniwha in taniwhas:
            window.blit(taniwha_img, (x_taniwha-25, y_taniwha-25))

        # update the game window
        pygame.display.flip()

        """Check boundaries"""
        if waka.check_bounds(x_limit=bounds[0], y_limit=bounds[0]):
            break

    # end of the game
    print(f"\nGame over, You got {stars_collected} star{'s' if stars_collected != 1 else ''}!")
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

    def draw(self, window, img):
        """Draw the waka in the game window"""
        # rotate the waka to head in the correct direction
        if self.direction == DOWN:
            img = pygame.transform.rotate(img, 180)
        elif self.direction == LEFT:
            img = pygame.transform.rotate(img, 90)
        elif self.direction == RIGHT:
            img = pygame.transform.rotate(img, -90)

        # draw the waka
        window.blit(img, (self.coords[0] - waka_width, self.coords[1] - waka_height))

    def move(self):
        """Move the waka in the direction it is heading"""
        x, y = self.coords  # x,y coordinates of the waka
        dist = 20  # pixels moved in each step

        # determine coordinates after moving
        if self.direction == DOWN:
            y += dist
        elif self.direction == UP:
            y -= dist
        elif self.direction == RIGHT:
            x += dist
        elif self.direction == LEFT:
            x -= dist

        self.coords = x, y

    def turn(self, direction):
        """Change the direction of the waka"""
        self.direction = direction

    def check_hit(self, x_object, y_object):
        """True if waka has hit object, False otherwise"""
        x, y = self.coords
        r = waka_width / 2 + 15  # range which counts as hitting the object

        # check if object coordinates are the within range
        if (x - r <= x_object <= x + r) and (y - r <= y_object <= y + r):
            return True
        return False

    def check_bounds(self, x_limit, y_limit):
        """True if waka has hit boundary, False otherwise"""
        x, y = self.coords  # x,y coordinates of waka

        # check if coordinates are within boundaries
        if 0 < x < x_limit and 0 < y < y_limit:
            return False
        return True


if __name__ == '__main__':
    main()
