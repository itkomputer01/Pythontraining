# Pertemuan 8 - Jawaban soal 2
# ------------------------------------------------------------
# Soal:
#   Hitung frekuensi setiap huruf pada kata "mississippi" dan cetak hasilnya.
# ------------------------------------------------------------

frek = {}
for ch in "mississippi":
    frek[ch] = frek.get(ch, 0) + 1
print(frek)

# Contoh output:
#   {'m': 1, 'i': 4, 's': 4, 'p': 2}
