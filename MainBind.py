from socket import *
import time

serverName = '127.0.0.1'

portListe = []
print('Så går vi igang')
start = time.time()

for port in range(50):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    try:
        #print(port)
        serverSocket.bind((serverName, port))
        serverSocket.close()
    except:
        portListe.append(port)

end = time.time()
print('mon der er åbne porte?')
for openPort in portListe:
    print('Åben port på ', openPort)

print('Tiden var ', end-start)