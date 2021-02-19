from tkinter import Canvas


class Drawer:
    def __init__(self, canvas: Canvas):
        self._canvas = canvas

    def draw(self, command: tuple):
        if command[0] == b'cd':
            self._canvas.delete('all')
            self._canvas.configure(bg=command[1])
        elif command[0] == b'dp':
            self._canvas.create_line(*command[1:-1], fill=command[-1])
        elif command[0] == b'dl':
            self._canvas.create_line(*command[1:-1], fill=command[-1])
        elif command[0] == b'dr':
            self._canvas.create_rectangle(*command[1:-1], outline=command[-1])
        elif command[0] == b'fr':
            self._canvas.create_rectangle(*command[1:-1], outline=command[-1], fill=command[-1])
        elif command[0] == b'de':
            self._canvas.create_oval(*command[1:-1], outline=command[-1])
        elif command[0] == b'fe':
            self._canvas.create_oval(*command[1:-1], outline=command[-1], fill=command[-1])
            # w.create_line(event.x, event.y, event.x + 1, event.y, fill="#ff0000")
