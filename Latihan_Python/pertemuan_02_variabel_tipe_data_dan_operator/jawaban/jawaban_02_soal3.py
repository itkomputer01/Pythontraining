# Pertemuan 2 - Jawaban soal 3
# ------------------------------------------------------------
# Soal:
#   Tukar nilai dua variabel a = 5 dan b = 9 tanpa menghilangkan salah satu
#   nilainya, lalu cetak hasilnya.
# ------------------------------------------------------------

a, b = 5, 9
a, b = b, a      # cara ringkas Python
print(a, b)

# cara dengan variabel bantu
tmp = a
a = b
b = tmp
print(a, b)

# Contoh output:
#   9 5
#   5 9
