def kaydirmali_sifrele(mesaj, anahtar):
    alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
    sifreli_mesaj = ""
    for harf in mesaj:
        
        if harf in alfabe:
            
            indeks = alfabe.index(harf)
            yeni_indeks = (indeks + anahtar) % len(alfabe)
            
            sifreli_mesaj += alfabe[yeni_indeks]
        else:
           
            sifreli_mesaj += harf
    return sifreli_mesaj


anahtar = int(input("Lütfen şifreleme için bir anahtar değeri girin : "))
mesaj = input("Lütfen şifrelenecek mesajı girin, mesaj bir kelimeden fazla ise lütfen arasında boşluk bırakmadan yazınız: ")

sifreli_mesaj = kaydirmali_sifrele(mesaj, anahtar)
print("Şifrelenmiş Mesaj:", sifreli_mesaj)


