import socket

#create a socket object
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#get local machine name
host=socket.gethostbyname("127.0.0.1") 
port=1234

#connection to a hostname on port
s.connect((host,port))

#Receive no more than 1024 bytes
msg=s.recv(1024)
s.close()

print(msg.decode('ascii'))

