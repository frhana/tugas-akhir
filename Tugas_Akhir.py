print("RENTAL MOBIL ABCD")

print("-------------------------------")

#Input
nama = input("Masukkan Nama Anda : ")
umur = int(input("Masukkan Umur Anda : "))
ktp = int(input("Masukkan Nomor KTP Anda : "))
k_mobil = input("Kategori Mobil [4/6/8 orang] : ")

#Proses
if k_mobil == "4" :
    kapasitasmobil = "4 orang"
    harga = 300000
elif k_mobil == "6" :
    kapasitasmobil = "6 orang"
    harga = 350000
else:
    kapasitasmobil = "8 orang"
    harga = 500000

#Input Durasi Peminjaman
jam = int(input("Masukkan Durasi Peminjaman : "))

#proses potongan
if jam > 6:
    diskon = (jam*harga)*0.1
else:
    diskon = 0

total = (jam*harga)

#Cetak Hasil
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