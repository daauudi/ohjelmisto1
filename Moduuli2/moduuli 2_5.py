leiviska_nauloissa=20
naula_luoteina=32
luoti_grammoissa=13.3
leiviskat=int(input("Anna leivisköiden määrä:"))
naulat=int(input("Anna naulojen määrä:"))
luodit=int(input("Anna luotien määrä:"))
kokonais_grammat=((leiviskat* leiviska_nauloissa* naula_luoteina* luoti_grammoissa) +
    (naulat * naula_luoteina * luoti_grammoissa) +
    (luodit * luoti_grammoissa))
kilogrammat=int(kokonais_grammat // 1000)
grammat = kokonais_grammat % 1000
print(f"Antamasi massa on {kilogrammat} kg ja {grammat:.2f} g.")
