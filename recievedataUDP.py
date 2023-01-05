from asyncio.windows_events import NULL
import socket
import string
import sys
from struct import unpack
import json
from telnetlib import KERMIT
from time import time
import matplotlib.pyplot as plt
import csv


def messageclean(message):
    message2 = ""
    for i in range(len(message)):
        if message[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ","]:
            message2 += message[i]
    return[float(message2[0:4]), float(message2[5:])]


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
host, port = '0.0.0.0', 65000
server_address = (host, port)

print(f'Starting UDP server on {host} port {port}')
sock.bind(server_address)
x = []
y = []
i = 0

# open the file in the write mode
f = open('C:\\Users\\Hp\\Desktop\\P2M Codes\\data.csv', 'a')

# create the csv writer
writer = csv.writer(f)

while True:
    try:
        # Wait for message
        message, address = sock.recvfrom(4096)
        # Print message
        message = message.decode('utf8').replace("'", '"')
        print(message)
        print(address)
        x.append(messageclean(message)[1])
        y.append(messageclean(message)[0])
        print(x[i], y[i])
        if x[i] and y[i]:
            writer.writerow([x[i], y[i], "tag"])
        #fig, ax = plt.subplots()
        #ax.scatter(x, y)
        # plt.show()
    except KeyboardInterrupt:
        break

f.close()
print("Done")
