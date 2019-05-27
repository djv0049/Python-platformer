import pygame as pg
from settings import *
vec = pg.math.Vector2



class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.vel = vec(0, 0)  #
        self.pos = vec(x, y)  # replaces the following 4 variables
        # self.vx =0
        # self.vy = 0
        # self.x = x
        # self.y = y

    def get_keys(self):

        # grounded = self.collide_with_walls('y')
        # grounded not used at present
        # set vx back to zero when pressing size keys to eliminate repeated movement after key is lifted
        self.vel.x = 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vel.x = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vel.x = PLAYER_SPEED
        # loop a few times if jumping
        if keys[pg.K_UP] or keys[pg.K_w]:
            if self.vel.y == 0:

                    self.vel.y = -JUMP_SPEED
        self.vel.y += GRAVITY
        # used to calculate diagonal movement using pythagoras to ensure it is the same as regular
        # movement, but only for the grid/ top-down game
        # if self.vx != 0 and self.vy != 0:
        #    self.vx *= 0.7071
        #    self.vy *= 0.7071

    def jump(self, dy=0):
        if not self.collide_with_walls(dy):
            self.pos.y += dy

    def collide_with_walls(self, direction):
        collided_with_ground = False
        if direction == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x
        if direction == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                    collided_with_ground = True
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y

        return collided_with_ground

    def update(self):
        self.get_keys()
        self.pos += self.vel * 0.01
        # self.y += self.vy * 0.01  # * self.game.dt
        # self.x += self.vx * 0.01
        self.rect.x = self.pos.x
        self.collide_with_walls('x')
        self.rect.y = self.pos.y
        collided = self.collide_with_walls('y')
        if collided:
           # self.pos.y -= self.vel.y *0.01
            return


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image_surface = pg.Surface((TILESIZE, TILESIZE))
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Lava(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.lavas
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.lava_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Coin(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.coins
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE/2, TILESIZE/2))  # draws the coin in the top left quarter of the tile
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE