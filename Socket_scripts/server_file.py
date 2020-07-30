
import os
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 12345

server.bind((host,port))
server.listen()
print("\n Server is ready to listen.......")

client_socket,client_addr = server.accept()
print(f"\n The client is at ip {client_addr[0]} and port{client_addr[1]}")

client_socket.send("\n Okay waiting for your path of file".encode())

path = client_socket.recv(1024).decode()

if os.path.exists(path) and os.path.isfile(path):
    client_socket.send("\n The file is on the way.......Please Wait".encode())
    f = open(path,'rb')
    data = f.readline()
    while data:
        client_socket.send(data)
        data = f.readline()
    else:
        print('\n Successfully send the file')
else:
    client_socket.send("\n The path does not exist....Please send the correct path".encode())
    print("\n The path asked by the client was not correct")
    client_socket.close()
    server.close()
