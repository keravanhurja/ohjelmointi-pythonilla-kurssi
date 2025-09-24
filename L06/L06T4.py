def kaikki_askeleet(tiedostonimi):
    askeleet = 0
    with open(tiedostonimi, encoding="utf-8") as tiedosto:
        for rivi in tiedosto:
            askeleet += int(rivi.strip())
    return askeleet

def etsi_pienin(tiedostonimi):
    pienin = None
    with open(tiedostonimi, encoding="utf-8") as tiedosto:
        for rivi in tiedosto:
            askeleet = int(rivi.strip())
            if pienin is None or askeleet < pienin:
                pienin = askeleet
    return pienin

def etsi_suurin(tiedostonimi):
    suurin = None
    with open(tiedostonimi, encoding="utf-8") as tiedosto:
        for rivi in tiedosto:
            askeleet = int(rivi.strip())
            if suurin is None or askeleet > suurin:
                suurin = askeleet
    return suurin

def tulosta_ja_tallenna(tallennetiedosto, askeleet, suurin, pienin):
    print(f"Pienin askelmäärä oli {pienin} askelta.")
    print(f"Suurin askelmäärä oli {suurin} askelta.")
    print(f"Yhteensä askelia oli {askeleet} askelta.")
    
    with open(tallennetiedosto, "w", encoding="utf-8") as tiedosto:

        tiedosto.write(f"Pienin askelmäärä oli {pienin} askelta.\n")
        tiedosto.write(f"Suurin askelmäärä oli {suurin} askelta.\n")
        tiedosto.write(f"Yhteensä askelia oli {askeleet} askelta.\n")

def main():
    tiedostonimi = input("Anna tiedot sisältävän tiedoston nimi: ")
    tallennetiedosto = input("Anna tallennettavan tiedoston nimi: ")
    askeleet = kaikki_askeleet(tiedostonimi)
    suurin = etsi_suurin(tiedostonimi)
    pienin = etsi_pienin(tiedostonimi)
    tulosta_ja_tallenna(tallennetiedosto, askeleet, suurin, pienin)
    print("Kiitos ohjelman käytöstä.")


if __name__ == "__main__":
    main()