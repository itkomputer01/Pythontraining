# Pertemuan 5 - Jawaban soal 7
# ------------------------------------------------------------
# Soal:
#   Cetak pola piramida setinggi 4 baris:
# ------------------------------------------------------------

tinggi = 4
for i in range(1, tinggi + 1):
    print(" " * (tinggi - i) + "*" * (2 * i - 1))

# Contoh output:
#      *
#     ***
#    *****
#   *******
