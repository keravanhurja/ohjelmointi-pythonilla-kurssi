import datetime

def viikonpaivat():
    paiva = datetime.date(2023, 1, 2)  # Tämä on maanantai
    for _ in range(7):
        print(paiva.strftime("%A"))
        paiva += datetime.timedelta(days=1)

def erotus():
    syntymapv = input("Anna syntymäpäiväsi muodossa pp.kk.vvvv: ")
    osat = syntymapv.split(".")
    paivat = osat[0]
    kuukaudet = osat[1]
    vuodet = osat[2]

    syntyma = datetime.date(int(vuodet), int(kuukaudet), int(paivat))
    vertailupaiva = datetime.date(2000, 1, 1)
    erotus = vertailupaiva - syntyma
    return erotus

def tunnista():
    # Käyttäjältä kysytään päivämäärä ja kellonaika
    aika = input("Anna päivämäärä ja kello muodossa 'pp.kk.vvvv hh:mm': ")
    osat = aika.split(" ")
    paivamaara = osat[0].split(".")
    kellonaika = osat[1].split(":")

    # Poistetaan mahdolliset etunollat
    if kellonaika[0].startswith("0"):
        kellonaika[0] = kellonaika[0][1:]
    if kellonaika[1].startswith("0"):
        kellonaika[1] = kellonaika[1][1:]

    # Tulostetaan osat
    print(f"Annoit vuoden {paivamaara[2]}")
    print(f"Annoit kuukauden {paivamaara[1]}")
    print(f"Annoit päivän {paivamaara[0]}")
    print(f"Annoit tunnin {kellonaika[0]}")
    print(f"Annoit minuutin {kellonaika[1]}")

def main():
    print("Tämä ohjelma käyttää datetime-kirjastoa tehtävien ratkaisemiseen.")

    while True:
        print("Mitä haluat tehdä:")
        print("1) Tunnistaa aika-olion komponentit")
        print("2) Laskea iän päivinä")
        print("3) Tulostaa viikonpäivät")
        print("4) Tulostaa kuukaudet")
        print("0) Lopeta")

        valinta = input("Valintasi: ")

        if valinta == "1":
            tunnista()
            print()

        elif valinta == "2":
            print(f"1.1.2000 sinä olit {erotus().days} päivää vanha.")
            print()

        elif valinta == "3":
            viikonpaivat()
            print()

        elif valinta == "4":
            for kuukausi in range(1, 13):
                print(datetime.date(2023, kuukausi, 1).strftime("%b"))
            print()
                
        elif valinta == "0":
            break

    print("Kiitos ohjelman käytöstä.")

if __name__ == "__main__":
    main()