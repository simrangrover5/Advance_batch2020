import socket,os

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 12345

sock.connect((host,port))

server_msg = sock.recv(1024).decode()
print("\n Server ---> ",server_msg)

path = input("\n Enter the path of file that you want to share : ")
sock.send(path.encode())

server_msg = sock.recv(1024).decode()
print("\n Server ---> ",server_msg)
if "does not exist" in server_msg:
    sock.close()
else:
    filename = input("\n Enter name of file by where you want to save with extension : ")  #C://batches//xyz
    if "//" in filename:
        l = filename.split("//")[:-1]
        path1 = "//".join(l)
    if "\\" in filename:
        l = filename.split("\\")[:-1]
        path1 = "//".join(l)
    elif "/" in filename:
        l = filename.split("/")[:-1]
        path1 = "//".join(l)
    else:
        print("\n Incorrect path....")
        sock.close()
    if os.path.exists(path1) and filename.split(".")[-1] == path.split(".")[-1]:
        with open(filename,"wb") as fp:
            line = sock.recv(1024)
            while line:
                fp.write(line)
                line = sock.recv(1024)
            else:
                print("\n The file is received successfully")
    else:
        print("\n Incorrect Extension")
        sock.close()
