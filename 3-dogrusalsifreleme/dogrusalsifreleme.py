def dogrusal_sifrele(metin, a, b):
    sifreli_metin = ""
    alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
    metin = metin.lower()  
    for karakter in metin:
            indeks = alfabe.index(karakter)
            kod = (a * indeks + b) % 29
            sifreli_metin += alfabe[kod]

    return sifreli_metin

metin = input("Şifrelenecek metni girin. Metin birkelimeden fazla ise lütfen arasında boşluk bırakmadan yazınız : ")
a = int(input("Lütfen 'a' anahtarını girin: "))
b = int(input("Lütfen 'b' anahtarını girin: "))

sifreli_metin = dogrusal_sifrele(metin, a, b)
print("Şifreli metin:", sifreli_metin)



