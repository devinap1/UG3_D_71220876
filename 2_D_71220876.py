try:
    mpn = input("masukkan plat nomor kendaraan: ")          #mpn = masukkan plat nomor
    no = int(mpn.split()[1])
    if no >= 0 and no <= 3000:
        print("kendaraan tersebut untuk mobil")
    elif no >= 3001 and no <= 4000:
        print("Kendaraan tersebut untuk motor")
    elif no >= 4001 and no <= 5000:
        print("kendaraan tersebut untuk angkutan umum")
    else:
        print("plat nomor tidak teridentifikasi.")
except (ValueError, IndexError):
    print("plat nomor tidak teridentifikasi, harus terdapat nomor kendaraan setelah kode daerah.")