import pygame_menu


class MainMenu(pygame_menu.Menu):
    """Class for the main menu
    """

    def __init__(self, display, start_function, name_setter, default_name=""):
        """The consructor, creates main menu by calling pygame_menu.Menu's constructor and adding a start button.

        Args:
            display_width (int): The width of the window
            display_height (int): The height of the window
            start_function (func): Function to start the game
            name_setter (func): Game class method for saving the players name
        """
        self._display = display
        self.start_function = start_function
        self.name_setter = name_setter
        self.default_name = default_name
        super().__init__("Visuaalimuisti", self._display.get_width(),
                         self._display.get_height(), theme=pygame_menu.themes.THEME_BLUE)

        self.add_contents()

    def add_contents(self):
        self.add.button("Pelaa", self.start_function)
        self.add.text_input("Nimi: ", default=self.default_name, maxchar=20, onchange=self.name_setter)

    def render_main(self):
        self.mainloop(self._display)


class FailMenu(pygame_menu.Menu):
    """Class for the fail menu
    """

    def __init__(self, display_width, display_height, score, render_main):
        """The consructor, creates fail menu by calling pygame_menu.Menu's constructor and adding text.

        Args:
            display_width (int): The width of the window
            display_height (int): The height of the window
            score (int): The score the player achieved
        """
        self.render_main = render_main
        self.score = score
        super().__init__("Game Over", display_width,
                         display_height, theme=pygame_menu.themes.THEME_DARK)

        self.add_contents()

    def add_contents(self):
        self.add.label("GAME OVER")
        self.add.label(f"Tulos: {self.score}")
        self.add.button("Takaisin aloitusnäyttöön", self.render_main)
