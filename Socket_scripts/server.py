
### server_file

import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #AF_INET --> IPv4, SOCK_STREAM --> TCP Protocol
ip = "192.168.1.4"
port = 1234

server.bind((ip,port))
print(f"\n The server socket is created at ip {ip} and port {port}")
server.listen()
print("\n Server is ready to listen......")
client_socket,client_addr = server.accept()  #accept will return 2 things 1 --> client socket, client address
print(client_socket)
print(client_addr)
