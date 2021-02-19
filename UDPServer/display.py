from tkinter import *
from UDPServer.drawer import Drawer
from UDPServer.command_converter import CommandConverter
import threading
import sys
# from UDPServer import receiving


def receiving():
    import socket
    from message_parser import MessageParser
    from command_converter import CommandConverter

    UDP_IP = "127.0.0.2"
    UDP_PORT = 5005

    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    sock.bind((UDP_IP, UDP_PORT))

    parser = MessageParser()
    builder = CommandConverter()

    while True:
        data, address = sock.recvfrom(50)
        print(data)

        parser.parse(data)
        if parser.error:
            print(parser.message)
        else:
            drawer.draw(converter.convert_command(parser.parsed_message))
            print('Received command: ', parser.parsed_message)

root = Tk()

canvas = Canvas(root, width=300, height=200, bg='white')
canvas.pack(padx=20, pady=20)

drawer = Drawer(canvas)
converter = CommandConverter()


# command = (b'dl', 10, 10, 20, 50, b'ff0000')
# commands = (b'cd', b'00ff00'), (b'fe', 250, 60, 300, 110, b'ff0000'), (b'dl', 10, 10, 20, 50, b'ff0000'), (b'de', 45, 45, 30, 50, b'21414a')
# , (b'de', 45, 45, 30, 50, b'21414a'), (b'fe', 12, 20, 30, 20, b'181c18')

#for command in commands:
#    drawer.draw(converter.convert_command(command))

x = threading.Thread(target=receiving)
x.daemon = True
x.start()

root.mainloop()
