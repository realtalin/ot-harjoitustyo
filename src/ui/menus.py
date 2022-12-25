import pygame_menu

from services.database.score_service import score_service


class MainMenu(pygame_menu.Menu):
    """Class for the main menu
    """

    def __init__(self, display, start_function, name_setter, default_name=""):
        """The consructor, creates main menu by calling pygame_menu.Menu's constructor and adding a start button.

        Args:
            display: The pygame display to draw the menu on
            start_function (func): Function to start the game
            name_setter (func): Game class method for saving the players name
            default_name (str, optional): Default username to show in selection box.
                Defaults to an empty string.
        """
        self._display = display
        self._start_function = start_function
        self._name_setter = name_setter
        self._default_name = default_name

        super().__init__("Visuaalimuisti", self._display.get_width(),
                         self._display.get_height(), theme=pygame_menu.themes.THEME_BLUE)

        self.add_contents()

    def add_contents(self):
        """Adds the start button, name input box and scores menu button to the menu
        """
        self.add.button("Pelaa", self._start_function)
        self.add.text_input("Nimi: ", default=self._default_name,
                            maxchar=20, onchange=self._name_setter)
        scores_menu = ScoresMenu(self._display, self.render_main)
        self.add.button("Tulokset", scores_menu.render_scores)

    def render_main(self):
        """Renders the main menu
        """
        self.mainloop(self._display)


class FailMenu(pygame_menu.Menu):
    """Class for the fail menu
    """

    def __init__(self, display, score, render_main):
        """The consructor, creates fail menu by calling pygame_menu.Menu's constructor and adding score and game over text.

        Args:
            display: The pygame display to draw the menu on
            score (int): The score the player achieved
            render_main (func): The function that renders the main menu
        """
        self._display = display
        self._score = score
        self._render_main = render_main

        super().__init__("Game Over", self._display.get_width(),
                         self._display.get_height(), theme=pygame_menu.themes.THEME_DARK)

        self.add_contents()

    def add_contents(self):
        """Adds game over text, the achieved score and a main menu button to the fail menu
        """
        self.add.label("GAME OVER")
        self.add.label(f"Tulos: {self._score}")
        self.add.button("Takaisin aloitusnäyttöön", self._render_main)

    def render_fail(self):
        """Renders the fail menu
        """
        self.mainloop(self._display)


class ScoresMenu(pygame_menu.Menu):
    """Class for the scores menu
    """

    def __init__(self, display, render_main):
        """The consructor, creates score menu by calling pygame_menu.Menu's constructor and adding sorted scores.

        Args:
            display: The pygame display to draw the menu on
            render_main (func): The function that renders the main menu
        """
        self._display = display
        self._render_main = render_main

        super().__init__("Visuaalimuisti", self._display.get_width(),
                         self._display.get_height(), theme=pygame_menu.themes.THEME_BLUE)

        self.add_contents()

        for score in self._sorted_scores():
            self.add_score(score)

    def _sorted_scores(self):
        """Sorts the list of scores from score_service

        Returns:
            scores: A sorted list of dictionaries representing scores
        """
        return sorted(score_service.fetch_all(), key=lambda score: score["score"], reverse=True)

    def add_contents(self):
        """Adds back button and label to the scores menu
        """
        self.add.button("Takaisin aloitusnäyttöön", self._render_main)
        self.add.label("Tulokset")

    def add_score(self, score):
        """Adds a score to the scores menu, called for every score in the constructor
        """
        self.add.label(f"{score['username']}: {score['score']}")

    def render_scores(self):
        """Renders the scores menu
        """
        self.mainloop(self._display)
