__version__ = "1.0"

class Tuote:
    def __init__(self, tunniste, maara, hinta):
        self.tunniste = tunniste
        self.maara = maara
        self.hinta = hinta
        

def lue_tiedosto(luettava, luetuttiedot):
    with open(luettava, encoding="utf-8") as tiedosto:
        rivit = 0
        for rivi in tiedosto:
            rivi = rivi.strip()
            luetuttiedot.append(rivi)
            rivit += 1
        print(f"Tiedosto '{luettava}' luettu, {rivit} riviä.")
    print()

def analysoi_tiedot(luetuttiedot, analysoidut):
    for i in luetuttiedot:
        osat = i.split(";")
        tuote = Tuote(osat[0], int(osat[1]), float(osat[2]))
        analysoidut.append(tuote)

    varaston_arvo = float(0)

    for i in analysoidut:
        varaston_arvo += float(i.maara * i.hinta)

    print(f"Tiedot analysoitu, varaston arvo on {varaston_arvo:.2f} EUR.")
    print()

def tallenna_tulokset(kirjoitettava, analysoidut):
    with open(kirjoitettava, "w", encoding="utf-8") as tiedosto:
        for i in analysoidut:
            tiedosto.write(f"{(i.maara * i.hinta):.2f}\n")
    
    print(f"Tulokset tallennettu tiedostoon '{kirjoitettava}'.")
    print()