import sys

def lue(luettava, lista):
    try:
        rivit = 0

        with open(luettava, "r", encoding="utf-8") as tiedosto:
            for rivi in tiedosto:
                lista.append(rivi.strip())
                rivit += 1
        print(f"Tiedoston '{luettava}' lukeminen onnistui, {rivit} riviä.")

    except OSError:
        print(f"Tiedoston '{luettava}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

def kirjoita(kirjoitettava, lista):
    try:
        with open(kirjoitettava, "w", encoding="utf-8") as tiedosto:
            for rivi in lista:
                tiedosto.write(rivi + "\n")
        print(f"Tiedostoon '{kirjoitettava}' kirjoittaminen onnistui.")

    except OSError:
        print(f"Tiedoston '{kirjoitettava}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

def main():
    lista = []
    luettava = input("Anna luettavan tiedoston nimi: ")

    lue(luettava, lista)

    kirjoitettava = input("Anna kirjoitettavan tiedoston nimi: ")

    kirjoita(kirjoitettava, lista)

    print("Kiitos ohjelman käytöstä.")
            
if __name__ == "__main__":
    main()