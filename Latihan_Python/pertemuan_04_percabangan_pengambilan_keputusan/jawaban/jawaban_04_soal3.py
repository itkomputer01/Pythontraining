# Pertemuan 4 - Jawaban soal 3
# ------------------------------------------------------------
# Soal:
#   Minta sebuah tahun dan tentukan apakah tahun kabisat. Tahun kabisat: habis
#   dibagi 4 tetapi tidak habis dibagi 100, kecuali habis dibagi 400.
# ------------------------------------------------------------

tahun = int(input("Tahun: "))
if (tahun % 4 == 0 and tahun % 100 != 0) or tahun % 400 == 0:
    print("Kabisat")
else:
    print("Bukan kabisat")

# Penjelasan: Uji dengan 2000 (kabisat), 1900 (bukan), 2024 (kabisat), dan
# 2026 (bukan).
