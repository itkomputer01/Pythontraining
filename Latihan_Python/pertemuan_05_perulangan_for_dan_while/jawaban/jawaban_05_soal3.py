# Pertemuan 5 - Jawaban soal 3
# ------------------------------------------------------------
# Soal:
#   Minta bilangan n, lalu cetak tabel perkalian n dari 1 sampai 10 dengan
#   format n x i = hasil.
# ------------------------------------------------------------

n = int(input("n = "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
