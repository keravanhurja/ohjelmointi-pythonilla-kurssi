def tiedostoKirjoita(tNimi):
    with open(tNimi, "w") as tiedosto:
        while True:
            nimi = input("Anna tiedostoon tallennettava nimi (0 lopettaa): ")
            if nimi == "0":
                print(f"Tiedostoon '{tNimi}' on tallennettu seuraavat nimet:")
                break
            tiedosto.write(nimi+"\n")
        
def tiedostoLue(tNimi):
    with open(tNimi) as tiedosto:
            for rivi in tiedosto:
                print(rivi.strip())
def main():
    tNimi = input("Anna tallennettavan tiedoston nimi: ")
    tiedostoKirjoita(tNimi)
    tiedostoLue(tNimi)
    print("Kiitos ohjelman käytöstä.")

if __name__ == "__main__":
    main()