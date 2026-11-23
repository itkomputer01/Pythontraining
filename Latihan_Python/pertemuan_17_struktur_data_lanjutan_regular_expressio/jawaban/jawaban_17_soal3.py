# Pertemuan 17 - Jawaban soal 3
# ------------------------------------------------------------
# Soal:
#   Gunakan regex untuk mengambil semua angka (bilangan bulat) dari "Beli 3 apel
#   seharga 15000 dan 2 jeruk seharga 9000" dan jumlahkan semuanya.
# ------------------------------------------------------------

import re
teks = "Beli 3 apel seharga 15000 dan 2 jeruk seharga 9000"
angka = [int(x) for x in re.findall(r"\d+", teks)]
print(angka, sum(angka))

# Contoh output:
#   [3, 15000, 2, 9000] 24005
