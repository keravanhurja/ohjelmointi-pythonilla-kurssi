def nimet_ja_merkit(tiedostonimi):
    rivit = 0
    merkit = 0
    nimet = 0
    with open(tiedostonimi, encoding="utf-8") as tiedosto:
        for rivi in tiedosto:
            rivit += 1
            # Remove only the trailing newline (\n or \r\n), not spaces
            merkit += len(rivi)
            nimet += len(rivi.strip())
    print(f"Tiedostossa oli {rivit} nimeä ja {merkit} merkkiä.")
    return rivit, merkit, nimet

def ka(rivit, merkit, nimet):
    if rivit > 0:
        nimienkeskiarvo = float(nimet / rivit)
        print(f"Keskimääräinen nimen pituus oli {nimienkeskiarvo:.0f} merkkiä.")
    else:
        print("Tiedosto on tyhjä.")
        
def main():
    tiedostonimi = input("Anna luettavan tiedoston nimi: ")
    rivit, merkit, nimet = nimet_ja_merkit(tiedostonimi)
    ka(rivit, merkit, nimet)
    print("Kiitos ohjelman käytöstä.")

if __name__ == "__main__":
    main()