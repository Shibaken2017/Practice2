#socketは他のコンピュータとunix_file記述でやり取りする方法である
import socket
import sys
try:
    tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print(socket.AF_INET)
    print(socket.SOCK_STREAM)
except socket.error as e:
    print(str(e))
    sys.exit()

print("success")

