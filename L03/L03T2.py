while True:
    x = input("Haluatko lopettaa ohjelman suorittamisen (k/K): ")

    if x.lower() == 'k':
        print("Kiitos ohjelman käytöstä.")
        break
    else:
        nimi = input("Anna nimi: ")
        salasana = input("Anna salasana: ")
        
        if nimi != "Matti" or salasana != "salasana":
            print("Antamasi nimi oli 5 merkkiä pitkä, mutta se tai salasana ei ollut oikein.")
            break
        else:
            print("Käyttäjä tunnistettu.")
            break
