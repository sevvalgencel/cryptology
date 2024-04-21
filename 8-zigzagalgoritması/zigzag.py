def zigzag_sifrele(metin, anahtar):
    sıralar = ['' for _ in range(anahtar)]
    index = 0
    artis = 1

    for karakter in metin:
        sıralar[index] += karakter
        if index == 0:
            artis = 1
        elif index == anahtar - 1:
            artis = -1
        index += artis

    return ''.join(sıralar)

metin = input("Şifrelenecek metni girin: ")
metin = metin.replace(" ", "")
anahtar = int(input("Anahtar sayısını girin: "))

sifreli_metin = zigzag_sifrele(metin, anahtar)
print("Şifreli metin:", sifreli_metin)
