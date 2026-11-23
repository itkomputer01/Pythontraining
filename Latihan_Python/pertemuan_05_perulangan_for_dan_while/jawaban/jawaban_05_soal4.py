# Pertemuan 5 - Jawaban soal 4
# ------------------------------------------------------------
# Soal:
#   Hitung faktorial dari bilangan yang diinput menggunakan perulangan while
#   (misalnya 5! = 120).
# ------------------------------------------------------------

n = int(input("n = "))
hasil = 1
i = n
while i > 1:
    hasil *= i
    i -= 1
print(f"{n}! = {hasil}")
