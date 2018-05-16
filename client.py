#!/usr/bin/python
'''
    Simple socket client
'''
 
import socket
import sys

sys.argv.pop(0) #discard script name from list
server_port_list = sys.argv

if len(server_port_list) < 1:
    print('You need to inform at list one server port. Ex: python client.py 1213 1214 1215')
    exit()

def connectToServer():
    global server_port_list

    server = 'localhost'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    for port in server_port_list:
        #Bind socket to local host and port
        try:
            s.connect((server, int(port)))

            if s.recv(1024) == b'accept': 
                return s

        except socket.error:
            pass
    
    print('Cant connect to any server. ')
    sys.exit()
    
def LoopEcho():

    s = connectToServer()
    
    while True:
    
        msg = b''
        while msg == b'':
            try:
                if sys.version_info.major == 3:
                    msg = bytes(input('Type a message(type -q to exit): '),'utf-8') # python 3 needs to inform charset encoding on cast
                else:
                    msg = bytes(input('Type a message(type -q to exit): '))
                    
            except KeyboardInterrupt:
                msg = b'-q'
                break    

        if msg == b'-q':
            return s

        s.send(msg)

        resp = s.recv(1024)

        if resp == b'':
            s = connectToServer()
            s.send(msg)

            resp = s.recv(1024)


        print(resp)

s = LoopEcho()

print('\nClosing connection.')
s.close()