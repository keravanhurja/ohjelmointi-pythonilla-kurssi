import sys

def luku(luettava, rivit):
    try:
        with open(luettava, "r", encoding="utf-8") as tiedosto:
            for rivi in tiedosto:
                rivi = rivi.strip()
                if rivi:
                    rivit.append(rivi)
    except OSError:
        print(f"Tiedoston '{luettava}' käsittelyssä virhe, lopetetaan.")
        sys.exit()
    return rivit
        

def analyysi(rivit, merkit):
    merkit = []
    edellinen = None
    for rivi in rivit:
        if rivi != edellinen:
            merkit.append(rivi)
            edellinen = rivi
    return merkit

def tulostusKirjoitus(kirjoitettava, merkit):
    if not merkit:
        print("Tiedosto oli tyhjä, yhtään automerkkiä ei tunnistettu.")
    else:
        print(f"Tiedostossa oli {len(merkit)} eri automerkkiä.")
        for merkki in merkit:
            print(merkki)
        try:
            with open(kirjoitettava, "w", encoding="utf-8") as tiedosto:
                for merkki in merkit:
                    tiedosto.write(f"{merkki}\n")
        except OSError:
            print("Tiedoston avaaminen epäonnistui.")
            sys.exit(0)

def main():
    rivit = []
    merkit = []

    luettava = input("Anna luettavan tiedoston nimi: ")
    kirjoitettava = input("Anna kirjoitettavan tiedoston nimi: ")

    rivit = luku(luettava, rivit)
    merkit = analyysi(rivit, merkit)
    tulostusKirjoitus(kirjoitettava, merkit)
    print("Kiitos ohjelman käytöstä.")

if __name__ == "__main__":
    main()