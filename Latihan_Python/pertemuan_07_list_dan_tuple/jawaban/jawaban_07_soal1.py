# Pertemuan 7 - Jawaban soal 1
# ------------------------------------------------------------
# Soal:
#   Hitung rata-rata dari list nilai = [80, 65, 90, 72, 88] tanpa memakai fungsi
#   sum().
# ------------------------------------------------------------

nilai = [80, 65, 90, 72, 88]
total = 0
for n in nilai:
    total += n
print(total / len(nilai))

# Contoh output:
#   79.0
