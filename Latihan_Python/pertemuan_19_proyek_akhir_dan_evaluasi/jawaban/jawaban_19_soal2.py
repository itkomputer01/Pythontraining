# Pertemuan 19 - Jawaban soal 2
# ------------------------------------------------------------
# Soal:
#   Tulis fungsi bilangan_terbesar_kedua(data) yang mengembalikan bilangan
#   terbesar kedua dari sebuah list (abaikan duplikat). Kembalikan None bila
#   tidak ada.
# ------------------------------------------------------------

def terbesar_kedua(data):
    unik = sorted(set(data), reverse=True)
    return unik[1] if len(unik) >= 2 else None

print(terbesar_kedua([5, 9, 9, 3, 7]))
print(terbesar_kedua([4, 4]))

# Contoh output:
#   7
#   None
