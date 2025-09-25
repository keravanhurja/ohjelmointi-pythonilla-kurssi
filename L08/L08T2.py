import L08T2Kirjasto

def main():
    print(f"Käytetään lämpötilamuunnoskirjaston versiota {L08T2Kirjasto.__version__}")

    while True:
        print("Minkä lämpötilamuunnoksen haluat tehdä?")
        print("1) Celsius->Fahrenheit")
        print("2) Celsius->Kelvin")
        print("3) Fahrenheit->Kelvin")
        print("4) Fahrenheit->Celsius")
        print("5) Kelvin->Celsius")
        print("6) Kelvin->Fahrenheit")
        print("0) Lopeta")
        valinta = input("Valintasi: ")

        if valinta == "1":
            c = float(input("Anna lähtölämpötila: "))
            f = L08T2Kirjasto.celsius_to_fahrenheit(c)
            print(f"Lämpötila Fahrenheit asteina: {round(f, 2)}\n")

        elif valinta == "2":
            c = float(input("Anna lähtölämpötila: "))
            k = L08T2Kirjasto.celsius_to_kelvin(c)
            print(f"Lämpötila Kelvin asteina: {round(k, 2)}\n")

        elif valinta == "3":
            f = float(input("Anna lähtölämpötila: "))
            k = L08T2Kirjasto.fahrenheit_to_kelvin(f)
            print(f"Lämpötila Kelvin asteina: {round(k, 2)}\n")

        elif valinta == "4":
            f = float(input("Anna lähtölämpötila: "))
            c = L08T2Kirjasto.fahrenheit_to_celsius(f)
            print(f"Lämpötila Celsius asteina: {round(c, 2)}\n")

        elif valinta == "5":
            k = float(input("Anna lähtölämpötila: "))
            c = L08T2Kirjasto.kelvin_to_celsius(k)
            print(f"Lämpötila Celsius asteina: {round(c, 2)}\n")

        elif valinta == "6":
            k = float(input("Anna lähtölämpötila: "))
            f = L08T2Kirjasto.kelvin_to_fahrenheit(k)
            print(f"Lämpötila Fahrenheit asteina: {round(f, 2)}\n")

        elif valinta == "0":
            break

        else:
            print("Valintaa ei tunnistettu, yritä uudestaan.\n")

    print("Kiitos ohjelman käytöstä.")

if __name__ == "__main__":
    main()
    