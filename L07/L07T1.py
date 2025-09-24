def main():
    ostoslista =  []
    while True:
        print(f"Ostoslistasi sisältää seuraavat tuotteet:\n{ostoslista}")
        print("Voit valita alla olevista toiminnoista:")
        print("1) Lisää")
        print("2) Poista")
        print("0) Lopeta")
        toiminto = input("Valintasi: ")

        if toiminto == "0":
            print(f"Sinulta jäi ostamatta seuraavat tuotteet:\n{ostoslista}")
            break

        elif toiminto == "1":
            tuote = input("Anna lisättävä tuote: \n")
            ostoslista.append(tuote)

        elif toiminto == "2":
            if not ostoslista:
                print("Lista on tyhjä, ei voida poistaa.")
            else:
                print(f"Ostoslistassasi on {len(ostoslista)} tuotetta.")
                indeksi = int(input("Anna poistettavan tuotteen järjestysnumero: \n"))
                if 0 < indeksi <= len(ostoslista):
                    poistettu = ostoslista.pop(indeksi - 1)
        else:
            print("Tunnistamaton valinta.\n")
    print("Kiitos ohjelman käytöstä.")

if __name__ == "__main__":
    main()