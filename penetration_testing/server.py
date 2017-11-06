import socket
import sys
TCP_IP="127.0.0.1"
TCP_PORT=8090
BUFFER_SIZE=1024
try:
    tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as e:
    print("error cocured {} errormessage{}".format(e[0],e[1]))

    sys.exit()


tcp_socket.bind((TCP_IP,TCP_PORT))
tcp_socket.listen(2)
print("listening")

while True:
    connection,addres=tcp_socket.accept()
    print("client connected")

    data=connection.recv(BUFFER_SIZE)
    connection.sendall(b"thanks for cconect")
