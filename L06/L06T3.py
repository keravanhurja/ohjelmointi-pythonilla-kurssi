def read_and_write(luettava_tiedosto):
    open("L06T3T1.txt", "w").close()
    with open(luettava_tiedosto, "r", encoding="utf-8") as file:
        for rivi in file:
            rivi = rivi.strip()
            if rivi == rivi[::-1] and rivi != "":
                print(f"Rivi '{rivi}' on palindromi.")
                with open("L06T3T1.txt", "a", encoding="utf-8") as pal_file:
                    pal_file.write(rivi + "\n")
            elif rivi.strip().isdigit():
                print(f"Rivi '{rivi}' on numerorivi.")
            else:
                print(f"Rivi '{rivi}' ei ole palindromi.")
def main():
    luettava_tiedosto = input("Anna luettavan tiedoston nimi: ")
    read_and_write(luettava_tiedosto)
    print("Kiitos ohjelman käytöstä.")

if __name__ == "__main__":
    main()