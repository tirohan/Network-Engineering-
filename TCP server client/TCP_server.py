from socket import *

host = "192.168.1.104"

port = 9999

s = socket(AF_INET, SOCK_STREAM)

s.bind((host, port))

s.listen(5)

while True:

    c,addr = s.accept()
    print("[+] Got connection from ", addr)

    Rcv_msg = c.recv(1024)
    print(Rcv_msg.decode('ascii'))

    message = "hi there client"
    c.send(message.encode('ascii'))
    c.close()