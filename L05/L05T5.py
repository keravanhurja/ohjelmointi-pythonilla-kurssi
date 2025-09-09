luku1 = int()
luku2 = int()

while True:
    print(f'Tämä laskin osaa seuraavat toiminnot:\n1) Anna luvut\n2) Summa\n3) Erotus\n4) Tulo\n5) Osamäärä\n6) Potenssi\n0) Lopeta')
    toiminto = input("Valitse toiminto (0-6): ")

    if toiminto == "0":
        print("Lopetetaan")
        break
    elif toiminto == "1":
        luku1 = int(input("Anna ensimmäinen luku: "))
        luku2 = int(input("Anna toinen luku: "))
        print(f'Annoit luvut {luku1} ja {luku2}')
    elif toiminto == "2":
        print(f'Summa {luku1} + {luku2} = {luku1 + luku2}')
    elif toiminto == "3":
        print(f'Erotus {luku1} - {luku2} = {luku1 - luku2}')
    elif toiminto == "4":
        print(f'Tulo {luku1} * {luku2} = {luku1 * luku2}')
    elif toiminto == "5":
        if luku2 != 0:
            print(f'Osamäärä {luku1} / {luku2} = {round(luku1 / luku2, 2)}')
        else:
            print("Nollalla ei voi jakaa.")
    elif toiminto == "6":
        print(f'Potenssi {luku1} ** {luku2} = {luku1 ** luku2}')
    else:
        print("Tuntematon valinta, yritä uudestaan.")
print("Kiitos ohjelman käytöstä.")