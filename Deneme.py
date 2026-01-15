import random

def stil_asistani():
    # Bu program kullanicinin verdigi bilgilere gore kiyafet onerisi yapar.
    print("--- Stil Asistani Programi ---")

    # 1. Kullanicidan bilgileri aliyoruz
    print("Lutfen asagidaki sorulari cevaplayin:")
    hava = input("Hava durumu nasil? (gunesli, yagmurlu, soguk): ").lower()
    mekan = input("Nereye gidiyorsunuz? (okul, is, gezme): ").lower()
    mod = input("Kendinizi nasil hissediyorsunuz? (mutlu, yorgun, ciddi): ").lower()

    # 2. Kiyafet ve renk listeleri
    renkler = ["Mavi", "Siyah", "Beyaz", "Gri", "Bej"]
    kiyafetler = []
    aksesuarlar = []

    # Hava durumuna gore temel kiyafet secimi
    if "gunes" in hava:
        kiyafetler = ["T-shirt", "Ince Pantolon"]
        aksesuarlar = ["Gunes Gozlugu"]
    elif "yagmur" in hava:
        kiyafetler = ["Yagmurluk", "Su Gecirmez Pantolon"]
        aksesuarlar = ["Semsiye"]
    elif "soguk" in hava:
        kiyafetler = ["Kalin Kazak", "Mont"]
        aksesuarlar = ["Atki", "Bere"]
    else:
        # Eger farkli bir sey yazilirsa varsayilan kiyafetler
        kiyafetler = ["Hirka", "Siyah Pantolon"]
        aksesuarlar = ["Kol Saati"]

    # Mekana gore ekleme yapalim
    if "is" in mekan:
        kiyafetler.append("Ceket")
    elif "okul" in mekan:
        aksesuarlar.append("Sirt Cantasi")

    # 3. Sonuclari ekrana yazdirma
    print("\n--- Onerileriniz Hazir ---")
    print("Sizin icin sectigimiz tarz: ")
    print("- Gunun rengi: " + random.choice(renkler))
    print("- Giyecekler: " + ", ".join(kiyafetler))
    print("- Aksesuarlar: " + ", ".join(aksesuarlar))

    # Moduna gore kucuk bir not
    if "mutlu" in mod:
        print("Not: Enerjiniz harika, bugun cok guzel gececek!")
    elif "yorgun" in mod:
        print("Not: Rahat parcalar secmeye calistik, kendinizi iyi hissedin.")

    print("--------------------------")


# Programi baslat
# DUZELTME: Buradaki main yazisinin yanlarinda ikişer tane alt cizgi olmali.
if __name__ == "__main__":
    stil_asistani()