class Command:
    def execute(self):
        pass


class ClearDisplay(Command):
    def __init__(self, color):
        self.__color = color

    def execute(self):
        print(f'Display is cleared with color {self.__color}')


class DrawPixel(Command):
    def __init__(self, x, y, color):
        self.__x = x
        self.__y = y
        self.__color = color

    def execute(self):
        print(f'Pixel is drawn with color {self.__color} in point ({self.__x}, {self.__y})')


class DrawLine(Command):
    def __init__(self, x0, y0, x1, y1, color):
        self.__x0 = x0
        self.__y0 = y0
        self.__x1 = x1
        self.__y1 = y1
        self.__color = color

    def execute(self):
        print(f'Line is drawn with color {self.__color} in points ({self.__x0}, {self.__y0}) ({self.__x1}, {self.__y1})')


class DrawRectangle(Command):
    def __init__(self, x, y, w, h, color):
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h
        self.__color = color

    def execute(self):
        print(f'Rectangle is drawn with color {self.__color} in point ({self.__x}, {self.__y}) w = {self.__w} h = {self.__h}')


class FillRectangle(Command):
    def __init__(self, x, y, w, h, color):
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h
        self.__color = color

    def execute(self):
        print(
            f'Rectangle is filled with color {self.__color} in point ({self.__x}, {self.__y}) w = {self.__w} h = {self.__h}')


class DrawEllipse(Command):
    def __init__(self, x, y, rad_x, rad_y, color):
        self.__x = x
        self.__y = y
        self.__rad_x = rad_x
        self.__rad_y = rad_y
        self.__color = color

    def execute(self):
        print(
            f'Ellipse is drawn with color {self.__color} in point ({self.__x}, {self.__y}) radius_x = {self.__rad_x} radius_y = {self.__rad_y}')


class FillEllipse(Command):
    def __init__(self, x, y, rad_x, rad_y, color):
        self.__x = x
        self.__y = y
        self.__rad_x = rad_x
        self.__rad_y = rad_y
        self.__color = color

    def execute(self):
        print(
            f'Ellipse is filled with color {self.__color} in point ({self.__x}, {self.__y}) radius_x = {self.__rad_x} radius_y = {self.__rad_y}')
