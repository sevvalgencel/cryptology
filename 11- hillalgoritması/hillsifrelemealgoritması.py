import numpy as np
from egcd import egcd  # pip install egcd

alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"

harften_indexe = dict(zip(alfabe, range(len(alfabe))))
indexten_harfe = dict(zip(range(len(alfabe)), alfabe))


def matrix_mod_tersi(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = egcd(det, modulus)[1] % modulus
    matrix_modulus_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )
    return matrix_modulus_inv


def hill_sifreleme(mesaj, K):
    sifrelenmis_metin = ""
    mesaj_numaraları = []

    for harf in mesaj:
        mesaj_numaraları.append(harften_indexe[harf])
    blok = [
        mesaj_numaraları[i : i + int(K.shape[0])]
        for i in range(0, len(mesaj_numaraları), int(K.shape[0]))
    ]

    for P in blok:
        P = np.transpose(np.asarray(P))[:, np.newaxis]

        while P.shape[0] != K.shape[0]:
            P = np.append(P, harften_indexe[" "])[:, np.newaxis]

        numaralar = np.dot(K, P) % len(alfabe)
        n = numaralar.shape[0]

        for idx in range(n):
            number = int(numaralar[idx, 0])
            sifrelenmis_metin += indexten_harfe[number]

    return sifrelenmis_metin



def main():
        mesaj = input("Şifrelenecek metni girin: ").lower()
        # Matris girişini al
        print("3x3 matrisin elemanlarını girin:")
        K = []
        for i in range(3):
            row = []
            for j in range(3):
                elem = int(input(f"Matrisin {i+1}.{j+1}. elemanını giriniz: "))
                row.append(elem)
            K.append(row)
        K = np.array(K)

        # Matrisin tersini al
        K_ters = matrix_mod_tersi(K, len(alfabe))

        şifreli_mesaj = hill_sifreleme(mesaj, K)
        

        print("Orijinal mesaj: " + mesaj)
        print("Şifreli mesaj:  " + şifreli_mesaj)

main()