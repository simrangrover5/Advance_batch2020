
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #AF_INET --> IPv4, SOCK_STREAM --> TCP Protocol
ip = "192.168.1.4"
port = 1234

sock.connect((ip,port))
print(f"\n Connected to server at ip {ip} and port {port}")

msg = sock.recv(1024).decode()
print("\n Server : ",msg)

sock.send("Thankyou".encode())
l = ["bye","byebye","bubye","bye bye","tata","see you"]
while True:
    ser_msg = sock.recv(1024).decode().strip().lower()
    print(f"Server ---> {ser_msg}".rjust(50))
    if ser_msg in l:
        print("\n Server doesn't want to talk to you anymore")
        break
    client_msg = input("Client ---> ".ljust(50))
    sock.send(client_msg.encode())
    if client_msg in l:
        print("\n Client doesn't want to talk to you anymore")
        break
