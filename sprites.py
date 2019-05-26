import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x
        self.y = y

    def get_keys(self):

        grounded = self.collide_with_walls('y')
        # grounded not used at present
        # set vx back to zero when pressing size keys to eliminate repeated movement after key is lifted
        self.vx = 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = PLAYER_SPEED
        # loop a few times if jumping
        if keys[pg.K_UP] or keys[pg.K_w]:
            if self.vy == 0:

                    self.vy = -JUMP_SPEED

        # used to calculate diagonal movement using pythagoras to ensure it is the same as regular
        # movement, but only for the grid/ top-down game
        # if self.vx != 0 and self.vy != 0:
            # self.vx *= 0.7071
            # self.vy *= 0.7071
        self.vy += GRAVITY

    def jump(self, dy=0):
        if not self.collide_with_walls(dy):
            self.y += dy

    def collide_with_walls(self, dir):
        colided_with_ground = False
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.width
                    colided_with_ground = True
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y

        return colided_with_ground


    def update(self):
        self.get_keys()
        self.y += self.vy * 0.01# * self.game.dt
        self.x += self.vx  * 0.01
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        collided = self.collide_with_walls('y')
        if collided:
            self.y -= self.vy *self.game.dt


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
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
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
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
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE