import pygame
from config import *
import math
import random


# class Spritesheet:
#     def __init__(self, file):
#         self.sheet = pygame.image.load(file)
        
#     def get_sprite(self, x, y, width, height):
#         sprite = pygame.Surface([width, height])
#         sprite.blit(self.sheet, (0, 0), (x, y, width, height))
#         sprite.set_colorkey(BLACK)
#         return sprite


# class Player(pygame.sprite.Sprite):
#     def __init__(self, game, x, y):
        
#         self.game = game
#         self._layer = PLAYER_LAYER
#         self.groups = self.game.all_sprites
#         pygame.sprite.Sprite.__init__(self, self.groups)
        
#         self.x = x * TILESIZE
#         self.y = y * TILESIZE
#         self.width = TILESIZE
#         self.height = TILESIZE
        
#         self.x_change = 0
#         self.y_change = 0
        
#         self.facing = 'down'
        
#         self.animation_loop = 1
        
#         self.image = self.game.character_spritesheet.get_sprite(3,2,self.width,self.height)
        
#         # self.image = pygame.transform.scale(self.image, (50, 50))
        
        
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y
        
#     def update(self):
#         self.movement()
#         self.animate()
#         self.collide_enemy()
        
#         self.rect.x += self.x_change
#         self.collide_block('x')
#         self.rect.y += self.y_change
#         self.collide_block('y')
        
#         self.x_change = 0
#         self.y_change = 0
    
    


    # управление игрока
    
import pygame
from config import *
import math
import random


class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file)
        
    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite
# class Spritesheet:
#     def __init__(self, file):
#         self.sheet = pygame.image.load(file)
        
#     def get_sprite(self, x, y, width, height):
#         sprite = pygame.Surface([width, height])
#         sprite.blit(self.sheet, (0, 0), (x, y, width, height))
#         sprite.set_colorkey(BLACK)
#         return sprite


class Attack(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ATTACK_LAYER
        self.groups = self.game.all_sprites, self.game.attacks
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x
        self.y = y
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.image = self.game.attack_spritesheet.get_sprite(0, 0, self.width, self.height)
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update(self):
        self.rect.x += ATTACK_SPEED
        if self.rect.x > WIN_WIDTH:
            self.kill()


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.x_change = 0
        self.y_change = 0
        
        self.facing = 'down'
        
        self.animation_loop = 1
        
        self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update(self):
        self.movement()
        self.animate()
        self.collide_enemy()
        
        self.rect.x += self.x_change
        self.collide_block('x')
        self.rect.y += self.y_change
        self.collide_block('y')
        
        self.x_change = 0
        self.y_change = 0
    
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            for sprite in self.game.all_sprites:
                sprite.rect.x += PLAYER_SPEED
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -= PLAYER_SPEED
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            for sprite in self.game.all_sprites:
                sprite.rect.y += PLAYER_SPEED
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -= PLAYER_SPEED
            self.y_change += PLAYER_SPEED
            self.facing = 'down'
        

            
    def collide_enemy(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if hits:
            self.kill()
            self.game.playing = False
        
        
    
    def collide_block(self,direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right 
                    
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
        
    def animate(self):
        fick = [self.game.character_spritesheet.get_sprite(97, 99, self.width, self.height),
                self.game.character_spritesheet.get_sprite(128, 129, self.width, self.height),
                    self.game.character_spritesheet.get_sprite(163, 99, self.width, self.height)]
        up_down_animations =[self.game.character_spritesheet.get_sprite(64, 227, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(31, 228, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(0, 225, self.width, self.height)]

        
        if self.facing == "down":
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)
            else:
                self.image = up_down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
                    
        if self.facing == "up":
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)
            else:
                self.image = up_down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        if self.facing == "right":
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(97, 99, self.width, self.height)
            else:
                self.image = fick[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1  
        if self.facing == "left":
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(64, 0, self.width, self.height)
            else:
                self.image = fick[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1         

class Enemy(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        
        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.height = TILESIZE
        self.width = TILESIZE
        
        self.x_change = 0
        self.y_change = 0
        
        self.facing = random.choice(['left', 'right'])
        
        self.animation_loop = 1
        self.movement_loop = 0
        self.max_travel = random.randint(7,30)
        
        self.image = self.game.pumpkin.get_sprite(20,386,self.width, self.height)
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update(self):
        self.movement()
        
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        
        self.x_change = 0
        self.y_change = 0
    
    def movement(self):
        if self.facing == 'left':
            self.x_change -= ENEMY_SPEED
            self.movement_loop -= 1
            if self.movement_loop <= -self.max_travel:
                self.facing = 'right'
        if self.facing == 'right':
            self.x_change += ENEMY_SPEED
            self.movement_loop += 1
            if self.movement_loop >= self.max_travel:
                self.facing = 'left'
                    
    def animate(self):
        
        right = [self.game.pumpkin(144, 387, self.width, self.height),
                self.game.pumpkin(177, 385, self.width, self.height),
                self.game.pumpkin(144, 385, self.width, self.height)]
        left = [self.game.character_spritesheet.get_sprite(64, 227, self.width, self.height),
                self.game.character_spritesheet.get_sprite(31, 228, self.width, self.height),
                self.game.character_spritesheet.get_sprite(0, 225, self.width, self.height)]
        
        if self.facing == "right":
            if self.y_change == 0:
                self.image = self.game.character_spritesheet.get_sprite(240, 386, self.width, self.height)
            else:
                self.image = right[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1  
        # if self.facing == "left":
        #     if self.y_change == 0:
        #         self.image = self.game.character_spritesheet.get_sprite(64, 0, self.width, self.height)
        #     else:
        #         self.image = fick[math.floor(self.animation_loop)]
        #         self.animation_loop += 0.1
        #         if self.animation_loop >= 3:
        #             self.animation_loop = 1   
        
        
class Block(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites , self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.image = self.game.wall.get_sprite(160, 50, self.width, self.height)


        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Block2(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites , self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.image = self.game.tress.get_sprite(96, 190, self.width, self.height)


        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Ground(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game = game
        self._layer = GROUNDS_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE  
        
        self.image = self.game.grass.get_sprite(64,64,self.width,self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
class Wall_left(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game = game
        self._layer = GROUNDS_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE  
        
        self.image = self.game.wall_2.get_sprite(86,67,self.width,self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
                
class Ground2(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game = game
        self._layer = GROUNDS_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)
        
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE  
        
        self.image = self.game.grass.get_sprite(144,143,self.width,self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y        
# class Button:
#     def __init__(self,x,y,width,height,fg,bg,content,fontsize):
#         self.font = pygame.font.Font('arial.ttf', fontsize)
#         self.content = content
        
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
        
#         self.fg = fg
#         self.bg = bg
        
#         self.image = pygame.Surface((self.width, self.height))
#         self.image.fill(self.bg)
#         self.rect = self.image.get_rect()
        
#         self.rect.x = self.x
#         self.rect.y = self.y
        
#         self.text = self.font.render(self.content, True, self.fg)
#         self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
#         self.image.blit(self.text, self.text_rect)
        
#     def is_pressed(self,pos,pressed):
#         if self.rect.collidepoint(pos):
#             if pressed[0]:
#                 return True
#             return False
#         return False
    
class Button:
    def __init__(self,x,y,width,height,fg,bg,content,fontsize):
        self.font = pygame.font.Font('arial.ttf', fontsize)
        self.content = content
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.fg = fg
        self.bg = bg
        
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()
        
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)
        
    def is_pressed(self,pos,pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False
    
class ImageButton:
    def __init__(self, x, y, width, height, image):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (width, height))
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False
    
# class Attack(pygame.sprite.Sprite):
    
#     def __init__(self, game, x, y):
       
        
        
#         self.game = game
#         self._layer = PLAYER_LAYER
#         self.groups = self.game.all_sprites, self.game.attack
#         pygame.sprite.Sprite.__init__(self, self.groups)
        
#         self.x = x
#         self.y = y
#         self.width = TILESIZE
#         self.height = TILESIZE
        
#         self.animation_loop = 0
#         self.image = self.game.attack.get_sprite(0,0, self.width, self.height)
        
#         self.rect = self.image.get_rect()
#         self.rect.x = self.x
#         self.rect.y = self.y
        
#     def update(self):
#         self.animate()
#         self.collide()
        
#     def collide(self):
#         hits = pygame.sprite.spritecollide(self, self.game.enemies, True)
        
#     def animate(self):
#         direction = self.game.player.facing
        
#         right_animations = [self.game.attack_spritesheet.get_sprite(0, 0, self.width, self.height),
#                             self.game.attack_spritesheet.get_sprite(32, 0, self.width, self.height),
#                             self.game.attack_spritesheet.get_sprite(64, 0, self.width, self.height),
#                             self.game.attack_spritesheet.get_sprite(96, 0, self.width, self.height),
#                             self.game.attack_spritesheet.get_sprite(128, 0, self.width, self.height),
#                             self.game.attack_spritesheet.get_sprite(160, 0, self.width, self.height),
#                             self.game.attack_spritesheet.get_sprite(192, 0, self.width, self.height),
#                             self.game.attack_spritesheet.get_sprite(224, 0, self.width, self.height)]

#         # down_animations = [self.game.attack_spritesheet.get_sprite(0, 32, self.width, self.height),
#         #                     self.game.attack_spritesheet.get_sprite(32, 32, self.width, self.height),
#         #                     self.game.attack_spritesheet.get_sprite(64, 32, self.width, self.height),
#         #                     self.game.attack_spritesheet.get_sprite(96, 32, self.width, self.height),
#         #                     self.game.attack_spritesheet.get_sprite(128, 32, self.width, self.height)]

#         left_animations = [self.game.attack_spritesheet.get_sprite(0, 0, self.width, self.height),
#                             self.game.attack_spritesheet.get_sprite(32, 0, self.width, self.height),
#                             self.game.attack_spritesheet.get_sprite(64, 0, self.width, self.height),
#                             self.game.attack_spritesheet.get_sprite(96, 0, self.width, self.height),
#                             self.game.attack_spritesheet.get_sprite(128, 0, self.width, self.height),
#                             self.game.attack_spritesheet.get_sprite(160, 0, self.width, self.height),
#                             self.game.attack_spritesheet.get_sprite(192, 0, self.width, self.height),
#                             self.game.attack_spritesheet.get_sprite(224, 0, self.width, self.height)]

#         # up_animations = [self.game.attack_spritesheet.get_sprite(0, 0, self.width, self.height),
#         #                     self.game.attack_spritesheet.get_sprite(32, 0, self.width, self.height),
#         #                     self.game.attack_spritesheet.get_sprite(64, 0, self.width, self.height),
#         #                     self.game.attack_spritesheet.get_sprite(96, 0, self.width, self.height),
#         #                     self.game.attack_spritesheet.get_sprite(128, 0, self.width, self.height)]
        
#         # if direction == 'up':
#         #     self.image = up_animations[math.floor(self.animation_loop)]
#         #     self.animation_loop += 0.5
#         #     if self.animation_loop >= 5:
#         #         self.kill()
#         # if direction == 'down':
#         #     self.image = down_animations[math.floor(self.animation_loop)]
#         #     self.animation_loop += 0.5
#         #     if self.animation_loop >= 5:
#         #         self.kill()        
#         if direction == 'right':
#             self.image = right_animations[math.floor(self.animation_loop)]
#             self.animation_loop += 0.5
#             if self.animation_loop >= 8:
#                 self.kill()
#         if direction == 'left':
#             self.image = left_animations[math.floor(self.animation_loop)]
#             self.animation_loop += 0.5
#             if self.animation_loop >= 8:
#                 self.kill()