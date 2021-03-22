from tkinter import *
from PIL import Image, ImageTk
from UDPServer.drawer import Drawer
import threading


def receiving():
    import socket
    from message_parser import MessageParser
    from command_converter import CommandConverter

    # UDP_IP = "192.168.0.32"
    UDP_IP = "192.168.1.121"
    UDP_PORT = 5005

    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    sock.bind((UDP_IP, UDP_PORT))

    parser = MessageParser()

    while True:
        data, address = sock.recvfrom(1024)
        print(data)

        parser.parse(data)
        if parser.error:
            print(parser.message)
        else:
            drawer.draw(CommandConverter.convert_command(parser.parsed_message))
            image_tk = ImageTk.PhotoImage(image)

            canvas.delete('all')
            canvas.create_image(150, 100, image=image_tk)
            print('Received command: ', parser.parsed_message)


root = Tk()
canvas = Canvas(root, width=300, height=200, bg='white')
canvas.pack(padx=20, pady=20)

image = Image.new("RGB", (300, 200), (0, 0, 0))

drawer = Drawer(image)

x = threading.Thread(target=receiving)
x.daemon = True
x.start()

root.mainloop()
