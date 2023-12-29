import pygame as pg

import src.config
from src.config import SCREEN_SIZE, FLAGS
from src.GameEngine.ControllerClass import Controller
from src.GameEngine.Render.RendererClass import Renderer
from src.GameEngine.GameLogicClass import GameLogic


class GameEngine:
    def __init__(self):
        self._setup()
        self.controller = Controller()
        self.screen = pg.display.set_mode(SCREEN_SIZE, FLAGS)
        self.renderer = Renderer(self.screen)
        self.game_logic = GameLogic()

    @staticmethod
    def _setup():
        pg.init()

    def _handle_inputs(self):
        for event in pg.event.get():
            self.controller.set_event(event)
            self.controller.handle_input()

    def run(self):
        """
        The main game loop
        :return:
        """
        test_object = self.game_logic.make_step()
        while True:
            self._handle_inputs()
            #objects = self.game_logic.make_step()
            self.renderer.render(test_object)
