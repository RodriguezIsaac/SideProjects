#Sockets are endpoints in a communication system
#Protocols: TCP (socket.SOCK_STREAM) & UDP (socket.SOCK_DGRAM)

#todo Code for essentially a self-made server
import socket

#Creates a TCP (Connection Oriented) Internet Socket (socket.AF_INET)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Creates a tuple of the ip address being used & the port the socket is going to run on
s.bind(("192.168.0.7", 55555))

#Makes the socket listen for possible connections (listening socket)
s.listen()

#Loop which accepts connection
while True:
    #s.accept is the method used to accept the connection
    client, address = s.accept()
    print("Connected to {}".format(address))
    #Sends encoded message to the client that connects to the server
    client.send("You are connected".encode("UTF-8"))
    #Closes client
    client.close()