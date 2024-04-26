import numpy as np

alfabe = 'abcçdefgğhıijklmnoöprsştuüvyz'

def matrisi_olustur():
    print("Lütfen 9 sayıyı aralarında boşluk bırakarak girin (3x3'lük bir matris oluşturmak için):")
    giris = input()
    
    sayilar = giris.split()
    if len(sayilar) != 9:
        print("9 sayı girmelisiniz.")
        return matrisi_olustur()  
    
    sayilar = [int(sayi) for sayi in sayilar]
   
    matris = np.array([sayilar[:3], sayilar[3:6], sayilar[6:]])
    return matris

def metni_sifrele(metin, anahtar_matrisi):
    sifreli_metin = ""
    
    for i in range(0, len(metin), 3):
        blok = metin[i:i+3]
        sayi_blok = [alfabe.index(harf) for harf in blok]
        sifreli_blok = np.dot(anahtar_matrisi, sayi_blok) % 29  
        sifreli_metin += ''.join([alfabe[sayi] for sayi in sifreli_blok])
    return sifreli_metin

def main():
  
    metin = input("Lütfen şifrelenecek metni girin (sadece Türk alfabesini kullanarak): ").lower()

    anahtar_matrisi = None
    for _ in range(3):  
        anahtar_matrisi = matrisi_olustur()
        if anahtar_matrisi is not None:  
            break

    # Matris uygun bir şekilde oluşturulamazsa programı sonlandır
    if anahtar_matrisi is None:
        print("Uygun bir matris oluşturulamadı. Program sonlandırılıyor.")
        return

    print("Oluşturulan matris:")
    print(anahtar_matrisi)  

    sifreli_metin = metni_sifrele(metin, anahtar_matrisi)

    print("Şifreli Metin:", sifreli_metin)

if __name__ == "__main__":
    main()
