
import socket,os,json

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 12345

sock.connect((host,port))

server_msg = sock.recv(1024).decode()
print("\n Server ---> ",server_msg)

data = {"name":"simran","password":"admin"}
sock.send(json.dumps(data).encode())
print("\n Successfully send")
