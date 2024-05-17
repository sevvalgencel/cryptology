import numpy as np


alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"


harf_to_index = {harf: idx for idx, harf in enumerate(alfabe)}
index_to_harf = {idx: harf for idx, harf in enumerate(alfabe)}

# Kullanıcıdan matris girişi alma
def matris_girisi():
    boyut = int(input("Matris boyutunu girin (örneğin, 2x2 için 2 girin): "))
    matris = []
    print(f"Lütfen {boyut}x{boyut} matris değerlerini girin (sadece sayılar):")
    for i in range(boyut):
        satir = list(map(int, input(f"{i+1}. satırı girin: ").split()))
        matris.append(satir)
    return np.array(matris)

# Metni şifrelemek için Hill algoritması
def hill_sifreleme(metin, matris):
    boyut = matris.shape[0]
    # Metni uygun uzunlukta bloklara böl
    while len(metin) % boyut != 0:
        metin += 'x'  # Boşluğu 'x' ile dolduruyoruz (veya başka bir harf seçilebilir)
    
    # Metni harf indekslerine çevir
    metin_indices = [harf_to_index[harf] for harf in metin]
    
    # Blokları oluştur ve şifrele
    sifreli_metin = ""
    for i in range(0, len(metin_indices), boyut):
        blok = metin_indices[i:i+boyut]
        blok = np.array(blok)
        sifreli_blok = np.dot(matris, blok) % len(alfabe)
        sifreli_metin += ''.join(index_to_harf[idx] for idx in sifreli_blok)
    
    return sifreli_metin

# Kullanıcıdan metin girişi al
def main():
    metin = input("Şifrelenecek metni girin: ").lower()
    # Boşlukları yok say
    metin = metin.replace(' ', '')
    matris = matris_girisi()
    sifreli_metin = hill_sifreleme(metin, matris)
    print("Şifreli metin:", sifreli_metin)

if __name__ == "__main__":
    main()
