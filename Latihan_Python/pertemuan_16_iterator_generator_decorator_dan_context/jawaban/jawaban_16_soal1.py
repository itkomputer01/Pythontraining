# Pertemuan 16 - Jawaban soal 1
# ------------------------------------------------------------
# Soal:
#   Buat generator kuadrat(n) yang menghasilkan kuadrat dari 1 sampai n. Cetak
#   untuk n = 5.
# ------------------------------------------------------------

def kuadrat(n):
    for i in range(1, n + 1):
        yield i * i

print(list(kuadrat(5)))

# Contoh output:
#   [1, 4, 9, 16, 25]
