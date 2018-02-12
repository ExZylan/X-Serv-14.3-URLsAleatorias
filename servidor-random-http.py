#!/usr/bin/python3

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


mySocket.bind(('localhost', 1234))
mySocket.listen(5)

try:
    while True:
        num = random.randint(0,10000000000000)

        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()

        print('HTTP request received:')
        print(recvSocket.recv(1024))

        recvSocket.send(b"HTTP/1.1 200 OK\r\n\r\n" +
                        b"<html><body><h1>Hello.</h1>"
                        b"<p><a href= http://localhost:1234/" +
                        bytes(str(num), 'utf-8') +
                        b">Give me another!</a></p>" +
                        b"</body></html>" +
                        b"\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
