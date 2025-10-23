# PT Jaya Abadi perlu mencatat data karyawan baru secara digital. Buatkan sebuah class Python bernama Karyawan yang memiliki metode konstruktor untuk menerima dan menyimpan nama, jabatan, dan gaji.
# Selain itu, tambahkan metode tampilkan_info() yang mencetak ketiga atribut tersebut, dan metode naikkan_gaji(jumlah) yang akan menambahkan nilai jumlah ke atribut gaji.

class Karyawan:
    def __init__(self, nama, jabatan, gaji):
        self.nama = nama
        self.jabatan = jabatan
        self.gaji = gaji

    def tampilkan_info(self):
        return f"Nama : {self.nama}\nJabatan : {self.jabatan}\nGaji : {self.gaji}"
    
    def naikkan_gaji(self, tambah):
        self.gaji += tambah

try :
    nama = input("Masukkan Nama Karyawan: ")
    jabatan = input("Memasukkan Jabatan Karyawan: ")
    gaji = int(input("Masukkan Gaji Karyawan: "))

    karyawan1 = Karyawan(nama=nama, jabatan=jabatan, gaji=gaji)

    print("\n===INFO KARYAWAN===")
    print(karyawan1.tampilkan_info())
    print("\nGAJI AWAL")
    print(karyawan1.gaji)
    print("\nGAJI SETELAH DITAMBAHKAN")
    karyawan1.naikkan_gaji(200000)
    print(karyawan1.gaji)
except ValueError :
    print(" NILAI GAJI HARUS BERUPA ANGKA SAJA!")