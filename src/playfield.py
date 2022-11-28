import pygame
from sprites.cell import Cell



class Playfield():
    def __init__(self, size, display_size):
        self.cells = pygame.sprite.Group()
        self.playfield = []
        cell_size = (display_size / size) * 0.9
        for x in range(size):
            self.playfield.append([])
            for y in range(size):
                x_normalized = x * cell_size * 1.111 + ((display_size / size) * 0.1 / 2)
                y_normalized = y * cell_size * 1.111 + ((display_size / size) * 0.1 / 2)
                cell = Cell(cell_size, x_normalized, y_normalized)
                self.playfield[x].append(cell)
                self.cells.add(cell)

