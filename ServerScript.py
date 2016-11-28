#!/usr/bin/python

import socket                       #Imports

sock = socket.socket()              #Create socket
#host = socket.gethostname()         #Get local machine name
host = '10.0.0.1'
port = 12397                        #Reserve port
sock.bind((host, port))
#sock.bind(('', port))               #Bind to the port

sock.listen(5)                      #Wait for connection
while True:
    c, addr = sock.accept()         #Establish connection
    print("Connection to", addr)    #Print address of connection
    c.send("connected")             #Send message
    message = c.recv(1024)		    #Recieve from host
    print message
#    c.close()                       #Close connection
