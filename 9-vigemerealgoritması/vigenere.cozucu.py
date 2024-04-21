alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"


def vigenere_cozme(sifrelenmis_metin, anahtar):
    cozulmus_metin = ""  
    anahtar_indisi = 0  
    for karakter in sifrelenmis_metin:
        
        if karakter in alfabe:
            karakter_indisi = alfabe.index(karakter)
          
            anahtar_karakter_indisi = alfabe.index(anahtar[anahtar_indisi])
            
            cozulmus_indis = (karakter_indisi - anahtar_karakter_indisi) % len(alfabe)
            
            cozulmus_metin += alfabe[cozulmus_indis]
            # Anahtar kelimesinin sonraki karakterine geçiyoruz.
            anahtar_indisi = (anahtar_indisi + 1) % len(anahtar)
        else:
            cozulmus_metin += karakter
    return cozulmus_metin


sifrelenmis_metin = input("Çözülecek metni girin: ").lower()  
anahtar = input("Anahtar kelimeyi girin: ").lower()  


cozulmus_metin = vigenere_cozme(sifrelenmis_metin, anahtar)

# Çözülmüş metni ekrana yazdır
print("Çözülmüş Metin:", cozulmus_metin)
