#Sprite classes for platform game

import pygame as pg
from settings import * # access settings
vec = pg.math.Vector2 # This is for velocity and acceleration, assign vec for vector

class Player(pg.sprite.Sprite): # Creating the player and player movement
    def __init__(self, game): # knows about the game class
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30, 40)) # size of sprite
        self.image.fill(YELLOW) # color of sprite
        self.rect = self.image.get_rect() # rectangle shape of sprite
        self.rect.center = (WIDTH / 2, HEIGHT / 2 ) # Starting position
        self.pos = vec(WIDTH / 2, HEIGHT / 2) # position vector
        self.vel = vec(0, 0) # Uses a vector in the front, velocity of the player when keys pressed, also in starting position
        self.acc = vec(0, 0) # Uses a vector in the front, acceleration of the player

    def jump(self):
        # jump only if standing on platform, collide with a platform
        self.rect.x += 1 # take rectangle of player, add 1 pixel below
        hits = pg.sprite.spritecollide(self, self.game.platfroms, False)
        self.rect.x -= 1 # move back up 1 pixel 
        if hits:
            self.vel.y = -PLAYER_JUMP

    def update(self):
        self.acc = vec(0, PLAYER_GRAV)   #falling speed, how velocity is changing over time
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]: # Pressing left arrow key
            self.acc.x = -PLAYER_ACC # calling player acceleration from settings
        if key[pg.K_RIGHT]: # Pressing right arrow key
            self.acc.x = PLAYER_ACC # calling player acceleration from settings

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION # faster you are going, the more friction is needed to slow the player, negative number to slow down, only applied in the x direction not the y
        #equations of motion, moving the character
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH: # if position is greater than the width, set to 0
            self.pos.x = 0
        if self.pos.x < 0: # # if position is less than 0, set it equal to the width
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos # calculated position of the player will always be midbottom


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h): # spawning new platform, size and where it is
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h)) # create the image
        self.image.fill(GREEN) # color of image
        self.rect = self.image.get_rect() #
        self.rect.x = x # placement of rect at specified x
        self.rect.y = y # placement of rect at specified y
