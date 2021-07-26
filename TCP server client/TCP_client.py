from socket import *

host = "192.168.1.104"

port = 9999

s = socket(AF_INET, SOCK_STREAM)

s.connect((host, port))

message = "hi there server"

s.send(message.encode('ascii'))

Rcv_msg = s.recv(1024)

print(Rcv_msg.decode('ascii'))

s.close()
