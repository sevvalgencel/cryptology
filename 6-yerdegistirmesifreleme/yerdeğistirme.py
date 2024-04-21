import math

def yer_degistirme(ana_metin, anahtar):
    sütunlar = anahtar

    satırlar = math.ceil(len(ana_metin) / sütunlar)
    #ceiling fonksiyonu ile satır sayısını hesaplarken yukarı yuvarladık.
    
    matris = []
    indeks = 0
    for _ in range(satırlar):
        satır = []
        for _ in range(sütunlar):
            if indeks < len(ana_metin):
                satır.append(ana_metin[indeks])
                indeks += 1  
            else:
                satır.append('a')  
        matris.append(satır)
    
    
    şifreli_metin = ''
    for j in range(sütunlar):
        for i in range(satırlar):
            şifreli_metin += matris[i][j]
    
    return şifreli_metin


ana_metin = input("Şifrelenecek metni girin: ")
ana_metin = ana_metin.replace(" ", "")
anahtar = int(input("Anahtarı yani Sütun sayısını belirleyin: "))

şifreli_metin = yer_degistirme(ana_metin, anahtar)


print("Şifreli Metin:", şifreli_metin)
