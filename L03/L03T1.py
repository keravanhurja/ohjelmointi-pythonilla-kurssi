kokonaisluku = int(input("Anna kokonaisluku: "))
if kokonaisluku < 10:
    print("Luku on pienempi kuin 10.")
else:
    print("Luku on suurempi tai yhtä suuri kuin 10.")
if kokonaisluku % 2 == 0:
    print("Antamasi luku on parillinen.")
else:
    print("Antamasi luku on pariton.")
print("Kiitos ohjelman käytöstä.")