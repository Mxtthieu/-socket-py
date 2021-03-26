from socket import *
import time
import sys
import select

if len(sys.argv) != 3:
    sys.exit(-1)

host = sys.argv[1]
port = int(sys.argv[2])
mysocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
myself = gethostname()
mysocket.connect((host, port))

list1 = []
list1.append(mysocket)
x = ""

while x != "FIN" :
    [read,_,_] = select.select(list1,[],[])
    if sys.stdin in read:
        x = sys.stdin.readline() 
        message = x +"\n"
        time.sleep(1)
        message_bytes = bytes(message, "utf-8")
        sent = mysocket.send(message_bytes)
    if mysocket in read:
        mysocket.recv(1000)
mysocket.close()


