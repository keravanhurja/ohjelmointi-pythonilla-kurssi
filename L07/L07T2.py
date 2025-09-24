class Auto:
    def __init__(self, merkki, lukumaara):
        self.merkki = merkki
        self.lukumaara = lukumaara

def kysy_auto():
    merkki = input("Anna automerkki: ")
    lukumaara = int(input("Anna automerkin lukumäärä varastossa: "))
    return Auto(merkki, lukumaara)

def tulosta_auto(auto):
    print(f"Varastossa on nyt {auto.merkki}-merkkisiä autoja {auto.lukumaara} kpl.")

def main():
    auto = kysy_auto()
    tulosta_auto(auto)
    print("Kiitos ohjelman käytöstä.")

if __name__ == "__main__":
    main()