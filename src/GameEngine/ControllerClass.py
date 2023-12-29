import pygame as pg


class Controller:
    """
    Controller class. Used to handle events by the user
    """
    def __init__(self):
        self.event = None

    def set_event(self, event):
        self.event = event

    @staticmethod
    def _is_pressed(key):
        return pg.key.get_pressed()[key]

    def handle_input(self):
        if self.event.type == pg.QUIT:
            pg.quit()
        if self.event.type == pg.KEYDOWN:
            if self.event.key == pg.K_ESCAPE:
                pg.quit()
        if self._is_pressed(pg.K_s):
            print("down")
