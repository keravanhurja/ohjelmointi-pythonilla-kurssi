ala = int(input("Anna alueen alaraja: "))
yla = int(input("Anna alueen yläraja: "))

for luku in range(ala, yla + 1):
    if luku % 5 == 0 and luku % 7 == 0:
        print(f'Luku {luku} on jaollinen 5:llä ja 7:llä.')
        print("Lopetetaan etsintä.")
        break
    elif luku % 5 != 0:
        print(f'{luku} ei ole jaollinen viidellä, hylätään.')
    elif luku % 7 != 0:
        print(f'{luku} ei ole jaollinen seitsemällä, hylätään.')
else:
    print("Alueelta ei löytynyt sopivaa arvoa.")
    
print("Kiitos ohjelman käytöstä.")