import pygame
from pygame import *
from pygame.locals import *
import pygame_gui

class inventoryGui():
    def __init__(self, inv_list, screen, scroll_offset):
        self.toggled = False
        
        self.inv_list = inv_list
        self.screen = screen
        self.list_position = (50, 50)
        self.list_size = (200, 400)
        self.list_font = pygame.font.SysFont(None, 24)
        self.list_item_height = 30
        self.box_position = (40, 40)
        self.box_size = (120, 420)
        self.box_color = (255, 255, 255)
        self.box_thickness = 2
        self.scroll_offset = scroll_offset
        self.clickable_rects = []
        self.list_font = pygame.font.SysFont('fallouty', 24)
    def toggle_on(self):
        self.invbox = pygame.image.load('objects/ui/inv/inv.png')
        self.rect = self.invbox.get_rect()
        self.rect.x = 1320/2 - 499
        self.rect.y = 920/2 - 377
        
        x = 1320
        y = 920
        manager = pygame_gui.UIManager((x,y))
        cont = manager.get_root_container() 
        self.button_3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x/2-199, y/2-163), (100, 50)),
                                        text='exit', manager=manager,
                                        container=cont,
                                        anchors={'bottom': 'bottom',
                                                 'top': 'top'})
        pygame.draw.rect(self.screen, self.box_color, (*self.box_position, *self.box_size), self.box_thickness)

        # Calculate the visible items within the box
              # New list to store clickable regions

        start_index = max(0, self.scroll_offset // self.list_item_height)
        end_index = min(len(self.inv_list), (self.scroll_offset + self.box_size[1]) // self.list_item_height + 1)

        for i, item in enumerate(self.inv_list):
            item_y = self.list_position[1] + i * self.list_item_height - self.scroll_offset
            if self.box_position[1] <= item_y < self.box_position[1] + self.box_size[1]:
                item_position = (self.list_position[0], item_y)

                # Create a rectangle surface for each item
                item_rect = pygame.Surface((self.list_size[0], self.list_item_height))
                item_rect.fill((0, 0, 0))  # Set the background color of the item rectangle
                item_text = self.list_font.render(self.inv_list[i], True, (255, 255, 255))
                item_rect.blit(item_text, (0, 0))  # Blit the item text onto the rectangle

                # Draw the rectangle on the screen
                self.screen.blit(item_rect, item_position)

                # Store the clickable region (rectangle and item) in clickable_rects
                self.clickable_rects.append((item_rect.get_rect().move(item_position), self.inv_list[i]))

        return self.clickable_rects
    
    def update(self):
        if self.toggled == True:
            self.toggle_on()

