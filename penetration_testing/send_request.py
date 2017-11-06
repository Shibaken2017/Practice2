import socket
import sys
#send requst

TCP_IP="127.0.0.1"
TCP_PORT=8090
BUFFER_SIZE=1024
MESSAGE_TO_SERVER=b"HELLO WORLD"



try:
    tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as e:
    print("error occured wihile creating{}  {}".format(e[0],e[1]))
    sys.exit()

tcp_socket.connect((TCP_IP,TCP_PORT))




try:
    tcp_socket.send(MESSAGE_TO_SERVER)
except socket.error as e:
    print("{}  {}".format(str(e[0]),str(e[1])))
    sys.exit()

print("message to server send succesfully")
data=tcp_socket.recv(BUFFER_SIZE)
tcp_socket.close()
