class Auto:
    def __init__(self, merkki, hinta):
        self.merkki = merkki
        self.hinta = hinta

def main():
    autot = []
    print("Tämä ohjelma lisää autojen tietoja listaan ja tulostaa ne.")
    while True:
        print("Käytettävissä olevat toiminnot:")
        print("1) Anna auton tiedot")
        print("2) Tulosta autojen tiedot")
        print("0) Lopeta")

        valinta = input("Valintasi: ")

        if valinta == "1":
            merkki = input("Anna auton merkki: ")
            hinta = int(input("Anna auton hinta: "))
            print()
            auto = Auto(merkki, hinta)
            autot.append(auto)

        elif valinta == "2":
            if not autot:
                print("Ei autoja listattavana.")
            else:
                print("Listalta löytyy seuraavat automerkit ja hinnat:")
                for i, auto in enumerate(autot, start=1):
                    print(f"{auto.merkki} {auto.hinta}")
                print()
        
        elif valinta == "0":
            print("Kiitos ohjelman käytöstä.")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.\n")

if __name__ == "__main__":
    main()