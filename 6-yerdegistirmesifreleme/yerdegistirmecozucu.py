import math

def yer_değiştirme_coz(şifreli_metin, anahtar):
    sütunlar = anahtar
    satırlar = math.ceil(len(şifreli_metin) / sütunlar)
    matris = []
    indeks = 0

    for _ in range(sütunlar):
        sütun = []
        for _ in range(satırlar):
            if indeks < len(şifreli_metin):
                sütun.append(şifreli_metin[indeks])
                indeks += 1
            else:
                break
        matris.append(sütun)
    
    
    orijinal_metin = ''
    for i in range(satırlar):
        for j in range(sütunlar):
            orijinal_metin += matris[j][i]
    
    return orijinal_metin


şifreli_metin = input("Çözülecek şifreli metni girin: ")
anahtar = int(input("Anahtarı yani Sütun sayısını girin: "))


çözülen_metin = yer_değiştirme_coz(şifreli_metin, anahtar)


print("Çözülen Metin:", çözülen_metin)
