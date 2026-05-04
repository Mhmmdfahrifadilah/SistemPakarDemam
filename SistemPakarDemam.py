def medicheck_sistem_pakar():
    print("=== MEDICHECK: SISTEM PAKAR DIAGNOSIS DEMAM ===")
    print("Silakan jawab pertanyaan berikut untuk skrining awal.\n")

    # V1: Durasi Demam
    v1 = input("Apakah demam sudah berlangsung >= 3 hari? (ya/tidak): ").lower()

    if v1 == "tidak":
        # V4: Nyeri Sendi
        v4 = input("Apakah Anda merasakan nyeri sendi dan otot yang hebat? (ya/tidak): ").lower()
        if v4 == "ya":
            print("\nHASIL: G5 - Demam Akut")
            print("Gejala sistemik namun belum menjurus ke infeksi spesifik.")
        else:
            print("\nHASIL: G4 - Observasi Mandiri")
            print("Demam ringan biasa. Perbanyak minum air dan istirahat.")

    elif v1 == "ya":
        # V2: Pola Demam
        print("Pola demam: 1. Naik-Turun (Siklus) | 2. Terus Menerus")
        v2 = input("Pilih pola demam (1/2): ")

        if v2 == "1":
            print("\nHASIL: G3 - Indikasi Malaria")
            print("Demam dengan pola menggigil berkala (siklus).")
        
        elif v2 == "2":
            # V3: Bintik Merah
            v3 = input("Apakah muncul bintik merah di kulit atau pendarahan gusi? (ya/tidak): ").lower()
            if v3 == "ya":
                print("\nHASIL: G1 - Indikasi DBD")
                print("Demam tinggi disertai bintik merah. Segera cek Trombosit.")
            else:
                # V5: Gangguan Pencernaan
                v5 = input("Apakah ada gangguan pencernaan (diare/sembelit parah)? (ya/tidak): ").lower()
                if v5 == "ya":
                    print("\nHASIL: G2 - Indikasi Tifus (Demam Tifoid)")
                    print("Demam menetap disertai gangguan pencernaan.")
                else:
                    print("\nHASIL: G5 - Demam Akut")
                    print("Gejala belum spesifik, silakan konsultasi ke dokter.")

# Menjalankan aplikasi
if __name__ == "__main__":
    medicheck_sistem_pakar()