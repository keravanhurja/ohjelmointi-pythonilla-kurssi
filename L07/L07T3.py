def main():
    tiedostonimi = input("Anna tiedoston nimi: ")
    with open(tiedostonimi, "r", encoding="utf-8") as tiedosto:
        otsikko = tiedosto.readline()
        for rivi in tiedosto:
            osat = rivi.strip().split(";")
            if len(osat) == 3:
                marjan_nimi = osat[0]
                kellonaika = osat[2]
                print(f"Kello oli {kellonaika}, kun punnittiin marjoja {marjan_nimi}.")
    print("Kiitos ohjelman käytöstä.")

if __name__ == "__main__":
    main()