import unittest
from unittest.mock import Mock
from components.playfield import Playfield

DISPLAY_SIZE = 800


class TestPlayfield(unittest.TestCase):

    def test_amount_of_cells_created_is_size_times_size(self):
        playfield = Playfield(5, DISPLAY_SIZE)

        self.assertEqual(len(playfield.cells), 25)

    def test_one_background_created_for_every_cell(self):
        playfield = Playfield(5, DISPLAY_SIZE)

        self.assertEqual(len(playfield.cells), len(playfield.cell_backgrounds))

    def test_correct_cells_not_clicked_if_shown(self):

        playfield = Playfield(5, DISPLAY_SIZE)
        for cell in playfield.cells:
            cell.click = Mock()

        for cell in playfield.correct_cells:
            playfield.click_cell((cell.rect.x, cell.rect.y), 1000)

        for cell in playfield.correct_cells:
            cell.click.assert_not_called()

    def test_correct_cells_clicked_if_not_shown(self):

        playfield = Playfield(5, DISPLAY_SIZE)
        for cell in playfield.cells:
            playfield.correct_cells.add(cell)
            cell.click = Mock()

        for cell in playfield.correct_cells:
            playfield.click_cell((cell.rect.x, cell.rect.y), 2000)

        for cell in playfield.correct_cells:
            cell.click.assert_called()
