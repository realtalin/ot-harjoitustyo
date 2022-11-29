import os
import pygame


asset_dir = os.path.dirname(__file__)


class Cell(pygame.sprite.Sprite):
    def __init__(self, size, row, column):
        self.size = size
        super().__init__()

        image_file = pygame.image.load(os.path.join(
            asset_dir, "..", "assets", "invisible_square.png"))
        self.image = pygame.transform.scale(image_file, (self.size, self.size))
        self.rect = self.image.get_rect()

        self.rect.x = row
        self.rect.y = column

        self.hidden = True
        self.clicked = False
        self.correct = False

    def hide(self):
        image_file = pygame.image.load(os.path.join(
            asset_dir, "..", "assets", "invisible_square.png"))
        self.image = pygame.transform.scale(image_file, (self.size, self.size))

    def show(self):
        image_file = pygame.image.load(os.path.join(
            asset_dir, "..", "assets", "white_square.png"))
        self.image = pygame.transform.scale(image_file, (self.size, self.size))

    def click(self):
        self.clicked = True

    def update(self):
        if self.hidden:
            self.hide()
        else:
            self.show()

    def set_hidden(self):
        self.hidden = True

    def set_visible(self):
        self.hidden = False


class CellBackground(pygame.sprite.Sprite):
    def __init__(self, size, row, column):
        super().__init__()

        image_file = pygame.image.load(os.path.join(
            asset_dir, "..", "assets", "grid_tile.png"))
        self.image = pygame.transform.scale(image_file, (size, size))
        self.rect = self.image.get_rect()

        self.rect.x = row
        self.rect.y = column
