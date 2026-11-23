# Pertemuan 9 - Jawaban soal 2
# ------------------------------------------------------------
# Soal:
#   Buat fungsi is_prima(n) yang mengembalikan True jika n bilangan prima.
#   Gunakan untuk mencetak semua bilangan prima ≤ 50.
# ------------------------------------------------------------

def is_prima(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for n in range(1, 51):
    if is_prima(n):
        print(n, end=" ")

# Contoh output:
#   2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
