import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):
        #display surface
        self.display_surface = pygame.display.get_surface()
        # sprites
        self.visible_spites = YSortCameraGroup()
        self.obstacles_spites = pygame.sprite.Group()

        self.create_map()



    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_spites,self.obstacles_spites])
                if col =='p':
                    self.player = Player((x,y), [self.visible_spites],self.obstacles_spites)




    def run(self):
        #pass
        # start and draw game
        self.visible_spites.custom_draw(self.player)
        self.visible_spites.update()



class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        
        #general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self,player):


        #offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height


        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)

