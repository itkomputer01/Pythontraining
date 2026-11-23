# Pertemuan 14 - Jawaban soal 5
# ------------------------------------------------------------
# Soal:
#   Buat class Produk (nama, harga, stok) dan class Toko yang menyimpan list
#   produk, dengan method tambah_produk() dan total_nilai_stok() (jumlah harga ×
#   stok).
# ------------------------------------------------------------

class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

class Toko:
    def __init__(self):
        self.produk = []

    def tambah_produk(self, p):
        self.produk.append(p)

    def total_nilai_stok(self):
        return sum(p.harga * p.stok for p in self.produk)

t = Toko()
t.tambah_produk(Produk("Buku", 10000, 5))
t.tambah_produk(Produk("Pena", 3000, 10))
print(t.total_nilai_stok())

# Contoh output:
#   80000
