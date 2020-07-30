
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

data ={
    "name" : ["simran",'sonam','khushi','nehal','komal'],
    "password" : ["admin","password","passwd","adminadmin","passwd"]
}

client_socket.send("Waiting for your data....".encode())

client_msg = client_socket.recv(1024).decode()
