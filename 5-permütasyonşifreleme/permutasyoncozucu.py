def çözümleme(şifrelenmiş_metin, anahtar):
    blok_boyutu = len(anahtar)
    text_blocks = [şifrelenmiş_metin[i:i+blok_boyutu] for i in range(0, len(şifrelenmiş_metin), blok_boyutu)]
   

    orijinal_metin = ""

    for blok in text_blocks:
        orijinal_blok = [''] * blok_boyutu
        for i, char in enumerate(blok):
            orijinal_blok[anahtar[i] - 1] = char
    #Bloktaki her bir karakteri (yani charı) ve bu karakterin indeksini (i) almak için bir enumerate() fonksiyonu kullanırız.
        orijinal_metin += ''.join(orijinal_blok)

    return orijinal_metin

şifrelenmiş_metin = input("Lütfen çözümlemek istediğiniz şifrelenmiş metni girin: ")
anahtar_sayısı = int(input("Lütfen anahtar sayısını giriniz: "))

permütasyon_anahtar = input(f"Lütfen permütasyon anahtarını girin (1'den {anahtar_sayısı} uzunluğuna kadar rakamları içermeli ve rakamların tekrarı olmamalıdır): ")

if sorted(permütasyon_anahtar) != [str(i) for i in range(1, anahtar_sayısı + 1)]:
    print(f"Hatalı giriş! Permütasyon anahtarı 1'den {anahtar_sayısı} uzunluğuna kadar rakamları içermeli ve rakamların tekrarı olmamalıdır.")
    exit()

çözülmüş_metin = çözümleme(şifrelenmiş_metin, [int(x) for x in permütasyon_anahtar])
print("Çözümlenmiş metin:", çözülmüş_metin)
