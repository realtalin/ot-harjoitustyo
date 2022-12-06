import pygame_menu


class MyMenu(pygame_menu.Menu):
    def __init__(self, display_size, start_function):
        self.start_function = start_function
        super().__init__("Visuaalimuisti", display_size,
                         display_size, theme=pygame_menu.themes.THEME_BLUE)

        self.add_buttons()

    def add_buttons(self):
        self.add.button("Pelaa", self.start_function)
