from services.game.level import Level


class Game:
    """Class that represents the current ongoing game.

    Attributes:
        visual_grid_size (int): The width/height of the window
        time (int): The current time
        level: The level being currently attempted
        username (str): The name of the player
        score (int): The score of the player
        lives (int): The amount of failures the player can make before game over
    """

    def __init__(self, visual_grid_size, score_service):
        """The constructor that creates a new game.

        Args:
            visual_grid_size (int): Width/height of the level in pixels
            score_service: The service for saving scores to the database
        """

        self._visual_grid_size = visual_grid_size
        self._score_service = score_service
        self._time = None
        self._level = None
        self.username = ""
        self.score = 0
        self.lives = 3

    def set_username(self, username):
        self.username = username

    def save_score(self):
        self._score_service.save(self.username, self.score)

    def click(self, mouse_position, time):
        """Handles a mouse click. If an incorrect cell is clicked, the level is failed.

        Args:
            mouse_position (tuple): Tuple of x and y coordinate of the click
            time (int): The time of the click
        """
        if self.level.click_on_incorrect_cell(mouse_position, time):
            self._level_failure()

    def update_state(self, time):
        """Updates the game time and the state of the level.
        If all correct cells have been clicked, the level succeeds.

        Args:
            time (int): The time at the moment of the update
        """
        self._update_time(time)
        self.level.update_state(time)

        if self.level.all_correct_clicked():
            self._level_success()

    def _update_time(self, time):
        self._time = time

    def _new_level(self, size):
        """Creates a new level and sets it as the current level

        Args:
            size (int): Width/height of the level to be created
        """
        self.level = Level.create_level(
            size, self._visual_grid_size, self._time)

    def _level_failure(self):
        self.lives -= 1
        self._new_level(self.level.size)

    def _level_success(self):
        self.score += 1
        self._new_level(self.level.size + 1)

    def game_over(self):
        if self.lives <= 0:
            return True

        return False

    def reset(self, time):
        """Resets the game's attributes and intializes a new level.

        Args:
            time (int): Time at the moment of the reset
        """
        self._time = time
        self.score = 0
        self.lives = 3
        self._new_level(4)
