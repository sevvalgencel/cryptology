def dogrusal_sifre_coz(sifreli_metin, a, b):
    gercek_metin = ""
    alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
    for karakter in sifreli_metin:
        indeks = alfabe.index(karakter)
        
        gercek_indeks = (pow(a, -1, 29) * (indeks - b)) % 29
        gercek_metin += alfabe[gercek_indeks]
    return gercek_metin

sifreli_metin = input("Çözülecek şifreli metni girin: ")
a = int(input("Lütfen 'a' anahtarını girin: "))
b = int(input("Lütfen 'b' anahtarını girin: "))

cozulmus_metin = dogrusal_sifre_coz(sifreli_metin, a, b)
print("Çözülmüş metin:", cozulmus_metin)
