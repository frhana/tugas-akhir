print("RENTAL MOBIL ABCD")

print("-------------------------------")

#Input
nama = input("Masukkan Nama Anda : ")
umur = int(input("Masukkan Umur Anda : "))

if umur < 18:
    print("Maaf", nama, "anda belum bisa meminjam kendaraan")
else:
    ktp = int(input("Masukkan Nomor KTP Anda : "))
    k_mobil = input("Kategori Mobil [4/6/8 orang] : ")
    if k_mobil == "4" :
        kapasitasmobil = "4 orang"
        harga = 300000
    elif k_mobil == "6" :
        kapasitasmobil = "6 orang"
        harga = 350000
    else:
        kapasitasmobil = "8 orang"
        harga = 500000
    jam = int(input("Masukkan Durasi Peminjaman (dalam hari): "))
    if jam > 6:
        diskon = (jam*harga)*0.1
    else:
        diskon = 0

    total = (jam*harga)

    print("-------------------------------")
    print("RENTAL MOBIL ABCD")
    print("-------------------------------")
    print("Masukkan Nama Anda            : "+str(nama))
    print("Masukkan Umur Anda            : "+str(umur))
    print("Masukkan Nomor KTP Anda       : "+str(ktp))
    print("Kapasitas Mobil               : "+str(k_mobil))
    print("Harga                         : ",+(harga))
    print("Potongan yang didapat        : ",+(diskon))
    print("-------------------------------")
    print("Total Bayar                  : ",+(total))
