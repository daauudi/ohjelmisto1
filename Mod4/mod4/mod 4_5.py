
oikea_tunnus = "python"
oikea_salasana = "rules"


yritykset = 0

while yritykset < 5:
    tunnus = input("Syötä käyttäjätunnus: ")
    salasana = input("Syötä salasana: ")



    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa!")
        break
    else:
        print("Väärä käyttäjätunnus tai salasana.")
        yritykset += 1

if yritykset == 5:
    print("Pääsy evätty.")