import pygame_menu


class MainMenu(pygame_menu.Menu):
    """Class for the main menu
    """

    def __init__(self, display_size, start_function):
        """The consructor, creates main menu by calling pygame_menu.Menu's constructor and adding a start button.

        Args:
            display_size (int): The width/heigth of the window
            start_function (func): Function to start the game
        """
        self.start_function = start_function
        super().__init__("Visuaalimuisti", display_size,
                         display_size, theme=pygame_menu.themes.THEME_BLUE)

        self.add_buttons()

    def add_buttons(self):
        self.add.button("Pelaa", self.start_function)


class FailMenu(pygame_menu.Menu):
    """Class for the fail menu
    """

    def __init__(self, display_size):
        """The consructor, creates fail menu by calling pygame_menu.Menu's constructor and adding text.

        Args:
            display_size (int): The width/heigth of the window
        """
        super().__init__("Game Over", display_size,
                         display_size, theme=pygame_menu.themes.THEME_DARK)

        self.add_labels()

    def add_labels(self):
        self.add.label("GAME OVER")
