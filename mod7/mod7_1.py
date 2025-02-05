def main():

    vuodenajat = ("talvi", "kevät", "kesä", "syksy", "talvi")


    kuukausi = int(input("Syötä kuukauden numero (1-12): "))


    if 1 <= kuukausi <= 12:
        vuodenaika = vuodenajat[(kuukausi % 12) // 3]
        print(f"Kuukausi {kuukausi} kuuluu vuodenaikaan: {vuodenaika}")
    else:
        print("Virheellinen kuukauden numero! Syötä luku väliltä 1-12.")
main()