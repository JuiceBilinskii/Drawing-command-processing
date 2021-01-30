import socket
from message_parser import MessageParser
from command_builder import CommandBuilder


UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))

parser = MessageParser()
builder = CommandBuilder()

while True:
    data, addr = sock.recvfrom(1024)
    message = data.decode('utf-8')
    parser.message = message

    parsed_attributes = parser.parse()
    ready_commands = builder.build_commands(parsed_attributes)

    for command in ready_commands:
        command.execute()

    # print(parsed_attributes)
    # print(ready_commands)
