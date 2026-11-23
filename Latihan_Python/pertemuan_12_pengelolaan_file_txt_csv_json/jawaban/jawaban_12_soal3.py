# Pertemuan 12 - Jawaban soal 3
# ------------------------------------------------------------
# Soal:
#   Buat nilai.csv (kolom nama, nilai) lalu hitung rata-rata nilai dan nama
#   siswa dengan nilai tertinggi dari file tersebut.
# ------------------------------------------------------------

import csv

total = 0
jumlah = 0
terbaik = ("", -1)
with open("nilai.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        n = int(row["nilai"])
        total += n
        jumlah += 1
        if n > terbaik[1]:
            terbaik = (row["nama"], n)

print(f"Rata-rata: {total / jumlah:.2f}")
print("Tertinggi:", terbaik)

# Contoh output:
#   Rata-rata: 82.33
#   Tertinggi: ('Cici', 92)
