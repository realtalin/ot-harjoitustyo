import unittest
from unittest.mock import Mock
from components.level import Level

DISPLAY_SIZE = 800


class TestLevel(unittest.TestCase):

    def test_amount_of_cells_created_is_size_times_size(self):
        level = Level(5, DISPLAY_SIZE)

        self.assertEqual(len(level.cells), 25)

    def test_one_background_created_for_every_cell(self):
        level = Level(5, DISPLAY_SIZE)

        self.assertEqual(len(level.cells), len(level.cell_backgrounds))

    def test_correct_cells_not_clicked_if_shown(self):

        level = Level(5, DISPLAY_SIZE)
        for cell in level.cells:
            cell.click = Mock()

        for cell in level.correct_cells:
            level.click_on_incorrect_cell((cell.rect.x, cell.rect.y), 1000)

        for cell in level.correct_cells:
            cell.click.assert_not_called()

    def test_correct_cells_clicked_if_not_shown(self):

        level = Level(5, DISPLAY_SIZE)
        for cell in level.cells:
            level.correct_cells.add(cell)
            cell.click = Mock()

        for cell in level.correct_cells:
            level.click_on_incorrect_cell((cell.rect.x, cell.rect.y), 3000)

        for cell in level.correct_cells:
            cell.click.assert_called()
