merkkijono = input("Anna merkkijono: ")

print(f'\nMerkkijonon pituus: {len(merkkijono)}')

print(f'\nViisi ensimmäistä merkkiä: {merkkijono[:5]}')
print(f'Viisi viimeistä merkkiä: {merkkijono[-5:]}')
print(f'Merkit 2,3,4 ja 5: {merkkijono[1:5]}')

print(f'\nMerkkijonon joka toinen merkki: {merkkijono[::2]}')

print(f'\nMerkkijono takaperin: {merkkijono[::-1]}')

aloituspaikka = int(input("\nAnna aloituspaikka: "))
lopetuspaikka = int(input("Anna lopetuspaikka: "))
siirtyma = int(input("Anna siirtymä: "))
print(f'Antamillasi asetuksilla merkkijono {merkkijono} tulostuu näin: {merkkijono[aloituspaikka:lopetuspaikka:siirtyma]}')

print("\nKiitos ohjelman käytöstä.")