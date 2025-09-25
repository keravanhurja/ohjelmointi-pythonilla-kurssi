import L08T5Kirjasto

def valikko():
    print("Mitä haluat tehdä:")
    print("1) Lue tiedosto")
    print("2) Analysoi tiedot")
    print("3) Tallenna Tulokset")
    print("0) Lopeta")

    valinta = input("Valintasi: ")
    return valinta


def main():
    valinta = ""
    luetuttiedot = []
    analysoidut = []

    luettava = input("Anna luettavan tiedoston nimi: ")
    kirjoitettava = input("Anna kirjoitettavan tiedoston nimi: ")

    while True:
        valinta = valikko()

        if valinta == "1":
            L08T5Kirjasto.lue_tiedosto(luettava, luetuttiedot)
        elif valinta == "2":
            L08T5Kirjasto.analysoi_tiedot(luetuttiedot, analysoidut)
        elif valinta == "3":
            L08T5Kirjasto.tallenna_tulokset(kirjoitettava, analysoidut)
        elif valinta == "0":
            break
        else:
            print("Virheellinen valinta, yritä uudelleen.")
    print("Kiitos ohjelman käytöstä.")
        
if __name__ == "__main__":
    main()