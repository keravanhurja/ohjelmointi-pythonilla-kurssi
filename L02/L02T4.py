pii = 3.14
posKokonaisluku = int(input("Anna positiivinen kokonaisluku: "))
print(f'Luku {posKokonaisluku} kerrottuna itsellään on {posKokonaisluku*posKokonaisluku}')
sade = int(input("Anna ympyrän säteen pituus kokonaislukuna: "))
print(f'Ympyrän säde on {sade}, kehä on {2*pii*sade} ja pinta-ala on {pii*(sade**2)}.')
sivu1 = int(input("Anna suorakulmion yhden sivun pituus kokonaislukuna: "))
sivu2 = int(input("Anna suorakulmion toisen sivun pituus kokonaislukuna: "))
print(f'Suorakulmion sivut ovat {sivu1} ja {sivu2}; kehä on {2*sivu1+2*sivu2}; ja pinta-ala on {sivu1*sivu2}.')
print("Kiitos ohjelman käytöstä.")