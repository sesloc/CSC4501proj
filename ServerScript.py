#!/usr/bin/python

import socket, os, sys              #Imports

sock = socket.socket()              #Create socket
host = socket.gethostname()         #Get local machine name
port = 8000                         #Reserve port
sock.bind((host, port))             #Bind to the port

sock.listen(10)                     #Wait for connection
while True:
    c, addr = sock.accept()         #Establish connection
    print("Connection to", addr)    #Print address of connection
    c.send("connected")             #Send message
    c.close()                       #Close connection
