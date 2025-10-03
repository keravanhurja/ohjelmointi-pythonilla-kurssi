import sys

def prosessi(luettava, vuodet):
    with open(luettava, encoding="utf-8") as tiedosto:
        next(tiedosto)  # skip header
        for rivi in tiedosto:
            osat = rivi.strip().split(";")
            if len(osat) < 2:
                continue
            pvm = osat[1]
            if len(pvm) < 4:
                continue
            vuosi = pvm[:4]  # get first 4 chars
            if vuosi.isdigit():
                vuodet[vuosi] = vuodet.get(vuosi, 0) + 1

    print("Autot lajiteltuna vuosiluvun mukaan laskevaan järjestykseen.")
    print("Vuosi: Autoja")
    for vuosi in sorted(vuodet.keys(), reverse=True):
        print(f"{vuosi}: {vuodet[vuosi]}")

    print(f"Yhteensä {sum(vuodet.values())} autoa.")


def main():
    vuodet = {}
    luettava = input("Anna luettavan tiedoston nimi: ")
    try:
        prosessi(luettava, vuodet)
    except (FileNotFoundError, OSError):
        print(f"Tiedoston '{luettava}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

    print("Kiitos ohjelman käytöstä.")

if __name__ == "__main__":
    main()