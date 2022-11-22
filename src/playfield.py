import pygame
from sprites.cell import Cell


class Playfield():
    def __init__(self, size, cell_size):
        self.cell_size = cell_size
        self.cells = pygame.sprite.Group()
        self._init_playfield(size)
    
        
    def _init_playfield(self, size):
        for x in range(size):
            for y in range(size):
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                self.cells.add(Cell(normalized_x, normalized_y))

   


    


        

            





    

