import random

import pygame

from sprites.cell import Cell, CellBackground


class Level:
    """Class for representing the level, contains all of the cells.

    Attributes:
        init_time (int): Time that the level was initialized at
        size (int): Width/height of the level
        cells: Pygame sprite group that contains all cells
        correct_cells: Pygame sprite group that contains all correct cells
        cell_backgrounds: Pygame sprite group that contains all cell backgrounds
        all_sprites: Pygame sprite group that contains all cells and all cell backgrounds
    """

    def __init__(self, size, display_size, init_time=0):
        """The constructor. Calls init_cells and generate_correct_cells.

        Args:
            size (int): Width/height of the level
            display_size (int): Width/height of the window
            init_time (int, optional): Time that the level was initialized at.
                Defaults to 0.
        """
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
        """Static method for creating a new level.

        Args:
            size (int): Width/height of the level
            display_size (int): Width/height of the window
            init_time (int): Time that the level was initialized and shown to the player at.

        Returns:
            A new level object
        """
        return Level(size, display_size, init_time)

    def _calculate_cell_size(self, display_size):
        """Calculates the cell size based on window size and level size (=amount of cells)

        Args:
            display_size (int): Width/height of the window

        Returns:
            Integer for cell size
        """
        return display_size / self.size * 0.9

    def _calculate_cell_coordinates(self, display_size, cell_size, row, column):
        """Calculates the actual cell coordinates, scaling to leave a gap inbetween the cells
        and adding a constant to move the cells away from the edge of the window.

        Args:
            display_size (int): Widht/height of the window
            cell_size (int): Width/height of the cells
            row (int): Row of the cell
            column (int): Column of the cell

        Returns:
            A tuple of the coordinates of the cell, x first, y second
        """
        cell_gap = 1/0.9
        level_edge = (display_size / self.size) * 0.05

        x_coordinate = row * cell_size * cell_gap + level_edge
        y_coordinate = column * cell_size * cell_gap + level_edge

        return (x_coordinate, y_coordinate)

    def _init_cells(self, display_size):
        """Creates cells based on size and coordinates,  and creates backgrounds for all of them.

        Args:
            display_size (int): Widht/height of the window
        """
        for row in range(self.size):

            for column in range(self.size):

                cell_size = self._calculate_cell_size(display_size)
                cell_coordinates = self._calculate_cell_coordinates(
                    display_size, cell_size, row, column)

                cell = Cell(cell_size, cell_coordinates)
                self.cells.add(cell)

                cell_background = CellBackground(cell_size, cell_coordinates)
                self.cell_backgrounds.add(cell_background)

        self.all_sprites.add(self.cells, self.cell_backgrounds)

    def _generate_correct_cells(self, correct_amount):
        """Chooses a specified amount of random cells to be correct cells

        Args:
            correct_amount (int): The amount of correct cells to choose
        """
        cell_list = []
        for cell in self.cells:
            cell_list.append(cell)

        correct = random.choices(cell_list, k=correct_amount)

        for cell in correct:
            self.correct_cells.add(cell)

    def _correct_showing_time_left(self, time):
        """Returns whether theres still time left for the correct cells
        to be shown at the start of the level.

        Args:
            time (int): The current time

        Returns:
            True, if the cells should still be shown, false if they should be hidden
        """
        if 2200 - (time - self.init_time) > 0:
            return True
        return False

    def click_on_incorrect_cell(self, mouse_position, time):
        """Handles clicks on cells, checks if an incorrect cell was clicked.
        Cells cannot be clicked while the correct cells are still being shown.

        Args:
            mouse_position (tuple): Tuple of x and y coordinate of the click
            time (int): The time of the click

        Returns:
            True, if an incorrect cell was clicked after the showing time is over, False otherwise
        """
        if self._correct_showing_time_left(time):
            return False
        for cell in self.cells:
            if cell.rect.collidepoint(mouse_position):
                cell.click()
                if cell not in self.correct_cells:
                    return True
        return False

    def all_correct_clicked(self):
        """Checks whether all correct cells have been clicked

        Returns:
            True, if all correct cells have been clicked, False otherwise
        """
        all_correct = True
        for cell in self.correct_cells:
            if cell.clicked is False:
                all_correct = False
        return all_correct

    def update_cell_visibility(self, time):
        """Shows cells during correct showing time.
        Shows correct clicked cells after showing time. Hides other cells.

        Args:
            time (int): The current time
        """
        for cell in self.correct_cells:
            if self._correct_showing_time_left(time) or cell.clicked:
                cell.set_visible()

            else:
                cell.set_hidden()

    def update_state(self, time):
        """Updates cell visibility

        Args:
            time (int): The current time
        """
        self.update_cell_visibility(time)
        self.cells.update()
