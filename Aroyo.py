import pygame
class importall():
    def __init__(self, None_Collision_Tile, Collision_Tile, all_sprites, none_collision_sprites,collision_sprites):
        
        self.wall_0 = None_Collision_Tile((all_sprites, none_collision_sprites), (388, 457), "objects/tiles/Floors/Main/Floor1.png")
                
        self.wall_1 = None_Collision_Tile((all_sprites, none_collision_sprites), (467, 474), "objects/tiles/Floors/Main/Floor1.png")
                
        self.wall_2 = None_Collision_Tile((all_sprites, none_collision_sprites), (545, 492), "objects/tiles/Floors/Main/Floor1.png")
                
        self.wall_3 = None_Collision_Tile((all_sprites, none_collision_sprites), (622, 510), "objects/tiles/Floors/Main/Floor1.png")

        #self.wall_4 = Collision_Tile((all_sprites, collision_sprites), (482, 446), "objects/tiles/walls/junk_walls/junk_wall1.png","objects/tiles/walls/junk_walls/junk_wall_mask.png","objects/tiles/walls/junk_walls/junk_wall_collision_rect.png")
                
        self.wall_5 = None_Collision_Tile((all_sprites, none_collision_sprites), (576, 469), "objects/tiles/walls/junk_walls/metal_door_frame.png")
                
        #self.wall_6 = Collision_Tile((all_sprites, collision_sprites), (653, 489), "objects/tiles/walls/junk_walls/junk_wall1.png","objects/tiles/walls/junk_walls/junk_wall_mask.png","objects/tiles/walls/junk_walls/junk_wall_collision_rect.png")
                
        self.wall_7 = None_Collision_Tile((all_sprites, none_collision_sprites), (697, 527), "objects/tiles/Floors/Main/Floor1.png")
                
        self.wall_8 = Collision_Tile((all_sprites, collision_sprites), (741, 512), "objects/tiles/walls/junk_walls/metal_wall.png","objects/tiles/walls/junk_walls/metal_wall_mask.png","objects/tiles/walls/junk_walls/junk_wall_collision_rect.png")
                
        self.wall_9 = Collision_Tile((all_sprites, collision_sprites), (788, 449), "objects/tiles/walls/junk_walls/junk_wall1b.png","objects/tiles/walls/junk_walls/junk_wall_mask_b.png","objects/tiles/walls/junk_walls/junk_wall_collision_rect.png")
                
        self.wall_10 = None_Collision_Tile((all_sprites, none_collision_sprites), (772, 468), "objects/tiles/Floors/Main/Floor1.png")
                
        self.wall_11 = None_Collision_Tile((all_sprites, none_collision_sprites), (698, 451), "objects/tiles/Floors/Main/Floor1.png")
                
        self.wall_12 = None_Collision_Tile((all_sprites, none_collision_sprites), (623, 434), "objects/tiles/Floors/Main/Floor1.png")
                
        self.wall_13 = None_Collision_Tile((all_sprites, none_collision_sprites), (549, 417), "objects/tiles/Floors/Main/Floor1.png")
                
        self.wall_14 = None_Collision_Tile((all_sprites, none_collision_sprites), (471, 399), "objects/tiles/Floors/Main/Floor1.png")
                
        self.wall_15 = Collision_Tile((all_sprites, collision_sprites), (882, 373), "objects/tiles/walls/junk_walls/junk_wall1b.png","objects/tiles/walls/junk_walls/junk_wall_mask_b.png","objects/tiles/walls/junk_walls/junk_wall_collision_rect.png")
                
        self.wall_16 = None_Collision_Tile((all_sprites, none_collision_sprites), (809, 439), "objects/tiles/Floors/Main/Floor1.png")
                
        self.wall_17 = None_Collision_Tile((all_sprites, none_collision_sprites), (735, 424), "objects/tiles/Floors/Main/Floor1.png")
                
        self.wall_18 = None_Collision_Tile((all_sprites, none_collision_sprites), (656, 408), "objects/tiles/Floors/Main/Floor1.png")
                
        self.wall_19 = None_Collision_Tile((all_sprites, none_collision_sprites), (577, 390), "objects/tiles/Floors/Main/Floor1.png")
                
        self.wall_20 = None_Collision_Tile((all_sprites, none_collision_sprites), (503, 374), "objects/tiles/Floors/Main/Floor1.png")
                
        self.wall_21 = Collision_Tile((all_sprites, collision_sprites), (389, 346), "objects/tiles/walls/junk_walls/junk_wall1b.png","objects/tiles/walls/junk_walls/junk_wall_mask_b.png","objects/tiles/walls/junk_walls/junk_wall_collision_rect.png")
                
        self.wall_22 = Collision_Tile((all_sprites, collision_sprites), (481, 281), "objects/tiles/walls/junk_walls/junk_wall1b.png","objects/tiles/walls/junk_walls/junk_wall_mask_b.png","objects/tiles/walls/junk_walls/junk_wall_collision_rect.png")
                
        self.wall_23 = Collision_Tile((all_sprites, collision_sprites), (567, 278), "objects/tiles/walls/junk_walls/metal_wall.png","objects/tiles/walls/junk_walls/metal_wall_mask.png","objects/tiles/walls/junk_walls/junk_wall_collision_rect.png")
                
        self.wall_24 = Collision_Tile((all_sprites, collision_sprites), (612, 288), "objects/tiles/walls/junk_walls/metal_wall.png","objects/tiles/walls/junk_walls/metal_wall_mask.png","objects/tiles/walls/junk_walls/junk_wall_collision_rect.png")

        self.wall_25 = Collision_Tile((all_sprites, collision_sprites), (660, 298), "objects/tiles/walls/junk_walls/junk_wall1.png","objects/tiles/walls/junk_walls/junk_wall_mask.png","objects/tiles/walls/junk_walls/junk_wall_collision_rect.png")
                
        self.wall_26 = Collision_Tile((all_sprites, collision_sprites), (751, 321), "objects/tiles/walls/junk_walls/junk_wall1.png","objects/tiles/walls/junk_walls/junk_wall_mask.png","objects/tiles/walls/junk_walls/junk_wall_collision_rect.png")
                
        self.wall_27 = Collision_Tile((all_sprites, collision_sprites), (844, 346), "objects/tiles/walls/junk_walls/junk_wall1.png","objects/tiles/walls/junk_walls/junk_wall_mask.png","objects/tiles/walls/junk_walls/junk_wall_collision_rect.png")
                
        self.wall_28 = Collision_Tile((all_sprites, collision_sprites), (927, 365), "objects/tiles/walls/junk_walls/metal_wall.png","objects/tiles/walls/junk_walls/metal_wall_mask.png","objects/tiles/walls/junk_walls/junk_wall_collision_rect.png")
                
