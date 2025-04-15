import socket

info = ("127.0.0.1", 12345)

CLIENTsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CLIENTsocket.connect(info)
while 1:
    msg = input("You: ")
    data = bytes(msg, "utf-8")

    print(f"sending {msg} to {info[0]} port {info[1]}")
    CLIENTsocket.sendall(data)

    DataFromServer = str(CLIENTsocket.recv(1024))
    print(f"data recieved from server {str(DataFromServer)}")