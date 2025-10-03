import sys

def tLuku(luettava, merkit):
    try:
        with open(luettava, encoding="utf-8") as tiedosto:
            for rivi in tiedosto:
                rivi = rivi.strip()
                if rivi:
                    merkit.append(rivi)

    except (FileNotFoundError, OSError):
        print(f"Tiedoston '{luettava}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

def analyysi(tallennettava, merkit, tiedot):
    eriMerkit = list(set(merkit))
    eriMerkit.sort()

    print(f"Tunnistettiin {len(eriMerkit)} automerkkiä ja {len(merkit)} autoa:")
    tiedot.append(f"Tunnistettiin {len(eriMerkit)} automerkkiä ja {len(merkit)} autoa:\n")

    with open(tallennettava, "w", encoding="utf-8") as tiedosto:
        for merkki in eriMerkit:
            lukumaara = merkit.count(merkki)
            if lukumaara > 1:
                print(f"{merkki}: {lukumaara} autoa")
                tiedot.append(f"{merkki}: {lukumaara} autoa\n")
            else:
                print(f"{merkki}: {lukumaara} auto")
                tiedot.append(f"{merkki}: {lukumaara} auto\n")

def tKirjoita(tallennettava, tiedot):
    try:
        with open(tallennettava, "w", encoding="utf-8") as tiedosto:
            for rivi in tiedot:
                tiedosto.write(rivi)
    except OSError:
        print(f"Tiedoston '{tallennettava}' käsittelyssä virhe, lopetetaan.")

def main():
    merkit = []
    tiedot = []
    luettava = input("Anna luettavan tiedoston nimi: ")
    tallennettava = input("Anna kirjoitettavan tiedoston nimi: ")

    tLuku(luettava, merkit)
    
    if not merkit:
        print("Tiedosto oli tyhjä, yhtään automerkkiä ei tunnistettu.")
    else:
        analyysi(tallennettava, merkit, tiedot)
        tKirjoita(tallennettava, tiedot)
    
    print("Kiitos ohjelman käytöstä.")

if __name__ == "__main__":
    main()