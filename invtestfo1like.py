import pygame
from pygame.locals import *
inventory_width = 1  # Maximum number of items per row
inventory_height = 10  # Maximum number of rows
current_page = 0  # Current inventory page
image2 = pygame.image.load('objects/Items/Weapons/RIFLE.png')
image3 = pygame.image.load('objects/ui/inv/items/SHOTGUN.png')
inventory = []
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
class InventoryItem:
    def __init__(self, name, image):
        self.name = name
        self.image = image
        self.rect = self.image.get_rect()

    def move(self, x, y):
        self.rect = self.rect.move(x, y)
object1 = InventoryItem('test', image2)
object2 = InventoryItem('LOL', image3)
inventory = [object1,object1,object1,object1,object1,object1,object1,object1,object1,object1,object1,object1,object1,object1,object1,object1,object1,object1,object1,object1,object1,object1,object1,object1,object1,object1,object1,object1,object1,object2]

def handle_item_click(item):
    print("Clicked item:", item.name)

def draw_inventory():
    x, y = 50, 50
    global current_page 
    global inventory
    global inventory_width
    global inventory_height
    item_spacing = 10
    item_count = len(inventory)
    start_index = current_page * inventory_width * inventory_height
    end_index = min(start_index + (inventory_width * inventory_height), item_count)

    for i in range(start_index, end_index):
        item = inventory[i]
        item_rect = item.image.get_rect().move(x, y)
        screen.blit(item.image, (x, y))
        if item_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                handle_item_click(item)
        x += item.image.get_width() + item_spacing
        if (i + 1) % inventory_width == 0:
            x = 50
            y += item.image.get_height() + item_spacing

    # Draw navigation buttons
    next_button_rect = pygame.Rect(700, 500, 80, 40)
    pygame.draw.rect(screen, (255, 0, 0), next_button_rect)
    pygame.draw.rect(screen, (0, 0, 0), next_button_rect, 3)
    pygame.draw.polygon(screen, (0, 0, 0), ((720, 515), (720, 525), (730, 520)))
    prev_button_rect = pygame.Rect(700, 420, 80, 40)
    pygame.draw.rect(screen, (255, 0, 0), prev_button_rect)
    pygame.draw.rect(screen, (0, 0, 0), prev_button_rect, 3)
    pygame.draw.polygon(screen, (0, 0, 0), ((720, 445), (720, 435), (730, 440)))

    # Check for button clicks
    if next_button_rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            current_page = (current_page + 1) % ((item_count - 1) // (inventory_width * inventory_height) + 1)
    elif prev_button_rect.collidepoint(pygame.mouse.get_pos()):
        if pygame.mouse.get_pressed()[0]:
            current_page = (current_page - 1) % ((item_count - 1) // (inventory_width * inventory_height) + 1)
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    screen.blit(pygame.image.load('Background.png'), (0,0))
    draw_inventory()
    #
    
    pygame.display.flip()

            