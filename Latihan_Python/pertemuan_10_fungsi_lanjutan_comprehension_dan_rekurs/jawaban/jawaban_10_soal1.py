# Pertemuan 10 - Jawaban soal 1
# ------------------------------------------------------------
# Soal:
#   Buat fungsi rata_rata(*angka) yang menerima sejumlah angka dan mengembalikan
#   rata-ratanya.
# ------------------------------------------------------------

def rata_rata(*angka):
    return sum(angka) / len(angka)

print(rata_rata(80, 90, 70))

# Contoh output:
#   80.0
