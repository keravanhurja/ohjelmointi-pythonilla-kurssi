

def tulostaOhjeet():
    print("Tämä ohjelma etsii antamistasi luvuista pienimmän.\nOhjelman lopussa se kertoo pienimmän luvun lisäksi antamiesi\nlukujen lukumäärän.")
    print()

def kysyLuku(luvut):
    if len(luvut) == 1:
        luku = int(input("Anna vertailtava positiivinen kokonaisluku (0 lopettaa): "))
        return luku
    elif len(luvut) > 1:
        luku = int(input("Anna uusi positiivinen kokonaisluku (0 lopettaa): "))
        return luku
    else:
        luku = int(input("Anna positiivinen kokonaisluku: "))
        return luku

# Vertaa annettuja lukuja keskenään ja palauttaa pienemmän
def vertaileLukuja(luvut):
    pienempi = min(luvut)
    return pienempi

# Tulostaa lopuksi tarvittavat tiedot
def tulostaTiedot(luvut):
    print(f"\nAnnoit {len(luvut)} lukua.")
    print(f"Annetuista luvuista pienin oli {min(luvut)}.")
    
def main():
    luvut = []

    tulostaOhjeet()

    # Kysytään lukuja, kunnes käyttäjä antaa 0
    while True:
        luku = kysyLuku(luvut)
        if luku == 0:
            break
        luvut.append(luku)
        if len(luvut) > 1:
            vertaileLukuja(luvut)
            pienempi = vertaileLukuja(luvut)
            print(f"Annetuista luvuista pienempi oli {pienempi}.")

    # Varmistetaan, että on annettu ainakin kaksi lukua
    if len(luvut) > 1:
        tulostaTiedot(luvut)

    # Jos annettu vain yksi luku, kerrotaan siitä
    else:
        print(f"Annoit yhden luvun, joka oli {luvut[0]}.")
    print("Kiitos ohjelman käytöstä.")

if __name__ == "__main__":
    main()