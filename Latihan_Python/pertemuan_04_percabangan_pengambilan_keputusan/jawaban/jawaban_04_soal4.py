# Pertemuan 4 - Jawaban soal 4
# ------------------------------------------------------------
# Soal:
#   Buat kalkulator: minta dua bilangan dan satu operator (+, -, *, /), lalu
#   tampilkan hasilnya. Tangani pembagian dengan nol dan operator yang tidak
#   dikenal.
# ------------------------------------------------------------

a = float(input("Bilangan 1: "))
op = input("Operator (+ - * /): ")
b = float(input("Bilangan 2: "))

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        print("Tidak bisa dibagi nol")
    else:
        print(a / b)
else:
    print("Operator tidak dikenal")
