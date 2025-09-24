global luku1, luku2

luku1 = int()
luku2 = int()

def valikko():
    print(f'Tämä laskin osaa seuraavat toiminnot:\n1) Anna luvut\n2) Summa\n3) Osamäärä\n0) Lopeta')
    toiminto = input("Valitse toiminto (0-3): ")
    return toiminto

def annaLuku():
        global luku1, luku2
        luku1 = int(input("Anna ensimmäinen luku: "))
        luku2 = int(input("Anna toinen luku: "))
        return luku1, luku2
    
def summa():
    summa = luku1 + luku2
    return summa

def paaohjelma():
    while True:
        toiminto = valikko()
        if toiminto == "0":
            print("Lopetetaan")
            break

        elif toiminto == "1":
            annaLuku()
            print(f"Annoit luvut {luku1} ja {luku2}")

        elif toiminto == "2":
            summa()
            print(f"Summa {luku1} + {luku2} = {summa()}")

        elif toiminto == "3":
            if luku2 == 0:
                print("Nollalla ei voi jakaa.")
            else:
                osamaara = luku1 / luku2
                print(f"Osamäärä {luku1} / {luku2} = {round(osamaara, 2)}")

    print("Kiitos ohjelman käytöstä.")

paaohjelma()