'''
    Simple socket server using threads
'''
 
import socket
import sys
 
HOST = 'localhost'   # Symbolic name, meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg) + ' Message ')
    sys.exit()
     
print('Socket bind complete')
 
#Start listening on socket
s.listen(10)
print('Socket now listening')
 
#wait to accept a connection - blocking call
conn, addr = s.accept()
print('Connected with ' + addr[0] + ':' + str(addr[1]) )
 
#Receiving from client
data = conn.recv(1024)
print(data)
reply = b'OK...' + data

conn.send(reply)

s.close()