import math
import random

def menu():
    
    print("Mitä haluat tehdä:")
    print("1) Laskea ympyrän pinta-alan")
    print("2) Arvata luvun")
    print("0) Lopeta")
    valinta = input("Valintasi: ")
    return valinta

def main():
    random.seed(1)

    print("Tämä ohjelma käyttää kirjastoja tehtävien ratkaisemiseen.")
    while True:
        valinta = menu()

        if valinta == "1":
            r = int(input("Anna ympyrän säde kokonaislukuna: "))
            A = math.pi * r**2
            print(f"Säteellä {r} ympyrän pinta-ala on {A:.2f}.\n")

        elif valinta == "2":
            arvaus = 0
            arvaukset = 1
            luku = random.randint(0, 1000)
            
            print("Arvaa ohjelman arpoma kokonaisluku.")

            while True:
                arvaus = int(input("Anna kokonaisluku välillä 0-1000: "))

                if arvaus == luku:
                    print(f"Oikein! Käytit arvaamiseen {arvaukset} kierrosta.\n")
                    break

                elif arvaus < luku:
                    print("Haettu luku on suurempi.")
                    arvaukset += 1
                
                elif arvaus > luku:
                    print("Haettu luku on pienempi.")
                    arvaukset += 1

        elif valinta == "0":
            break

    print("Kiitos ohjelman käytöstä.")

if __name__ == "__main__":
    main()