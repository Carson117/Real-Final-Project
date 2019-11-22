# Platform Game
import pygame as pg # everything is now pg. rather than pygames.
import random
from settings import * # Taking all the code from settings file
from sprites import * # Taking all the code from sprites file

class Game:
    def __init__(self):
        # initialize game window, etc, when the game starts up
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT)) #class variables
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True   #variable that controls whether or not the loop happens, refered to at the bottom,
        self.font_name = pg.font.match_font(FONT_NAME)



    def new(self):
        # start a new game, initializes the game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group() # Hold all the platforms for the collisions
        self.player = Player(self) # Spawn player
        self.all_sprites.add(self.player) # add to all_sprites group
        for plat in PLATFORM_LISTS:
            p = Platform(*plat) # exploding the list
            self.all_sprites.add(p) # add platform to all_sprites
            self.platforms.add(p) # add platform to platform
        self.run() # Whenever a new game starts, runs itself


    def run(self):
        # The actual Game Loop
        self.playing = True # whether or not the game is being played, controls it
        while self.playing:
            self.clock.tick(FPS)
            self.events() # defined, checks this each time
            self.update() # defined, checks this each time
            self.draw() # defined, checks this each time

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        # Check if player hits a platfrom - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top # take players y position and set it equal to whatever it hits to the top
                self.player.vel.y = 0 # once the player hits the top, the velocity is 0 and player stops falling
        # Scrolling, if player reaches top quarter of screen
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y) # move player position down
            for plat in self.platforms: # taking the platforms and moving them down
                plat.rect.y += abs(self.player.vel.y) # moving platform down at whatever speed the player is going
                if plat.rect.top >= HEIGHT: # top of platform goes off the bottom of the screen, kill that platform
                    plat.kill()
                    self.score += 1 # 1 point added everytime a platform disappears off screen

        # Die!
        if self.player.rect.bottom > HEIGHT: # hit the bottom of the screen
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0: # off the bottom of the screen, kill it
                    sprite.kill()
        if len(self.platforms) == 0:
            self.player = False

        # Spawn new platforms to keep same average number
        while len(self.platforms) < 6: # 5 starting, 1 above
            width = random.randrange(50, 100) # reandomize the width
            p = Platfrom(random.randrange(0, WIDTH-width) # spawn new platform, randomized
                        random.randrange(-75, -30),
                        width, 20)
            self.platfrom.add(p)
            self.all_sprites.add(p)



    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False # If user stops playing the game
                self.running = False # ends the loop at the bottom thats running the whole program
            if event.type == pg.KEYDOWN: # event for key press
                if event.key == pg.K_SPACE: # space bar
                    self.player.jump() # jump as a result

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.draw_text(self.score, 22, WHITE, WIDTH / 2, 15)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        self.screen.fill(BGCOLOR)
        self.draw_text(TITLE, 40, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Arrows to move, space to jump", 22, WHITE, WIDTH / 2, HEIGHT / 2) # directions to play, placement of directions
        self.draw_test("Press a key to play", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()


    def show_go_screen(self):
        # game over/continue
        if not self.running: # ignores game over screen, end this function
            return
        self.screen.fill(BGCOLOR)
        self.draw_text("Game Over", 40, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_test("Press a key to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key() # calling wait_for_key function

    def wait_for_key(self): # this is for the start screen and game over screen
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT: # X on the window
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False



    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.reader(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y) # placement of text
        self.screen.blit(text_surface, text_rect)

g = Game() # Make a new game object, instance of the game object, does everything in __init__(self)
g.show_start_screen() # after __init__ at the top in class Game is initialized, show the start screen
while g.running:  #loop for running the game
    g.new() # calss new to set up a new game
    g.show_go_screen() # game over screen

pg.quit() # if the other loops aren't meet, end
