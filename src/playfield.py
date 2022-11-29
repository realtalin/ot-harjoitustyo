import pygame
from sprites.cell import Cell, CellBackground


class Playfield():
    def __init__(self, size, display_size):
        self.cells = pygame.sprite.Group()
        self.cell_backgrounds = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.playfield = []

        self._init_cells(size, display_size)
        
    def _init_cells(self, size, display_size):
        # 0.9 scale, so cells have space in between
        cell_size = (display_size / size) * 0.9
    
        for x in range(size):

            self.playfield.append([])

            for y in range(size):
                # scale x and y to create gap inbetween cells and 
                # add constant to move cells from edges of display
                x_normalized = x * cell_size * (1/0.9) + ((display_size / size) * 0.1 / 2)
                y_normalized = y * cell_size * (1/0.9) + ((display_size / size) * 0.1 / 2)

                cell = Cell(cell_size, x_normalized, y_normalized)
                self.playfield[x].append(cell)
                self.cells.add(cell)

                cell_background = CellBackground(cell_size, x_normalized, y_normalized)
                self.cell_backgrounds.add(cell_background)

        self.all_sprites.add(self.cells)
        self.all_sprites.add(self.cell_backgrounds)

    
