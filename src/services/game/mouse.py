import pygame


class Mouse:
    """Class for the mouse and it's functions
    """

    def get_pos(self):
        """Gets the position of the cursor

        Returns:
            Tuple for the x and y coordinate of the mouse cursor in the window
        """
        return pygame.mouse.get_pos()

    def get_pressed(self):
        """Gets the currently pressed mouse buttons

        Returns:
            Tuple of 5 bools, first bool is the left mouse button.
        """
        return pygame.mouse.get_pressed()
