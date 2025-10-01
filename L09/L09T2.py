def iError():
    lista = [11, 22, 33, 44, 55]
    indeksi = int(input("Anna indeksi 0-4: "))
    try:
        print(f"Listan arvo on {lista[indeksi]} indeksillä {indeksi}.")
    except IndexError:
        print(f"Tuli IndexError, indeksi {indeksi}.")

def zError():
    jakaja = int(input("Anna jakaja: "))
    try:
        jako = 4 / jakaja
        print(f"4/{jakaja} on {jako:.2f}.")
    except ZeroDivisionError:
        print(f"Tuli ZeroDivisionError, jakaja {jakaja}.")

def tError():
    try:
        tyyppi = input("Anna numero: ")
        kerroin = tyyppi * tyyppi
    except TypeError:
        print(f"Tuli TypeError, {tyyppi}*{tyyppi} merkkijonoilla ei onnistunut.")

def valikko():
    while True:
        print("Mitä haluat tehdä:")
        print("1) Testaa ValueError")
        print("2) Testaa IndexError")
        print("3) Testaa ZeroDivisionError")
        print("4) Testaa TypeError")
        print("0) Lopeta")

        while True:
            try:
                valinta = int(input("Valintasi: "))
                break
            except ValueError:
                print(f"Anna valinta kokonaislukuna.")

        if valinta == 0:
            print("Kiitos ohjelman käytöstä.")
            break
        elif valinta == 1:
                print("Valikko-ohjelma testaa ValueError'n.")
        elif valinta == 2:
            iError()
        elif valinta == 3:
            zError()
        elif valinta == 4:
            tError()
        else:
            print(f"Valintaa ei tunnistettu, yritä uudestaan.")

def main():
    valikko()

if __name__ == "__main__":
    main()