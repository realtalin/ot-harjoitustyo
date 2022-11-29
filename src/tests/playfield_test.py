import unittest
from playfield import Playfield

DISPLAY_SIZE = 800

class TestPlayfield(unittest.TestCase):
    
    def test_amount_of_cells_created_is_size_times_size(self):
        playfield = Playfield(5, DISPLAY_SIZE)

        self.assertEqual(len(playfield.cells), 25)

    def test_one_background_created_for_every_cell(self):
        playfield = Playfield(5, DISPLAY_SIZE)

        self.assertEqual(len(playfield.cells), len(playfield.cell_backgrounds))

    def test_playfield_array_contains_correct_amount_of_cells(self):
        size = 5
        playfield = Playfield(size, DISPLAY_SIZE)
        array_len = 0

        for row in playfield.playfield_array:
            for cell in row:
                array_len += 1

        self.assertEqual(len(playfield.cells), array_len)
