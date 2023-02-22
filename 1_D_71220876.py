msk = float(input("masukkan nilai curah hujan : "))    #msk = masukkan nilai curah hujan

severity = "wrong Input" if msk < 0 else "cuaca terang/Berawan" if msk == 0 else "curah hujan ringan" if msk < 21 else "curah hujan sedang" if msk < 51 else "curah hujan lebat" if msk < 101 else "Curah hujan ekstrem"

print(f"Nilai curah hujan {msk} mm termasuk dalam kategori: {severity}")