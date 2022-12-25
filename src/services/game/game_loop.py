import pygame


class GameLoop:
    """Class for handling the game loop and events.

    Attributes:
        game (Game): Game object that tracks the ongoing game
        clock (Clock): Clock for getting the current time
        event_queue (EventQueue): Event queue for pygame events
        mouse (Mouse): Mouse for mouse clicks and position
        renderer (Renderer): Renderer for rendering the level
    """

    def __init__(self, game, clock, event_queue, mouse, renderer):
        """The constructor for the loop.

        Args:
            game (Game): Game object that tracks the ongoing game
            clock (Clock): Clock for getting the current time
            event_queue (EventQueue): Event queue for pygame events
            mouse (Mouse): Mouse for mouse clicks and position
            renderer (Renderer): Renderer for rendering the level
        """

        self._game = game
        self._clock = clock
        self._event_queue = event_queue
        self._mouse = mouse
        self._renderer = renderer

    def start(self):
        """Starts the game loop, resets game at the start. Called by main menu start button.
        """

        self._game.reset(self._clock.get_time())

        while True:
            if self._game.game_over():
                self._game.save_score()
                self._renderer.render_fail_menu(
                    self.start, self._game.set_username, self._game.username)

            if self._handle_events() is False:
                break

            self._renderer.render()
            self._clock.run()

            self._game.update_state(self._clock.get_time())

    def _handle_events(self):
        """Event handler for pygame events.

        Returns:
            True, if the QUIT event hasn't been triggered, False if it has
        """

        for event in self._event_queue.get():
            time = self._clock.get_time()

            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN and self._mouse.get_pressed()[0]:
                self._game.click(self._mouse.get_pos(), time)

        return True
