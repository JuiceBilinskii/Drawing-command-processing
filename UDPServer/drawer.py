from PIL import Image, ImageTk, ImageDraw


class Drawer:
    def __init__(self, image):
        self._img_size = image.size
        self._draw_surface = ImageDraw.Draw(image)

    def draw(self, command: tuple):
        if command[0] == b'cd':
            self._draw_surface.rectangle((0, 0) + self._img_size, fill=command[1])
        elif command[0] == b'dp':
            self._draw_surface.point(command[1:-1], fill=command[-1])
        elif command[0] == b'dl':
            self._draw_surface.line(command[1:-1], fill=command[-1])
        elif command[0] == b'dr':
            self._draw_surface.rectangle(command[1:-1], outline=command[-1])
        elif command[0] == b'fr':
            self._draw_surface.rectangle(command[1:-1], outline=command[-1], fill=command[-1])
        elif command[0] == b'de':
            self._draw_surface.ellipse(command[1:-1], outline=command[-1])
        elif command[0] == b'fe':
            self._draw_surface.ellipse(command[1:-1], outline=command[-1], fill=command[-1])
