import socket, platform, os									#importo le librerie che gestiscono le comunicazioni di rete, il sistema operativo e il file system

SRV_ADDR = "127.0.0.1"			           					#il server sarà in ascolto all'indirizzo 127.0.0.1 alla porta 1234
SRV_PORT = 1234

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)		#crea un socket ipv4 che utilizza il protocollo TCP
s.bind((SRV_ADDR, SRV_PORT))					            #il socket viene associato all'indirizzo e porta che ho specificato							
s.listen(1)							                        #Il socket è in ascolto
connection, address = s.accept()				            #accetta la connessione in entrata

print("client connected: ", address)

while 1:
	try:
		data = connection.recv(1024)			            #tenta di ricevere dati dal socket
	except:continue

	if(data.decode('utf-8') == '1'):			            #se premo 1 il server risponde con le informazioni sul sistema operativo
		tosend = platform.platform() + " " + platform.machine()
		connection.sendall(tosend.encode())
	elif(data.encode('utf-8') == '2'):			            #se premo 2 il socket aspetta un path di directory e elenca i file nella directory
		data=connection.recv(1024)
		try:
			filelist = os.listdir(data.decode('utf-8'))
			tosend = ""
			for x in filelist:
				tosend += "," + x
		except:
			tosend = "wrong path"
		connection.sendall(tosend.encode())
	elif(data.decode('utf-8')) == '0':			            #se premo 0 chiude la connessione
		connection.close()
		connection, address = s.accept()