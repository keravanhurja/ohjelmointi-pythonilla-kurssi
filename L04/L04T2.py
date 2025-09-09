summa = 0
arvosanat = 0

while True:
    arvosana = int(input("Anna kurssiarvosana väliltä 1-5 (-1 lopettaa): "))

    if arvosana == -1:
        ka = float(summa / arvosanat)
        print(f"Arvosanojen keskiarvo on {round(ka, 2)}.")
        break
    elif 1 <=arvosana <= 5:
        summa += arvosana
        arvosanat += 1
    else:
        print("Väärä syöte. Vain arvosanat 1-5 kelpaavat (-1 lopettaa).")
        
print("Kiitos ohjelman käytöstä.")
