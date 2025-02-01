
luvut = []

while True:
    syote = input("Syötä luku (tai paina Enter lopettaaksesi): ")
    if syote == "":
        break
    try:
        luku = int(syote)
        luvut.append(luku)
    except ValueError:
        print("Virheellinen syöte. Syötä kokonaisluku.")


luvut.sort(reverse=True)


print("Viisi suurinta lukua suuruusjärjestyksessä:")
for luku in luvut[:5]:
    print(luku)