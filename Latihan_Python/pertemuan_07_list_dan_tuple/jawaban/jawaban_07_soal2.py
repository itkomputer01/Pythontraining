# Pertemuan 7 - Jawaban soal 2
# ------------------------------------------------------------
# Soal:
#   Cari nilai terbesar dan terkecil dari sebuah list tanpa memakai max() dan
#   min().
# ------------------------------------------------------------

data = [14, 3, 27, 9, 21]
besar = kecil = data[0]
for x in data:
    if x > besar:
        besar = x
    if x < kecil:
        kecil = x
print(besar, kecil)

# Contoh output:
#   27 3
