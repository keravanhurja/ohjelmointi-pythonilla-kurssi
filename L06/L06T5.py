global luku1, luku2

luku1 = int()
luku2 = int()

def valikko():
    print(f'Tämä laskin osaa seuraavat toiminnot:\n1) Anna luvut\n2) Summa\n3) Osamäärä\n0) Lopeta')
    toiminto = input("Valitse toiminto (0-3): ")
    return toiminto

def annaLuku(lukutiedosto):
    luvut = []
    for _ in range(2):
        rivi = lukutiedosto.readline()
        if rivi == "":
            print("Luvut loppuivat, lopeta ohjelma.")
            luvut.append(0)
        else:
            luvut.append(int(rivi.strip()))
    print(f"Luettiin luvut {luvut[0]} ja {luvut[1]}")
    return luvut
    
def summa(luku1, luku2):
    sums = luku1 + luku2
    return sums

def paaohjelma():
    tiedostonimi = input("Anna luettavan tiedoston nimi: ")
    lukutiedosto = open(tiedostonimi, "r", encoding="utf-8")
    tulostiedosto = open("L06T5T1.txt", "w", encoding="utf-8")
    

    while True:
        toiminto = valikko()
        if toiminto == "0":
            print("Lopetetaan")
            break

        elif toiminto == "1":
            luvut = annaLuku(lukutiedosto)
            luku1, luku2 = luvut[0], luvut[1]

        elif toiminto == "2":
            sums = summa(luku1, luku2)
            tulostiedosto.write(f"Summa {luku1} + {luku2} = {sums}\n")
            print("Tulos tallennettu tiedostoon.")

        elif toiminto == "3":
            if luku2 == 0:
                print("Nollalla ei voi jakaa.")
            else:
                osamaara = luku1 / luku2
            tulostiedosto.write(f"Osamäärä {luku1} / {luku2} = {round(osamaara, 2)}\n")
            print("Tulos tallennettu tiedostoon.")

    lukutiedosto.close()
    tulostiedosto.close()
    print("Kiitos ohjelman käytöstä.")

paaohjelma()