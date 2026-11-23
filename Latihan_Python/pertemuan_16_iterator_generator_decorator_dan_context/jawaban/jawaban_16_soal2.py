# Pertemuan 16 - Jawaban soal 2
# ------------------------------------------------------------
# Soal:
#   Buat generator genap() tak hingga yang menghasilkan 0, 2, 4, ... lalu ambil
#   6 nilai pertama dengan islice.
# ------------------------------------------------------------

from itertools import islice

def genap():
    n = 0
    while True:
        yield n
        n += 2

print(list(islice(genap(), 6)))

# Contoh output:
#   [0, 2, 4, 6, 8, 10]
