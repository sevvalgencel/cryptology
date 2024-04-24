alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"

def vigenere_sifreleme(şifre_metni, anahtar):
    sifrelenmis_metin = ""  
    anahtar_indisi = 0  
    for karakter in şifre_metni:
        # Karakterin Türkçe alfabede bulunup bulunmadığını kontrol ediyoruz.
        if karakter in alfabe:
            
            karakter_indisi = alfabe.index(karakter)
            
            anahtar_karakter_indisi = alfabe.index(anahtar[anahtar_indisi])
            
            sifrelenmis_indis = (karakter_indisi + anahtar_karakter_indisi) % len(alfabe)
           
            sifrelenmis_metin += alfabe[sifrelenmis_indis]
            # Anahtar kelimesinin sonraki karakterine geçiyoruz.
            anahtar_indisi = (anahtar_indisi + 1) % len(anahtar)
        else:
            # Eğer karakter alfabede bulunmuyorsa, aynı şekilde eklenir(dolgu karakteri gibi)
            sifrelenmis_metin += karakter
    return sifrelenmis_metin


sifre_metni = input("Şifrelenecek metni girin: ").lower().replace(" ", "")  
anahtar = input("Anahtar kelimeyi girin: ").lower()  


sifrelenmis_metin = vigenere_sifreleme(sifre_metni, anahtar)


print("Şifrelenmiş Metin:")
print(sifrelenmis_metin)
