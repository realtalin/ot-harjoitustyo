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


    def _calculate_cell_size(self, display_size):
        return display_size / self.size * 0.9


    def _calculate_cell_coordinates(self, display_size, cell_size, row, column):
        cell_gap = 1/0.9
        level_edge = (display_size / self.size) * 0.05

        x_coordinate = row * cell_size * cell_gap + level_edge
        y_coordinate = column * cell_size * cell_gap + level_edge

        return (x_coordinate, y_coordinate)


    def _init_cells(self, display_size):
        for row in range(self.size):

            for column in range(self.size):

                cell_size = self._calculate_cell_size(display_size)
                cell_coordinates = self._calculate_cell_coordinates(display_size, cell_size, row, column)

                cell = Cell(cell_size, cell_coordinates)
                self.cells.add(cell)

                cell_background = CellBackground(cell_size, cell_coordinates)
                self.cell_backgrounds.add(cell_background)

        self.all_sprites.add(self.cells, self.cell_backgrounds)

    def _generate_correct_cells(self, correct_amount):
        cell_list = []
        for cell in self.cells:
            cell_list.append(cell)

        correct = random.choices(cell_list, k=correct_amount)

        for cell in correct:
            self.correct_cells.add(cell)

    def _correct_showing_time_left(self, time):
        if 2200 - (time - self.init_time) > 0:
            return True
        return False

    def click(self, mouse_position, time):
        if self._correct_showing_time_left(time):
            return True
        for cell in self.cells:
            if cell.rect.collidepoint(mouse_position):
                cell.click()
                if cell not in self.correct_cells:
                    return False

                return True

    def all_correct_clicked(self):
        all_correct = True
        for cell in self.correct_cells:
            if cell.clicked is False:
                all_correct = False
        return all_correct

    def update_cell_visibility(self, time):
        for cell in self.correct_cells:
            if self._correct_showing_time_left(time) or cell.clicked:
                cell.set_visible()

            else:
                cell.set_hidden()

    def update_state(self, time):
        self.update_cell_visibility(time)
        self.cells.update()
