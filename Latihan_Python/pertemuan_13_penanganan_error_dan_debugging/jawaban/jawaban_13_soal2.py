# Pertemuan 13 - Jawaban soal 2
# ------------------------------------------------------------
# Soal:
#   Buat fungsi bagi_aman(a, b) yang mengembalikan hasil bagi, atau None dan
#   mencetak pesan bila terjadi pembagian dengan nol.
# ------------------------------------------------------------

def bagi_aman(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Pembagian dengan nol")
        return None

print(bagi_aman(10, 2))
print(bagi_aman(5, 0))

# Contoh output:
#   5.0
#   Pembagian dengan nol
#   None
