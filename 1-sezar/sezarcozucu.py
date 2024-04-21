def sezar_desifrele(sifreli_mesaj, anahtar):
    alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
    cozulmus_mesaj  = ""
    for harf in sifreli_mesaj:
        
        if harf in alfabe:
           
            indeks = alfabe.index(harf)
            yeni_indeks = (indeks - anahtar) % len(alfabe)
         
            cozulmus_mesaj += alfabe[yeni_indeks]
        else:
            
            cozulmus_mesaj += harf
    return cozulmus_mesaj


anahtar = 3
sifreli_mesaj = input("Lütfen çözülecek şifreli mesajı girin: ")

cozulmus_mesaj = sezar_desifrele(sifreli_mesaj, anahtar)
print("Çözülmüş Mesaj:", cozulmus_mesaj)
