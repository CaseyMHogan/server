
# Skeleton Python Code for the Web Server

#import socket module
from socket import *
import _socket;

import sys # In order to terminate the program

#AF_INET = IPV4, SOCK_STREAM = TCP
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
#Fill in start
port = 1234
hostname = _socket.gethostname()    
ip = _socket.gethostbyname(hostname) 

# I am very sorry I think that my code is wrong, I was not able to get remote machines to work with the
# ip from above. So this current code is working with a local host.
serverSocket.bind(('', port))

#Only one connection at a time.
serverSocket.listen(1)

#Fill in end

while True:

 #Establish the connection

 print("Ready to serve...")

 connectionSocket, addr = serverSocket.accept()

 try:
     print(f"Success! {addr} has been successfully connected")

     message = connectionSocket.recv(1024)

     filename = message.split()[1]

     f = open(filename[1:])

     outputdata = f.read()

     #Send one HTTP header line into socket

     #Fill in start
     connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n")
     #connectionSocket.send(outputdata.encode('utf-8'))
     #Fill in end

     #Send the content of the requested file to the client
     for i in range(0, len(outputdata)):

        connectionSocket.send(outputdata[i].encode())

     connectionSocket.send("\r\n".encode())

     connectionSocket.close()
 except IOError:
     #Send response message for file not found
     #Fill in start 
     print("Error 404 file not found!")
     connectionSocket.send(b"HTTP/1.1 404 file Not Found\r\n\r\n")
     #Fill in end

     #Close client socket
     #Fill in start
     connectionSocket.close()
     continue
     #Fill in end

serverSocket.close()

sys.exit()#Terminate the program after sending the corresponding data 
