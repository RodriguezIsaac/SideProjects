#todo Client used to connect to the self server script from "Sockets and Network Programming" file

import socket

#Creates a TCP (Connection Oriented) Internet Socket (socket.AF_INET)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Connects to the specified server socket
s.connect(("192.168.0.7", 55555))
#Recieves the message that the client sends by the specified amount of bytes (1024)
message = s.recv(1024)
s.close()

print(message.decode())