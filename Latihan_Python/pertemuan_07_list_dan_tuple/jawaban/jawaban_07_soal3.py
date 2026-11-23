# Pertemuan 7 - Jawaban soal 3
# ------------------------------------------------------------
# Soal:
#   Hapus elemen duplikat dari [3, 1, 3, 2, 1, 5] dengan tetap mempertahankan
#   urutan kemunculan pertama.
# ------------------------------------------------------------

data = [3, 1, 3, 2, 1, 5]
unik = []
for x in data:
    if x not in unik:
        unik.append(x)
print(unik)

# Contoh output:
#   [3, 1, 2, 5]
