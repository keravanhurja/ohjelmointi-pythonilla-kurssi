import L09T4Kirjasto
import sys

luku1 = int()
luku2 = int()

def valikko():
    print(f'Tämä laskin osaa seuraavat toiminnot:\n1) Anna luvut\n2) Summa\n3) Osamäärä\n0) Lopeta')
    toiminto = input("Valitse toiminto (0-3): ")
    return toiminto

def paaohjelma():
    sisaan = input("Anna luettavan tiedoston nimi: ")

    try:
        with open(sisaan, "r", encoding="utf-8") as f:
            luvut = [int(rivi.strip()) for rivi in f if rivi.strip()]
    except FileNotFoundError:
        print(f"Tiedoston '{sisaan}' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)

    ulos = input("Anna kirjoitettavan tiedoston nimi: ")
    
    tulokset = []
    indeksi = 0
    luku1 = luku2 = None
    tiedosto_luettu = False

    while True:
        toiminto = valikko()
        
        if toiminto == "1":
            if not tiedosto_luettu:
                print(f"Luettu tiedosto '{sisaan}'.")
                tiedosto_luettu = True
            if indeksi + 1 >= len(luvut):
                print("Luvut loppuivat, lopeta ohjelma.")
                luku1 = luku2 = None
            else:
                luku1 = luvut[indeksi]
                luku2 = luvut[indeksi + 1]
                indeksi += 2
                print(f"Luettiin luvut {luku1} ja {luku2}")

        elif toiminto == "2":
            tulos = f"Summa {luku1} + {luku2} = {luku1 + luku2}"
            print("Tulos lisätty listaan.")
            tulokset.append(tulos)

        elif toiminto == "3":
            if luku2 == 0:
                print("Nollalla ei voi jakaa.")
            else:
                osamaara = luku1 / luku2
            tulos = f"Osamäärä {luku1} / {luku2} = {round(osamaara, 2)}"
            print("Tulos lisätty listaan.")
            tulokset.append(tulos)
        
        elif toiminto == "0":
            try:
                with open(ulos, "w", encoding="utf-8") as f:
                    for rivi in tulokset:
                        f.write(rivi + "\n")
                print(f"Tallennettu tiedosto '{ulos}'.")
            except OSError:
                print(f"Tiedoston '{ulos}' käsittelyssä virhe, lopetetaan.")
                sys.exit(0)
            break

        else:
            print("Tuntematon valinta, yritä uudestaan.")

    print("Kiitos ohjelman käytöstä.")

paaohjelma()