sana1 = input("Anna sana 1: ")
sana2 = input("Anna sana 2: ")

if sana1 == sana2:
    print("Sanat ovat samoja.")
elif sana1 < sana2:
    print(f"'{sana1}' on aakkosissa aiemmin kuin '{sana2}'.")
else:
    print(f"'{sana2}' on aakkosissa aiemmin kuin '{sana1}'.")


if "z" in sana1 and "z" in sana2:
    print(f"Kirjain 'z' löytyy sanasta 1.")
    print(f"Kirjain 'z' löytyy sanasta 2.")
elif "z" in sana1:
    print(f"Kirjain 'z' löytyy sanasta 1.")
elif "z" in sana2:
    print(f"Kirjain 'z' löytyy sanasta 2.")
else:
    print("Kummastakaan sanasta ei löytynyt kirjainta 'z'.")

sana3 = input("Anna testattava sana: ")

if sana3 == sana3[::-1]:
    print(f"Antamasi sana '{sana3}' on palindromi.")
else:
    print(f"Antamasi sana ei ole palindromi.")
    print(f"Se on väärinpäin '{sana3[::-1]}' ja oikein päin '{sana3}'.")
print("Kiitos ohjelman käytöstä.")