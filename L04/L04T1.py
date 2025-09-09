aloitus = int(input("Anna aloitusarvo: "))
loppu = int(input("Anna lopetusarvo: "))
print("Toteutus for-lauseella:")
for i in range(aloitus, loppu + 1):
    print(i, end=" ")

print("\n\nToteutus while-lauseella:")
while aloitus <= loppu:
    print(aloitus, end=" ")
    aloitus += 1

print("\n\nKiitos ohjelman käytöstä.")