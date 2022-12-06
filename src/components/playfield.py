import random
import itertools
import pygame
from sprites.cell import Cell, CellBackground


class Playfield():
    def __init__(self, size, display_size, init_time=0):
        self.init_time = init_time
        self.display_size = display_size
        self.size = max(2, size)
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
            self.correct_cells.add(cell)

    def reset(self, step, init_time):
        self.__init__(self.size + step, self.display_size, init_time)

    def correct_showing_time_left(self, current_time):
        return 1500 - (current_time - self.init_time)

    def click_cell(self, mouse_position, current_time):
        if self.correct_showing_time_left(current_time) > 0:
            return
        for cell in self.cells:
            if cell.rect.collidepoint(mouse_position):
                cell.click()

    def all_correct_clicked(self):
        all_correct = True
        for cell in self.correct_cells:
            if cell.clicked is False:
                all_correct = False
        return all_correct

    def one_incorrect_clicked(self):
        one_incorrect = False
        for cell in self.cells:
            if cell.clicked is True and cell not in self.correct_cells:
                one_incorrect = True
        return one_incorrect

    def update_cell_visibility(self, current_time):
        for cell in self.correct_cells:
            if self.correct_showing_time_left(current_time) > 0 or cell.clicked:
                cell.set_visible()

            else:
                cell.set_hidden()

    def update_playfield_state(self, current_time):
        self.update_cell_visibility(current_time)
        
        if self.one_incorrect_clicked():
            self.reset(-1, current_time)

        if self.all_correct_clicked():
            self.reset(1, current_time)

        self.cells.update()

        