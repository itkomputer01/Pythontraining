# Pertemuan 3 - Jawaban soal 1
# ------------------------------------------------------------
# Soal:
#   Buat program kalkulator sederhana: minta dua bilangan dari pengguna lalu
#   cetak hasil penjumlahan, pengurangan, perkalian, dan pembagian.
# ------------------------------------------------------------

a = float(input("Bilangan pertama: "))
b = float(input("Bilangan kedua: "))
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")

# Catatan: Jika b diisi 0, program berhenti dengan ZeroDivisionError. Cara
# mengatasinya dipelajari pada Pertemuan 4 dan 13.
