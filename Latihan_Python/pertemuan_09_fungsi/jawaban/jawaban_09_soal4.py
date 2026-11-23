# Pertemuan 9 - Jawaban soal 4
# ------------------------------------------------------------
# Soal:
#   Buat fungsi hitung_gaji(pokok, tunjangan=500000, bonus=0) yang mengembalikan
#   total gaji. Panggil dengan tiga cara berbeda (hanya pokok; pokok dan bonus
#   dengan kata kunci; ketiganya).
# ------------------------------------------------------------

def hitung_gaji(pokok, tunjangan=500000, bonus=0):
    return pokok + tunjangan + bonus

print(hitung_gaji(4000000))
print(hitung_gaji(4000000, bonus=250000))
print(hitung_gaji(4000000, 300000, 100000))

# Contoh output:
#   4500000
#   4750000
#   4400000
