
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #AF_INET --> IPv4, SOCK_STREAM --> TCP Protocol
ip = "192.168.1.4"
port = 1234

server.bind((ip,port))
print(f"\n The server socket is created at ip {ip} and port {port}")
server.listen()
print("\n Server is ready to listen......")
client_socket,client_addr = server.accept()  #accept will return 2 things 1 --> client socket, client address
print(f"\n Client is at ip {client_addr[0]} and port {client_addr[1]}")

client_socket.send("Hey You are connected....Welcome".encode())

msg = client_socket.recv(1024).decode()
print("\n Client : ",msg)

l = ["bye","byebye","bubye","bye bye","tata","see you"]
while True:
    ser_msg = input("Server ---> ".ljust(50))
    client_socket.send(ser_msg.encode())
    if ser_msg.strip().lower() in l:
        print("\n Server doesn't want to talk to you anymore....")
        client_socket.close()
        break
    client_msg = client_socket.recv(1024).decode()
    print(f"Client ---> {client_msg}".rjust(50))
    if client_msg.strip().lower() in l:
        print("\n Client doesn't want to talk to you anymore")
        client_socket.close()
        break
