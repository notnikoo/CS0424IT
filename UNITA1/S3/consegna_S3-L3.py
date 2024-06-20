import math


def perimQuadrato():
    lato= float(input("Inserisci la lunghezza del lato: "))
    perimetro = 4*lato
    print(f"Il perimetro è: {perimetro}")                          


def perimTriangolo():
    print("Inserisci i tre lati: ")
    lato1 = float(input("Primo lato: "))
    lato2 = float(input("Secondo lato: "))
    lato3 = float(input("Terzo lato: "))
    perimetro = lato1+ lato2+ lato3
    print(f"Il perimetro del triangolo è: {perimetro}")

def perimRettangolo():
    base = float(input("Inserisci la base: "))
    altezza = float(input("Inserisci l'altezza: "))
    perimetro = 2*base+2*altezza
    print(f"Il perimetro del rettangolo è: {perimetro}")

def perimCerchio():
    raggio = float(input("Inserisci il raggio: "))
    perimetro = 2*raggio*math.pi
    print(f"Il perimetro del cerchio è: {perimetro}")


print("Di quale figura vuoi calcolare il perimetro?")
print("1-quadrato")
print("2-triangolo")
print("3-rettangolo")
print("4-cerchio")
print("5- Uscire")

scelta = int(input())
if scelta== 1 :
    perimQuadrato()
elif scelta == 2:
    perimTriangolo()
elif scelta==3:
    perimRettangolo()
elif scelta==4:
    perimCerchio()
elif scelta==5:
    print("Hai terminato il programma. Ciao")
else:
    print("Scelta non valida, inserisci un numero tra quelli proposti.")


