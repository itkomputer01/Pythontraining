# Pertemuan 10 - Jawaban soal 5
# ------------------------------------------------------------
# Soal:
#   Buat fungsi rekursif pangkat(a, n) yang menghitung a pangkat n (n bilangan
#   bulat ≥ 0) tanpa memakai operator .
# ------------------------------------------------------------

def pangkat(a, n):
    if n == 0:
        return 1
    return a * pangkat(a, n - 1)

print(pangkat(2, 10))

# Contoh output:
#   1024
