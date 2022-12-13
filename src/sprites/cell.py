import os
import pygame


asset_dir = os.path.dirname(__file__)


class Cell(pygame.sprite.Sprite):
    """Class that represents a clickable cell in the level grid.

    Attributes:
        size (int): Width/height of the cell in pixels, calculated automatically by Level
        image: Scaled image file representing the cell
        rect: Pygame rect object for storing rectangular coordinates
        rect.x (int): The x coordinate
        rect.y (int): The y coordinate
        visible (bool): Whether the cell should be drawn
        clicked (bool): Whether the cell has been clicked
    """

    def __init__(self, size, coordinates: tuple):
        """The constructor. Calls pygame sprite constructor.

        Args:
            size (int): Size of the cell in pixels, calculated automatically by Level
            coordinates (tuple): Tuple of two integers, first is the x coordinate, second is the y coordinate
        """

        self.size = size
        super().__init__()

        image_file = pygame.image.load(os.path.join(
            asset_dir, "..", "assets", "invisible_square.png"))
        self.image = pygame.transform.scale(image_file, (self.size, self.size))
        self.rect = self.image.get_rect()

        self.rect.x = coordinates[0]
        print(self.rect.x)
        self.rect.y = coordinates[1]

        self._visible = False
        self.clicked = False

    def _hide(self):
        """Hides the cell by making the image transparent.
        """
        image_file = pygame.image.load(os.path.join(
            asset_dir, "..", "assets", "invisible_square.png"))
        self.image = pygame.transform.scale(image_file, (self.size, self.size))

    def _show(self):
        """Shows the cell by making the image a white square.
        """
        image_file = pygame.image.load(os.path.join(
            asset_dir, "..", "assets", "white_square.png"))
        self.image = pygame.transform.scale(image_file, (self.size, self.size))

    def click(self):
        self.clicked = True

    def update(self):
        """Checks cell visibility and hides/shows the cell.
        """
        if self._visible:
            self._show()
        else:
            self._hide()

    def set_hidden(self):
        self._visible = False

    def set_visible(self):
        self._visible = True


class CellBackground(pygame.sprite.Sprite):
    """Class that represents the background of each cell, forming the level 'grid'.

    Atrributes:
        image: Scaled image file representing the background
        rect: Pygame rect object for storing rectangular coordinates
        rect.x (int): The x coordinate
        rect.y (int): The y coordinate
    """

    def __init__(self, size, coordinates):
        """The constructor. Calls pygame sprite constructor.

        Args:
            size (int): Width/height of the background in pixels, calculated automatically by Level
            coordinates (tuple): Tuple of two integers, first is the x coordinate, second is the y coordinate
        """

        super().__init__()

        image_file = pygame.image.load(os.path.join(
            asset_dir, "..", "assets", "grid_tile.png"))
        self.image = pygame.transform.scale(image_file, (size, size))
        self.rect = self.image.get_rect()

        self.rect.x = coordinates[0]
        self.rect.y = coordinates[1]
