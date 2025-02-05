import random

def heita_noppaa():
    return random.randint(1, 6)



def paaohjelma():
    while True:
        silmaluku = heita_noppaa()
        print(f"Heiton tulos: {silmaluku}")
        if silmaluku == 6:
            print("Sait kuutosen! Peli päättyy.")
            break

paaohjelma()