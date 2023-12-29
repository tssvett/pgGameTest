import pygame
import os

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location, screen_size):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.file_name = image_file
        self.location = location
        self.screen_size = screen_size
        self.images = self.get_images()
        self.surface = self.blit_to_surface()

    def get_images(self):
        """
        Images must be named lake: Layer_1, Layer_2, Layer_3 etc.
        :return:
        """
        directory = os.listdir(self.file_name)
        images = []
        for image in directory:
            image = pygame.image.load(os.path.join(self.file_name, image))
            images.append(image)
        return images

    def blit_to_surface(self):
        surface = pygame.Surface(self.screen_size)
        for image in self.images:
            surface.blit(pygame.transform.scale(image, self.screen_size), self.location)
        return surface