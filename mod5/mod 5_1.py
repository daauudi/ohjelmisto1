import random


nopat = int(input("Syötä arpakuutioiden lukumäärä: "))

summa = 0

for i in range(nopat):

    silmaluku = random.randint(1, 6)

    summa += silmaluku

print(f"Silmälukujen summa on: {summa}")