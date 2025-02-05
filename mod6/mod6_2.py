import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

def paaohjelma():

    tahkot = int(input("Syötä nopan tahkojen määrä (esim. 6 tavalliselle nopalle tai 21 roolipelinopalle): "))

    while True:
        silmaluku = heita_noppaa(tahkot)
        print(f"Heiton tulos: {silmaluku}")
        if silmaluku == tahkot:
            print(f"Sait nopan maksimisilmäluvun {tahkot}! Peli päättyy.")
            break
paaohjelma()