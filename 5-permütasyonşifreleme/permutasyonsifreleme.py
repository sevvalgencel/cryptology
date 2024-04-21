import math
import random

def permütasyon_anahtarı(n):
    perm_anahtar = list(range(1, n + 1))
    return ''.join(str(x) for x in perm_anahtar)

def metin_bloklama(metin, blok_boyutu):
    blok = []
    for i in range(0, len(metin), blok_boyutu):
        blok.append(metin[i:i+blok_boyutu])  # Metni belirlenen blok boyutunda bölmek için slicing işlemini yapıyoruz
    return blok

def şifreleme(metin, anahtar):
    blok_boyutu = len(anahtar)
    text_blocks = metin_bloklama(metin, blok_boyutu)

    şifrelenmiş_metin = ""

    for blok in text_blocks:
        if len(blok) < blok_boyutu:
            blok += 'a' * (blok_boyutu - len(blok))

        şifrelenmiş_blok = ""
        for i in range(blok_boyutu):
            şifrelenmiş_blok += blok[int(anahtar[i]) - 1]
 
        şifrelenmiş_metin += şifrelenmiş_blok 

    return şifrelenmiş_metin

metin = input("Lütfen şifrelemek istediğiniz metni girin: ")
metin = metin.replace(" ", "")

# Anahtarın geçerli bir değer olup olmadığını kontrol etmek için döngü kullanarak kullanıcıdan istiyoruz
while True:
    anahtar_sayısı = input("Lütfen anahtar sayısını giriniz: ")
    if anahtar_sayısı.isdigit() and int(anahtar_sayısı) > 0:
        anahtar_sayısı = int(anahtar_sayısı)
        break
    else:
        print("Hatalı giriş! Anahtar sayısı bir pozitif tamsayı olmalıdır.")

permütasyon_anahtar = input(f"Lütfen permütasyon anahtarını girin (1'den {anahtar_sayısı} uzunluğuna kadar rakamları içermeli ve rakamların tekrarı olmamalıdır): ")
if sorted(permütasyon_anahtar) != [str(i) for i in range(1, anahtar_sayısı + 1)]:
    print(f"Hatalı giriş! Permütasyon anahtarı 1'den {anahtar_sayısı} uzunluğuna kadar rakamları içermeli ve rakamların tekrarı olmamalıdır.".format(anahtar_sayısı))
    exit()

şifrelenmiş_metin = şifreleme(metin, permütasyon_anahtar)
print("Şifrelenmiş metin:", şifrelenmiş_metin)
