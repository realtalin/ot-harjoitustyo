import pygame
import random
import itertools
from sprites.cell import Cell, CellBackground


class Playfield():
    def __init__(self, size, display_size):
        self.size = size
        self.cells = pygame.sprite.Group()
        self.cell_backgrounds = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.playfield_array = []

        self._init_cells(display_size)
        self.generate_correct(5)
        
    def _init_cells(self, display_size):
        # 0.9 scale, so cells have space in between
        cell_size = (display_size / self.size) * 0.9
    
        for x in range(self.size):

            self.playfield_array.append([])

            for y in range(self.size):
                # scale x and y to create gap inbetween cells and 
                # add constant to move cells from edges of display
                x_normalized = x * cell_size * (1/0.9) + ((display_size / self.size) * 0.1 / 2)
                y_normalized = y * cell_size * (1/0.9) + ((display_size / self.size) * 0.1 / 2)

                cell = Cell(cell_size, x_normalized, y_normalized)
                self.playfield_array[x].append(cell)
                self.cells.add(cell)

                cell_background = CellBackground(cell_size, x_normalized, y_normalized)
                self.cell_backgrounds.add(cell_background)

        self.all_sprites.add(self.cells, self.cell_backgrounds)

    def generate_correct(self, correct_amount):
        correct = random.choices(list(itertools.chain(*self.playfield_array)), k=correct_amount)
        for cell in correct:
            cell.correct = True


        

