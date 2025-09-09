def laskuri(luku, teksti):
    while luku > 0:
        print(teksti)
        luku -= 1

teksti = input("Anna teksti: ")

while True:
    if teksti == "lopeta":
        print("Lopetetaan.")
        break
    luku = int(input("Anna luku: "))
    laskuri(luku, teksti)
    teksti = input("\nAnna teksti: ")

print("Kiitos ohjelman käytöstä.")