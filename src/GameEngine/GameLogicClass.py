import random

import src.config
from src.GameObjects.BaseGameObjectClass import BaseGameObject
from src.GameEngine.Render.SpriteManager import Animation


class GameLogic:
    """
    GameLogic class. Use it to create game objects including game logic
    """
    def __init__(self):
        self.game_objects = []

    def make_step(self):
        """
        Main method
        :return:
        """
        self.create_object()
        return self.game_objects

    def create_object(self):
        animated_sprite = Animation('src/GameEngine/Render/sprites/skeleton_walk.ase')
        obj = BaseGameObject(x=100, y=750, width=100, height=100, sprite=animated_sprite, flip_x=False, flip_y=False, angle=0, scale=1.5)
        self.game_objects.append(obj)

    def generate_random_object(self):
        animated_sprite = Animation('src/GameEngine/Render/sprites/skeleton_walk.ase')
        print(animated_sprite.frame_duration)
        obj = BaseGameObject(x=random.randint(0, src.config.SCREEN_SIZE[0]), y=random.randint(0, src.config.SCREEN_SIZE[1]), width=100, height=100, sprite=animated_sprite)
        self.game_objects.append(obj)



