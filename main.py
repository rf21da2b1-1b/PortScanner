from socket import *
import time

serverName = '127.0.0.1'
portListe = []
clientSocket = socket(AF_INET, SOCK_STREAM)
print('Så går vi igang')
start = time.time()

for port in range(50):

    print('.')
    try:
        clientSocket.connect((serverName, port))
        portListe.append(port)
        clientSocket.close()
    except:
        val='dummy'

end = time.time()
print('mon der er åbne porte?')
for openPort in portListe:
    print('Åben port på ', openPort)
print('Tiden var ', end-start)


