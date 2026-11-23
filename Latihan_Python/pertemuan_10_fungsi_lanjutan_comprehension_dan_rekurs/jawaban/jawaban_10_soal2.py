# Pertemuan 10 - Jawaban soal 2
# ------------------------------------------------------------
# Soal:
#   Urutkan list tuple [("pena", 3000), ("buku", 12000), ("penghapus", 1500)]
#   berdasarkan harga dari termurah.
# ------------------------------------------------------------

barang = [("pena", 3000), ("buku", 12000), ("penghapus", 1500)]
print(sorted(barang, key=lambda b: b[1]))

# Contoh output:
#   [('penghapus', 1500), ('pena', 3000), ('buku', 12000)]
