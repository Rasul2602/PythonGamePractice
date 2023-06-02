import pygame
from sprites import *
from config import *
import sys

import pygame.mixer

pygame.mixer.init()


sound = pygame.mixer.Sound('music/xDeviruchi - Title Theme .wav')
deathMelody = pygame.mixer.Sound('music/IT FOLLOWS THEME - Disasterpeace (online-audio-converter.com).wav')
melody = pygame.mixer.Sound('music/Skyrim.wav')

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font('arial.ttf')
        
        self.grass = Spritesheet('img/tileset_grass.png')
        self.wall = Spritesheet('img/wall.png')
        self.pumpkin = Spritesheet('img/global_tileset.png')
        self.character_spritesheet = Spritesheet('img/AnimationSheet_Character2.png')
        self.go_background = pygame.image.load('img/1511867575144063811.png')
        self.go_background = pygame.transform.scale(self.go_background, (self.go_background.get_width() * 1, self.go_background.get_height() * 0.6))  # Увеличение размера фонового изображения
        self.intro_background = pygame.image.load('img/bg.png')
        
        self.wall_2 = Spritesheet('img/global_tileset.png')
        
        
    def createTilemap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self,j,i)
                if column == "|":
                    Wall_left(self, j,i) 
                if column == "B":
                    Block(self, j,i) 
                if column == "S":
                    Ground2(self, j,i)    
                if column == "L":
                    Priest(self, j,i)     
                if column == "E":
                    Enemy(self,j,i)
                if column == "P":
                    self.player= Player(self,j,i)

        
    def new(self):
        
        self.playing = True
        
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.exit = pygame.sprite.LayeredUpdates()
        
        self.createTilemap()
        
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
        
    def update(self):
        self.all_sprites.update()
        
        
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        #game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
            sound.stop()
            deathMelody.stop()
            melody.play(-1)
            
        
        
    def game_over(self):
        text = self.font.render('YOU DIED', True, RED)
        text_rect = text.get_rect(center=(400, 150))
        melody.stop()
        sound.stop()
        deathMelody.play(-1)
        restart_button = Button(10,WIN_HEIGHT - 60, 120,50,RED, BLACK, 'Restart', 32)
        
        for sprite in self.all_sprites:
            sprite.kill()
            
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            
            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                self.new()
                self.main()
                
            self.screen.blit(self.go_background,(0,0))
            self.screen.blit(text, text_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            pygame.display.update()        
            
    def intro_screen(self):
        intro = True
        sound.play(-1)
        title = self.font.render('Awesome Game', True, BLACK)
        
        title_rect = title.get_rect(x=10, y=10)
        
        play_button = ImageButton(340, WIN_HEIGHT/2, 100, 50, './img/play.png')
        
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            
            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
            self.screen.blit(self.intro_background, (0, 0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()    
    def intro_screen(self):
        intro = True
        
        title = self.font.render('Awesome Game', True, BLACK)
        
        title_rect = title.get_rect(x=10,y=10)
        
        play_button = ImageButton(340, WIN_HEIGHT/2, 100, 50, './img/play.png')
        
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            
            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro=False
            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()
            

g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()
    
pygame.quit()
sys.exit()

