# Pertemuan 5 - Jawaban soal 2
# ------------------------------------------------------------
# Soal:
#   Hitung jumlah semua bilangan kelipatan 3 atau 5 yang kurang dari 100.
# ------------------------------------------------------------

total = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)

# Contoh output:
#   2318
