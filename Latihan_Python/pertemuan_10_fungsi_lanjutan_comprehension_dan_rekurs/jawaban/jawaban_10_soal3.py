# Pertemuan 10 - Jawaban soal 3
# ------------------------------------------------------------
# Soal:
#   Dengan list comprehension, buat list kuadrat dari bilangan genap antara 1
#   dan 20.
# ------------------------------------------------------------

hasil = [x ** 2 for x in range(1, 21) if x % 2 == 0]
print(hasil)

# Contoh output:
#   [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
