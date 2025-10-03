import numpy as np

def arvot(matriisi):
    for rivi in range(matriisi.shape[0]):
        for sarake in range(matriisi.shape[1]):
            matriisi[rivi, sarake] = (rivi + 1) * (sarake + 1)
    print("Matriisi tulostettuna numpy-muotoilulla:")
    print(matriisi)
    print()

    print("Matriisi tulostettuna alkiot puolipisteillä eroteltuna:")
    for rivi in matriisi:
        print(";".join(str(luku) for luku in rivi)+";")
    
def main():
    print("Tämä ohjelma esittelee numpy-matriisin käyttöä.")
    
    matriisi = np.zeros((4, 4), dtype=int)
    arvot(matriisi)

    print("\nKiitos ohjelman käytöstä.")

if __name__ == "__main__":
    main()