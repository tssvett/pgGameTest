class BaseGameObject:
    """
    Parent object to all game objects
    """
    def __init__(self, x, y, width, height, sprite=None, flip_x=False, flip_y=False, angle=0, scale=1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.center_x = self.x + (self.width / 2)
        self.center_y = self.y + (self.height / 2)
        self.animated_sprite = sprite
        self.flip_x = flip_x
        self.flip_y = flip_y
        self.angle = angle
        self.scale = scale

    def update(self, new_x=None, new_y=None, new_width=None, new_height=None, flip_x=False, flip_y=False, angle=None, scale=None):
        """
        Update the game object
        :param angle: angle to rotate sprite
        :param flip_y: flip by y or not
        :param flip_x: flip by x or not
        :param new_x: changed x
        :param new_y: changed y
        :param new_width: changed width
        :param new_height: changed height
        :return:
        """
        if new_x is not None:
            self.x = new_x
        if new_y is not None:
            self.y = new_y
        if new_width is not None:
            self.width = new_width
        if new_height is not None:
            self.height = new_height
        if angle is not None:
            self.angle = angle
        if scale is not None:
            self.scale = scale
        self.center_x = self.x + (self.width / 2)
        self.center_y = self.y + (self.height / 2)
        self.flip_x = flip_x
        self.flip_y = flip_y

    def output(self):
        print(f'Координаты: ({self.x}, {self.y}, Размеры: ({self.width}, {self.height}), Координаты центра: ({self.center_x}, {self.center_y})')
