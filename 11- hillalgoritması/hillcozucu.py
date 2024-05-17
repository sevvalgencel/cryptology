import numpy as np

# Türk alfabesini tanımla (özel karakterler hariç)
turk_alfabesi = "abcçdefgğhıijklmnoöprsştuüvyz"

# Harfleri ve indekslerini eşleştiren bir sözlük oluştur
harf_to_index = {harf: idx for idx, harf in enumerate(turk_alfabesi)}
index_to_harf = {idx: harf for idx, harf in enumerate(turk_alfabesi)}

# Kullanıcıdan matris girişi al
def matris_girisi():
    boyut = int(input("Matris boyutunu girin (örneğin, 2x2 için 2 girin): "))
    matris = []
    print(f"Lütfen {boyut}x{boyut} matris değerlerini girin (sadece sayılar):")
    for i in range(boyut):
        satir = list(map(int, input(f"{i+1}. satırı girin: ").split()))
        matris.append(satir)
    return np.array(matris)

# Modüler ters hesaplama
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Matrisin modüler tersini hesapla
def matris_mod_tersi(matris, mod):
    det = int(np.round(np.linalg.det(matris)))
    det_mod = det % mod
    det_inv = mod_inverse(det_mod, mod)
    
    if det_inv is None:
        raise ValueError("Matrisin determinantının mod 29'a göre tersi yoktur. Lütfen geçerli bir matris girin.")
    
    matris_tersi = np.linalg.inv(matris) * det
    matris_adj = np.round(matris_tersi).astype(int) % mod
    matris_mod_tersi = (det_inv * matris_adj) % mod
    
    return matris_mod_tersi

# Metni çözmek için Hill algoritması
def hill_cozme(sifreli_metin, matris):
    boyut = matris.shape[0]
    
    # Şifreli metni harf indekslerine çevir
    sifreli_indices = [harf_to_index[harf] for harf in sifreli_metin]
    
    # Matrisin modüler tersini al
    matris_mod_ters = matris_mod_tersi(matris, len(turk_alfabesi))
    
    # Blokları oluştur ve çöz
    cozulmus_metin = ""
    for i in range(0, len(sifreli_indices), boyut):
        blok = sifreli_indices[i:i+boyut]
        blok = np.array(blok)
        cozulmus_blok = np.dot(matris_mod_ters, blok) % len(turk_alfabesi)
        cozulmus_metin += ''.join(index_to_harf[int(idx)] for idx in cozulmus_blok)
    
    return cozulmus_metin

# Kullanıcıdan metin girişi al
def main():
    sifreli_metin = input("Çözülecek şifreli metni girin: ").lower()
    matris = matris_girisi()
    cozulmus_metin = hill_cozme(sifreli_metin, matris)
    print("Çözülmüş metin:", cozulmus_metin)

if __name__ == "__main__":
    main()
