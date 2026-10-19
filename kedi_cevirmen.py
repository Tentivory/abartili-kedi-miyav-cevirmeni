#!/usr/bin/env python3
# Abartılı Kedi Miyav Çevirmeni
# Kediler ne düşünüyor? Biz biliyoruz (ya da öyle davranıyoruz).

import random

ceviriler = {
    "miyav": [
        "Açım! Hemen mama getir, yoksa evren çöker.",
        "İnsanlar neden bu kadar yavaş? Ben zaten 3 saat önce açtım.",
        "Bu dünya kedi merkezli olmalı. Tartışmasız."
    ],
    "mırıltı": [
        "Mutluyum ama bunu itiraf etmek istemiyorum. İmaj meselesi.",
        "Seni seviyorum... ama sadece şimdi. Sonra görürüz.",
        "Felsefi olarak, mırıltı evrenin titreşimidir."
    ],
    "hışs": [
        "Uzaklaş! Bu benim bölgem. Mahkemeye giderim.",
        "Tehdit algıladım. Savunma modu aktif.",
        "Siyasi olarak tarafsızım ama sen değilsin."
    ],
    "miyav miyav": [
        "Acil durum! Bir şey oldu ama ne olduğunu anlatamam çünkü kediim.",
        "İki kez söylüyorum: DİKKAT!"
    ]
}

def cevir(ses):
    ses = ses.lower().strip()
    if ses in ceviriler:
        return random.choice(ceviriler[ses])
    else:
        return random.choice([
            "Bu ses tanınmadı. Kediniz yeni bir dil icat etmiş olabilir.",
            "Miyav değil, başka bir şey. Belki kuş?ş",
            "Anlamadım. Tekrar mıyavla lütfen."
        ])

if __name__ == "__main__":
    print("=== ABARTILI KEDİ MİYAV ÇEVİRMENİ ===")
    print("Kediniz ne diyor? Sesi yazın (miyav, mırıltı, hışs...):")
    while True:
        ses = input("> ")
        if ses.lower() in ["çık", "exit", "quit"]:
            print("Kedilerle konuşmak bitti. Hoşça kalın.")
            break
        print(f"Çeviri: {cevir(ses)}\n")

# Gizli: Bazen kediler bile siyasete karışır. Mıyav mıyav seçim.
