
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #AF_INET --> IPv4, SOCK_STREAM --> TCP Protocol
ip = "192.168.1.4"
port = 1234

sock.connect((ip,port))
print(f"\n Connected to server at ip {ip} and port {port}")
