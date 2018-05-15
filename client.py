#!/usr/bin/python
'''
    Simple socket client
'''
 
import socket
import sys

if len(sys.argv) < 2:
    print('You need to inform at list one server port.')
    exit()
 
HOST = 'localhost'   # Symbolic name meaning all available interfaces
PORT = int(sys.argv[1]) # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

#Bind socket to local host and port
try:
    s.connect((HOST, PORT))
except socket.error as msg:
    print(msg)
    print('Connect failed. Error Code. ')
    sys.exit()
    
def LoopEcho(s):
    
    while True:
    
        msg = b''
        while msg == b'':
            msg = bytes(input('Type a message(type -q to exit): '),'utf-8')

        if msg == b'-q':
            break

        s.send(msg)

        resp = s.recv(1024)

        print(resp)


if s.recv(1024) == b'accept': 
    print('Socket connection complete')
    LoopEcho(s)
else:
    print('Socket connection refused')

s.close()