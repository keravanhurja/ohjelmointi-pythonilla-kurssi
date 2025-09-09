
def vaihe1():
    print("Ensimmäinen vaihe:")
    print("Nyt olemme tulosta-aliohjelmassa")
    print("Tämä aliohjelma tulostaa vain tekstiä.")
    print("Tämä sopii hyvin valikon tulostamiseen.")

def vaihe2(luku):
    print(f"Aliohjelmassa parametrin arvo on {luku}")
    luku = luku ** 2
    print(f"Aliohjelmassa parametrin arvo on neliöön korottamisen jälkeen {luku}")

def vaihe3(etunimi, sukunimi):
    return etunimi+" "+sukunimi

def paaohjelma():
    vaihe1()
    luku = int(input("\nToinen vaihe:\nAnna luku: "))
    print(f"Päätasolla ennen aliohjelmaa luku on {luku}")
    vaihe2(luku)
    print(f"Päätasolla aliohjelman jälkeen luku on {luku}")

    print("\nKolmas vaihe:")
    etunimi = input("Anna etunimi: ")
    sukunimi = input("Anna sukunimi: ")
    kokonimi = vaihe3(etunimi, sukunimi)
    print(f"Etunimi '{etunimi}' ja sukunimi '{sukunimi}' muodostavat nimen '{kokonimi}'.")
    print("Kiitos ohjelman käytöstä.")

paaohjelma()