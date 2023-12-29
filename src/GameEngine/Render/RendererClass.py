from src.GameEngine.Render.SpriteManager import AnimationManager
from src.GameEngine.Render.BackGroundClass import Background
import pygame as pg


class Renderer:
    """
    Renderer class. Used to render list of game objects
    """
    def __init__(self, screen):
        self.screen = screen
        self.screen.fill([255, 255, 255])
        self.background = Background(r'src/GameEngine/Render/sprites/forest_background', (0, 0), self.screen.get_size())
        self.object_to_render = []
        self.animation_manager = None

    def render(self, objects_to_render):
        """
        Main method
        :param objects_to_render:
        :return:
        """
        self.screen.fill([255, 255, 255])
        self.screen.blit(self.background.surface, (0,0))
        self.create_animation_manager(objects_to_render)
        for obj in self.object_to_render:
            self.animation_manager.update_self(obj.x, obj.y, flip_x=obj.flip_x, flip_y=obj.flip_y, angle=obj.angle, scale=obj.scale)
        pg.display.flip()

    def create_animation_manager(self, objects_to_render):
        self.object_to_render = objects_to_render
        animations = [obj.animated_sprite for obj in self.object_to_render]
        if self.animation_manager is None:
            self.animation_manager = AnimationManager(animations, self.screen)
