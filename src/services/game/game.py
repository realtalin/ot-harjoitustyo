from services.game.level import Level


class Game:
    """Class that represents the current ongoing game.

    Attributes:
        display_size (int): The width/height of the window
        time (int): The current time
        level: The level being currently attempted
        score: The score of the player
        lives: The amount of failures the player can make before game over
    """

    def __init__(self, visual_grid_size, score_service):
        """The constructor that creates a new game.

        Args:
            visual_grid_size (int): The desired size of the level grid in pixels
        """

        self.visual_grid_size = visual_grid_size
        self.score_service = score_service
        self.username = ""
        self.time = None
        self.level = None
        self.score = 0
        self.lives = 3

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def get_lives(self):
        return self.lives

    def get_score(self):
        return self.score

    def save_score(self):
        self.score_service.save(self.username, self.score)

    def click(self, mouse_position, time):
        """Handles a mouse click. If an incorrect cell is clicked, the level is failed.

        Args:
            mouse_position (tuple): Tuple of x and y coordinate of the click
            time (int): The time of the click
        """
        if self.level.click_on_incorrect_cell(mouse_position, time):
            self.level_failure()

    def update_state(self, time):
        """Updates the game time and the state of the level.
        If all correct cells have been clicked, the level succeeds.

        Args:
            time (int): The time at the moment of the update
        """
        self.update_time(time)
        self.level.update_state(time)

        if self.level.all_correct_clicked():
            self.level_success()

    def update_time(self, time):
        self.time = time

    def new_level(self, size):
        """Creates a new level and sets it as the current level

        Args:
            size (int): Width/height of the level to be created
        """
        self.level = Level.create_level(
            size, self.visual_grid_size, self.time)

    def level_failure(self):
        self.lives -= 1
        self.new_level(self.level.size)

    def level_success(self):
        self.score += 1
        self.new_level(self.level.size + 1)

    def game_over(self):
        if self.lives <= 0:
            return True

        return False

    def reset(self, time):
        """Resets the game's attributes and intializes a new level.

        Args:
            time (int): Time at the moment of the reset
        """
        self.time = time
        self.score = 0
        self.lives = 3
        self.new_level(4)
