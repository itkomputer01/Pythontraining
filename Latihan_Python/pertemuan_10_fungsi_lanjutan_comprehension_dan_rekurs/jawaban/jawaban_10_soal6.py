# Pertemuan 10 - Jawaban soal 6
# ------------------------------------------------------------
# Soal:
#   Buat fungsi rekursif balik(s) yang membalik sebuah string.
# ------------------------------------------------------------

def balik(s):
    if len(s) <= 1:
        return s
    return balik(s[1:]) + s[0]

print(balik("python"))

# Contoh output:
#   nohtyp
