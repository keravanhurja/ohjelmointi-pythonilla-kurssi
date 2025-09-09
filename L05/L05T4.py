maksimi = 15
minimi = 5

def merkkijono():
    mj = input("Anna merkkijono, 5-15 merkkiä: ")
    return mj
    
def laske_p(mj):
    pituus = 0
    for _ in mj:
        pituus += 1
    return pituus

def tarkista():
    while True:
        mj = merkkijono()
        p = laske_p(mj)

        if p < minimi:
            print(f"Liian lyhyt, {p} merkkiä, anna uusi.")
        elif p > maksimi:
            print(f"Liian pitkä, {p} merkkiä, anna uusi.")
        else:
            print(f"Annoit sopivan merkkijonon, {p} merkkiä.")
            print("Kiitos ohjelman käytöstä.")
            return mj

def main():
    tulos = tarkista()
    return tulos

if __name__ == "__main__":
    main()