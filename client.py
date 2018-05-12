'''
    Simple socket client
'''
 
import socket
import sys
 
HOST = 'localhost'   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

#Bind socket to local host and port
try:
    s.connect((HOST, PORT))
except socket.error as msg:
    print('Connect failed. Error Code : ' + msg + ' Message ')
    sys.exit()
    
print('Socket connection complete')

msg = b'Test'

s.send(msg)

resp = s.recv(1024)

print(resp)

s.close()