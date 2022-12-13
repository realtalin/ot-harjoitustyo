import random
import pygame
from sprites.cell import Cell, CellBackground


class Level:
    def __init__(self, size, display_size, init_time=0):
        self.init_time = init_time
        self.size = max(2, size)
        self.cells = pygame.sprite.Group()
        self.correct_cells = pygame.sprite.Group()
        self.cell_backgrounds = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._init_cells(display_size)
        self._generate_correct_cells(size*2)

    @staticmethod
    def create_level(size, display_size, init_time):
        return Level(size, display_size, init_time)

    def _init_cells(self, display_size):
        # 0.9 scale, so cells have space in between
        cell_size = (display_size / self.size) * 0.9

        for row in range(self.size):

            for column in range(self.size):
                # scale x and y to create gap inbetween cells and
                # add constant to move cells from edges of display
                x_normalized = row * cell_size * \
                    (1/0.9) + ((display_size / self.size) * 0.1 / 2)
                y_normalized = column * cell_size * \
                    (1/0.9) + ((display_size / self.size) * 0.1 / 2)

                cell = Cell(cell_size, x_normalized, y_normalized)
                self.cells.add(cell)

                cell_background = CellBackground(
                    cell_size, x_normalized, y_normalized)
                self.cell_backgrounds.add(cell_background)

        self.all_sprites.add(self.cells, self.cell_backgrounds)

    def _generate_correct_cells(self, correct_amount):
        cell_list = []
        for cell in self.cells:
            cell_list.append(cell)

        correct = random.choices(cell_list, k=correct_amount)

        for cell in correct:
            self.correct_cells.add(cell)

    def _correct_showing_time_left(self, current_time):
        if 1500 - (current_time - self.init_time) > 0:
            return True
        return False

    def click_cell(self, mouse_position, current_time):
        if self._correct_showing_time_left(current_time):
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
            if self._correct_showing_time_left(current_time) or cell.clicked:
                cell.set_visible()

            else:
                cell.set_hidden()

    def update_state(self, current_time):
        self.update_cell_visibility(current_time)
        self.cells.update()
