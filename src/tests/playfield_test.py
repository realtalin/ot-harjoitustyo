import unittest
from components.playfield import Playfield

DISPLAY_SIZE = 800

class TestPlayfield(unittest.TestCase):
    
    def test_amount_of_cells_created_is_size_times_size(self):
        playfield = Playfield(5, DISPLAY_SIZE)

        self.assertEqual(len(playfield.cells), 25)

    def test_one_background_created_for_every_cell(self):
        playfield = Playfield(5, DISPLAY_SIZE)

        self.assertEqual(len(playfield.cells), len(playfield.cell_backgrounds))
