pituus = int(input("Anna pituus (cm): "))
paino = int(input("Anna paino (kg): "))
bmi = paino / (pituus / 100) ** 2
kuvaus = ""

if bmi <= 17:
    kuvaus = "Vaarallinen aliravitsemus"
elif 17 < bmi < 18.5:
    kuvaus = "Liiallinen laihuus"
elif 18.5 <= bmi < 25:
    kuvaus = "Normaali paino"
elif 25 <= bmi < 30:
    kuvaus = "Ylipaino eli lievä lihavuus"
elif 30 <= bmi < 35:
    kuvaus = "Merkittävä lihavuus"
elif 35 <= bmi < 40:
    kuvaus = "Vaikea lihavuus"
else:
    kuvaus = "Sairaalloinen lihavuus"

print(f"Painoindeksi on {bmi:.1f} ({kuvaus})")

tavoite = float(input("Anna tavoiteindeksi: "))
tavoitepaino = tavoite * (pituus / 100) ** 2
ero = abs(tavoitepaino - paino)

if bmi > tavoite:
    print(f"Tavoiteindeksi vastaa {ero:.1f} kg alhaisempaa painoa.")
elif bmi < tavoite:
    print(f"Tavoiteindeksi vastaa {ero:.1f} kg suurempaa painoa.")
print("Kiitos ohjelman käytöstä.")