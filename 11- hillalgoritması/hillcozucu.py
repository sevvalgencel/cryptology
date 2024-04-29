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


def hill_cozucu(sifre, Kinv):
    cozulmus_sifre = ""
    sifre_numaraları = []

    for harf in sifre:
        sifre_numaraları.append( harften_indexe[harf])

    blok = [
        sifre_numaraları[i : i + int(Kinv.shape[0])]
        for i in range(0, len(sifre_numaraları), int(Kinv.shape[0]))
    ]

    for C in blok:
        C = np.transpose(np.asarray(C))[:, np.newaxis]
        numaralar = np.dot(Kinv, C) % len(alfabe)
        n = numaralar.shape[0]

        for idx in range(n):
            numara = int(numaralar[idx, 0])
            cozulmus_sifre += indexten_harfe[numara]

    return cozulmus_sifre


def main():
    sifre = input("Çözülecek şifreli metni girin: ").lower()
    # Matris girişini al
    print("3x3 matrisin elemanlarını girin:")
    K = []
    for i in range(3):
        row = []
        for j in range(3):
            elem = int(input(f"Matrisin {i+1}.{j+1}. elemanını girin: "))
            row.append(elem)
        K.append(row)
    K = np.array(K)

    # Matrisin tersini al
    K_ters = matrix_mod_tersi(K, len(alfabe))

    cozulmus_mesaj = hill_cozucu(sifre, K_ters)

    print("Şifreli mesaj: " + sifre)
    print("Orijinal mesaj: " + cozulmus_mesaj)


main()
