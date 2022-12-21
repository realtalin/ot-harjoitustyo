import pygame_menu


class MainMenu(pygame_menu.Menu):
    """Class for the main menu
    """

    def __init__(self, display_width, display_height, start_function, name_setter):
        """The consructor, creates main menu by calling pygame_menu.Menu's constructor and adding a start button.

        Args:
            display_width (int): The width of the window
            display_height (int): The height of the window
            start_function (func): Function to start the game
        """
        self.start_function = start_function
        self.name_setter = name_setter
        super().__init__("Visuaalimuisti", display_width,
                         display_height, theme=pygame_menu.themes.THEME_BLUE)

        self.add_contents()

    def add_contents(self):
        self.add.button("Pelaa", self.start_function)
        self.add.text_input("Nimi: ", maxchar=20, onchange=self.name_setter)


class FailMenu(pygame_menu.Menu):
    """Class for the fail menu
    """

    def __init__(self, display_width, display_height):
        """The consructor, creates fail menu by calling pygame_menu.Menu's constructor and adding text.

        Args:
            display_width (int): The width of the window
            display_height (int): The height of the window
        """
        super().__init__("Game Over", display_width,
                         display_height, theme=pygame_menu.themes.THEME_DARK)

        self.add_contents()

    def add_contents(self):
        self.add.label("GAME OVER")
