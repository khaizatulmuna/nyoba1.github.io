total = 0
barang = []
harga = []

while True:
    print("""Daftar Barang\
    1. Roti \t 5000
    2. Es Krim \t 7000
    3. Keripik \t 8000
    4. Cokelat \t 12000
    5. Buku \t 10000
    6. Pensil \t 4000
    7. Penghapus \t 3000
    """)

    kode = int(input("Masukkan Kode Barang : "))
    if kode == 1:
        barang.append('roti')
        harga.append(5000)
        total += 5000
    elif kode == 2:
        barang.append('es krim')
        harga.append(7000)
        total += 7000
    elif kode == 3:
        barang.append('keripik')
        harga.append(8000)
        total += 8000
    elif kode == 4:
        barang.append('cokelat')
        harga.append(12000)
        total += 12000
    elif kode == 5:
        barang.append('buku')
        harga.append(10000)
        total += 10000
    elif kode == 6:
        barang.append('pensil')
        harga.append(4000)
        total += 4000 
    elif kode == 7:
        barang.append('penghapus')
        harga.append(7000)
        total += 7000
    else:
        print("Kode Tidak Ditemukan")

    lanjut = input('lanjut belanja (y/t) : ')
    if lanjut == 't':
        print("")
        break

print("Barang yang Dibeli : ", barang)
print("Harga Barang : ", harga)
print("Total yang Harus Dibayar : ", total, '\n')

uang = int(input("Masukkan Uang Pembayaran : "))
if uang > total :
    print("Kembalian :", uang-total)
elif uang == total :
    print("Uang Pas")
else :
    print("Uang Kurang", uang-total)