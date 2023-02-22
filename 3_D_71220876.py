deret_awal = int(input("silahkan masukkan awal deret: "))
deret_akhir = int(input("silahkan masukkan akhir deret: "))

nomor = [num for num in range(deret_awal, deret_akhir+1) if (num % 6 != 0) and (num % 8 != 0)]

hasil = ' '.join([str(num) for num in nomor])

print(f"{hasil}")