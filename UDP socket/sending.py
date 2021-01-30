import socket
# import sys


file = open("D:\\Учеба\\МЗКІТ\\Message_example.txt", "r")
MESSAGE = file.read()
MESSAGE = MESSAGE.encode()

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)
# print(sys.getsizeof(MESSAGE))
# print(MESSAGE.__sizeof__())

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
