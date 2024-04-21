def kaydirmali_sifre_coz(sifreli_mesaj, anahtar):
    alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
    cozulmus_mesaj = ""
    for harf in sifreli_mesaj:
        if harf in alfabe:
            indeks = alfabe.index(harf)
            yeni_indeks = (indeks - anahtar) % len(alfabe)
            cozulmus_mesaj += alfabe[yeni_indeks]
        else:
            cozulmus_mesaj += harf
    return cozulmus_mesaj

# Şifreli mesajı ve anahtar değerini kullanıcıdan aldık.
sifreli_mesaj = input("Lütfen çözülecek şifreli mesajı girin: ")
anahtar = int(input("Lütfen şifreleme anahtarını girin: "))

cozulmus_mesaj = kaydirmali_sifre_coz(sifreli_mesaj, anahtar)
print("Çözülmüş Mesaj:", cozulmus_mesaj)
