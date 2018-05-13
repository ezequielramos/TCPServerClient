#!/usr/bin/python
'''
    Simple socket server using threads
'''
 
import socket
import sys

if len(sys.argv) < 3:
    print('You need to inform a server name and a server port. Ex: python server.py S1 1213')
    exit()


SERVERNAME = bytes(sys.argv[1], 'utf-8') 
HOST = 'localhost'   # Symbolic name, meaning all available interfaces
PORT = int(sys.argv[2]) # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print(msg)
    print('Bind failed. Error Code. ')
    sys.exit()
     
print('Socket bind complete')
 
#Start listening on socket
s.listen(10)
print('Socket now listening')
 
#wait to accept a connection - blocking call
conn, addr = s.accept()
print('Connected with ' + addr[0] + ':' + str(addr[1]) )
 
while True:
    #Receiving from client
    data = conn.recv(1024)
    if data == b'':
        break
    reply = SERVERNAME + b': ' + data

    conn.send(reply)

s.close()