import socket

info = ("127.0.0.1", 12345)

#Create TCP/IP socket
SERVERsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVERsocket.bind(info)

#create a socket specifically for the connection and actively listen

SERVERsocket.listen(10)
msg, addr = SERVERsocket.accept()

while 1:
    data = msg.recv(1024)
    if not data:
        print("Connection closed by client.")
        break
    print(f"{data.decode()} sent to server")
    msg.sendall(data)