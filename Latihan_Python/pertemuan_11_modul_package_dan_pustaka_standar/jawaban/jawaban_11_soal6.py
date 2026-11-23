# Pertemuan 11 - Jawaban soal 6
# ------------------------------------------------------------
# Soal:
#   Lempar dua dadu sebanyak 1000 kali memakai random, lalu cetak berapa kali
#   jumlah kedua dadu bernilai 7.
# ------------------------------------------------------------

import random

hitung = 0
for _ in range(1000):
    if random.randint(1, 6) + random.randint(1, 6) == 7:
        hitung += 1
print(hitung)

# Penjelasan: Hasilnya berbeda tiap dijalankan, secara teori sekitar 1/6 dari
# 1000 (± 167).
