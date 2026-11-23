# Pertemuan 12 - Jawaban soal 2
# ------------------------------------------------------------
# Soal:
#   Hitung jumlah baris, jumlah kata, dan jumlah karakter dari file teks
#   catatan.txt.
# ------------------------------------------------------------

with open("catatan.txt", encoding="utf-8") as f:
    isi = f.read()

baris = isi.splitlines()
print("Baris   :", len(baris))
print("Kata    :", len(isi.split()))
print("Karakter:", len(isi))
