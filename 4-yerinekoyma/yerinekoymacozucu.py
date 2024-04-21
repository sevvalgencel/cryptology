def yerine_koy_coz(sifre, sifreleme_sirasi):
    alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"  
    cozulmus_metin = ""
    for karakter in sifre:
        if karakter in sifreleme_sirasi:
            karakter_index = sifreleme_sirasi.index(karakter)
            cozulmus_metin += alfabe[karakter_index]
     
    return cozulmus_metin


sifreleme_sirasi = input("Kullanılan şifreleme sırasını girin (Alfabenin harflerini karışık bir şekilde yazın): ")

sifreli_metin = input("Çözülecek şifreli metni girin: ")

cozulmus_metin = yerine_koy_coz(sifreli_metin, sifreleme_sirasi)
print("Çözülmüş Metin:", cozulmus_metin)
