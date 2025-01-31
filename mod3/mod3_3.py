

sukupuoli = input("Syötä biologinen sukupuoli (nainen/mies): ")
hemoglobiini = float(input("Syötä hemoglobiiniarvo (g/l): "))

if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiiniarvo on alhainen.")

    elif 117 <= hemoglobiini <= 175:
        print("Hemoglobiiniarvo on normaali.")

    else:
        print("Hemoglobiiniarvo on korkea.")
elif sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif 134 <= hemoglobiini <= 195:
        print("Hemoglobiiniarvo on normaali.")

    else:
        print("Hemoglobiiniarvo on korkea.")
else:
    print("Virheellinen sukupuoli.")