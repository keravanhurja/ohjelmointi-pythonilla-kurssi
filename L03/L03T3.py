luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
print(f'Laskin osaa seuraavat toiminnot:\n1) Summa\n2) Erotus\n3) Tulo\n4) Osamäärä\n5) Potenssi\nAntamasi luvut ovat {luku1} ja {luku2}')
toiminto = input("Valitse toiminto (1-5): ")
if toiminto == "1":
    print(f'Summa {luku1} + {luku2} = {luku1 + luku2}')
elif toiminto == "2":
    print(f'Erotus {luku1} - {luku2} = {luku1 - luku2}')
elif toiminto == "3":
    print(f'Tulo {luku1} * {luku2} = {luku1 * luku2}')
elif toiminto == "4":
    if luku2 != 0:
        print(f'Osamäärä {luku1} / {luku2} = {luku1 / luku2}')
    else:
        print("Nollalla ei voi jakaa.")
elif toiminto == "5":
    print(f'Potenssi {luku1} ** {luku2} = {luku1 ** luku2}')
print("Kiitos ohjelman käytöstä.")