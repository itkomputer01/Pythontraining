# Pertemuan 9 - Jawaban soal 5
# ------------------------------------------------------------
# Soal:
#   Buat fungsi fibonacci(n) yang mengembalikan list berisi n bilangan Fibonacci
#   pertama (0, 1, 1, 2, 3, ...).
# ------------------------------------------------------------

def fibonacci(n):
    hasil = []
    a, b = 0, 1
    for _ in range(n):
        hasil.append(a)
        a, b = b, a + b
    return hasil

print(fibonacci(10))

# Contoh output:
#   [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
