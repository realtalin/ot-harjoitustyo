import random
import itertools
import pygame
from sprites.cell import Cell, CellBackground


class Playfield():
    def __init__(self, size, display_size, init_time=0):
        self.init_time = init_time
        self.display_size = display_size
        self.size = size
        self.cells = pygame.sprite.Group()
        self.correct_cells = pygame.sprite.Group()
        self.cell_backgrounds = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.playfield_array = []

        self._init_cells()
        self.generate_correct(size*2)

    def _init_cells(self):
        # 0.9 scale, so cells have space in between
        cell_size = (self.display_size / self.size) * 0.9

        for row in range(self.size):

            self.playfield_array.append([])

            for column in range(self.size):
                # scale x and y to create gap inbetween cells and
                # add constant to move cells from edges of display
                x_normalized = row * cell_size * \
                    (1/0.9) + ((self.display_size / self.size) * 0.1 / 2)
                y_normalized = column * cell_size * \
                    (1/0.9) + ((self.display_size / self.size) * 0.1 / 2)

                cell = Cell(cell_size, x_normalized, y_normalized)
                self.playfield_array[row].append(cell)
                self.cells.add(cell)

                cell_background = CellBackground(
                    cell_size, x_normalized, y_normalized)
                self.cell_backgrounds.add(cell_background)

        self.all_sprites.add(self.cells, self.cell_backgrounds)

    def generate_correct(self, correct_amount):
        correct = random.choices(list(itertools.chain(
            *self.playfield_array)), k=correct_amount)
        for cell in correct:
            cell.correct = True
            self.correct_cells.add(cell)

    def reset(self, step, init_time):
        self.__init__(self.size + step, self.display_size, init_time)

    def correct_showing_time_left(self, current_time):
        return 1500 - (current_time - self.init_time)

    def update(self, current_time):
        for cell in self.correct_cells:
            if self.correct_showing_time_left(current_time) > 0:
                cell.set_visible()

            else:
                cell.set_hidden()

        self.cells.update()
