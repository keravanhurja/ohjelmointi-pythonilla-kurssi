def tiedostoKirjoita(tNimi):
    while True:
        with open(tNimi, "a") as tiedosto:
            nimi = input("Anna tiedostoon tallennettava nimi (0 lopettaa): ")
            if nimi == "0":
                break
            tiedosto.write(nimi+"\n")
        
def tiedostoLue(tNimi):
    with open(tNimi) as tiedosto:
            for x in tiedosto:
                print(x)
def main():
    tNimi = input("Anna tallennettavan tiedoston nimi: ")
    tNimi += ".txt"
    tiedostoKirjoita(tNimi)
    tiedostoLue(tNimi)
    print("Kiitos ohjelman käytöstä.")

if __name__ == "__main__":
    main()