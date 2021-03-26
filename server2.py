from socket import *
import sys
import select
mysocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)

port = int(sys.argv[1])
mysocket.bind(('',port))
mysocket.listen(1)

clients = []
clients.append(mysocket)

while len(clients) > 0:
    [read,_,_] = select.select(clients,[],[])
    # Si read contient la socket d'écoute, alors il y a un client à accepter
    if mysocket in read:
        (socketClient,_) = mysocket.accept()
        clients.append(socketClient)
    for s in clients:
        # On recv les messages sauf si la socket est la socket d'écoute
        if s != mysocket:
            msg = s.recv(1000)
            if len(msg) == 0:
                s.close()
                clients.remove(s)
            else:
                message = str(msg, 'utf-8')
                print(message)
                message = bytes(message, "utf-8")
                #s.send(message)
mysocket.close()
