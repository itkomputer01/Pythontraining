# Pertemuan 7 - Jawaban soal 5
# ------------------------------------------------------------
# Soal:
#   Hitung jumlah diagonal utama dari matriks 3×3 [[1,2,3],[4,5,6],[7,8,9]].
# ------------------------------------------------------------

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total = 0
for i in range(len(m)):
    total += m[i][i]
print(total)

# Contoh output:
#   15
