def yerine_koy(sifre, sifreleme_sirasi):
    sifrelenmis_metin = ""

    for karakter in sifre:
        if karakter in alfabe:
            karakter_index = alfabe.index(karakter)
            sifrelenmis_metin += sifreleme_sirasi[karakter_index]

    return sifrelenmis_metin

alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"  
sifreleme_sirasi = input("Kullanmak istediğiniz sırayı girin (Alfabenin harflerini karışık bir şekilde yazın): ")
metin = input("Şifrelemek istediğiniz metni girin. Metin bir kelimeden fazla ise lütfen arasında boşluk bırakmadan yazınız: ")

sifrelenmis_metin = yerine_koy(metin, sifreleme_sirasi)
print("Şifrelenmiş Metin:", sifrelenmis_metin)
