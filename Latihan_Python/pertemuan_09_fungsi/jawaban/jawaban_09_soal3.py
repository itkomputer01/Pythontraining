# Pertemuan 9 - Jawaban soal 3
# ------------------------------------------------------------
# Soal:
#   Buat fungsi statistik(data) yang mengembalikan nilai terkecil, terbesar, dan
#   rata-rata dari sebuah list.
# ------------------------------------------------------------

def statistik(data):
    return min(data), max(data), sum(data) / len(data)

kecil, besar, rata = statistik([12, 7, 20, 9])
print(kecil, besar, rata)

# Contoh output:
#   7 20 12.0
