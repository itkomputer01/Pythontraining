# Pertemuan 10 - Jawaban soal 7
# ------------------------------------------------------------
# Soal:
#   Dari list kata = ["Belajar", "python", "itu", "Asyik", "sekali"], ambil kata
#   yang diawali huruf kapital menggunakan filter() dan lambda.
# ------------------------------------------------------------

kata = ["Belajar", "python", "itu", "Asyik", "sekali"]
kapital = list(filter(lambda k: k[0].isupper(), kata))
print(kapital)

# Contoh output:
#   ['Belajar', 'Asyik']
