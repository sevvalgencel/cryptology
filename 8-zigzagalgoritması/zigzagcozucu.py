def zigzag_coz(sifreli_metin, anahtar):
    sıralar = ['' for _ in range(anahtar)]
    ind = 0
    artis = 1
    sirali_ind = 0

    for i in range(len(sifreli_metin)):
        sıralar[ind] += '-'
        if ind == 0:
            artis = 1
        elif ind == anahtar - 1:
            artis = -1
        ind += artis

    for i in range(anahtar):
        for j in range(len(sıralar[i])):
            if sıralar[i][j] == '-' and sirali_ind < len(sifreli_metin):
                sıralar[i] = sıralar[i][:j] + sifreli_metin[sirali_ind] + sıralar[i][j+1:]
                sirali_ind += 1

    cozulmus_metin = ''
    ind = 0
    artis = 1
    for _ in range(len(sifreli_metin)):
        cozulmus_metin += sıralar[ind][0]
        sıralar[ind] = sıralar[ind][1:]
        if ind == 0:
            artis = 1
        elif ind == anahtar - 1:
            artis = -1
        ind += artis

    return cozulmus_metin

sifreli_metin = input("Çözülecek metni girin: ")
anahtar = int(input("Anahtar sayısını girin: "))

cozulmus_metin = zigzag_coz(sifreli_metin, anahtar)
print("Çözülmüş metin:", cozulmus_metin)
