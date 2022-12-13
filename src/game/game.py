from components.level import Level


class Game:
    def __init__(self, display_size):
        self.display_size = display_size
        self.time = None
        self.level = None
        self.score = 0
        self.lives = 3

    def click(self, mouse_position, time):
        if self.level.click_on_incorrect_cell(mouse_position, time):
            self.level_failure()

    def update_state(self, time):
        self.update_time(time)
        self.level.update_state(time)

        if self.level.all_correct_clicked():
            self.level_success()

    def update_time(self, time):
        self.time = time

    def new_level(self, size):
        self.level = Level.create_level(
            size, self.display_size, self.time)

    def draw_level(self, display):
        self.level.all_sprites.draw(display)

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
        self.time = time
        self.score = 0
        self.lives = 3
        self.new_level(4)
