import pygame
import os


asset_dir = os.path.dirname(__file__)

class Cell(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        self.size = size
        super().__init__()

        image_file = pygame.image.load(os.path.join(asset_dir, "..", "assets", "white_square.png"))
        self.image = pygame.transform.scale(image_file, (self.size, self.size))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.clicked = False
        self.correct = False

    def _hide(self):
        image_file = pygame.image.load(os.path.join(asset_dir, "..", "assets", "invisible_square.png"))
        self.image = pygame.transform.scale(image_file, (self.size, self.size))

    def _show(self):
        image_file = pygame.image.load(os.path.join(asset_dir, "..", "assets", "white_square.png"))
        self.image = pygame.transform.scale(image_file, (self.size, self.size))

    def click(self):
        self._hide()
        self.clicked = True

class CellBackground(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()

        image_file = pygame.image.load(os.path.join(asset_dir, "..", "assets", "grid_tile.png"))
        self.image = pygame.transform.scale(image_file, (size, size))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
