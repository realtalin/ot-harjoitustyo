from components.playfield import Playfield

# TODO: fix bug where the first playfield's init_time is set incorrectly

class Game:
    def __init__(self, display_size):
        self.display_size = display_size
        self.current_time = 0
        self.playfield = self.new_playfield(5)
        self.score = 0
        self.mistakes = 0

    def on_click(self, mouse_position, time):
        self.playfield.click_cell(mouse_position, time)

    def update_state(self, current_time):
        self.current_time = current_time
        self.playfield.update_state(current_time)

        if self.playfield.one_incorrect_clicked():
            self.playfield = self.new_playfield(self.playfield.size-1)

        if self.playfield.all_correct_clicked():
            self.playfield = self.new_playfield(self.playfield.size+1)

    def new_playfield(self, size):
        return Playfield.create_playfield(size, self.display_size, self.current_time)

    def draw_playfield(self, display):
        self.playfield.all_sprites.draw(display)
