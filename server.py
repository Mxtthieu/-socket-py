from socket import *
import sys
mysocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)

port = int(sys.argv[1])
mysocket.bind(('',port))
mysocket.listen(1)

(socketClient,_) = mysocket.accept()
while True:
    msg = socketClient.recv(1000)
    if len(msg)  == 0:
        # n'arrive que si le client est parti
        break
    message = str(msg, 'utf-8')
    print(message)
socketClient.close()    
mysocket.close()
