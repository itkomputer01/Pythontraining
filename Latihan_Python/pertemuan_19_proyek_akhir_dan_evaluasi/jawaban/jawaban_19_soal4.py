# Pertemuan 19 - Jawaban soal 4
# ------------------------------------------------------------
# Soal:
#   Baca file nilai.csv (kolom nama, nilai) lalu tulis hasil ke hasil.json
#   berisi nama, nilai, dan grade (A ≥ 85, B ≥ 70, selain itu C).
# ------------------------------------------------------------

import csv, json

def grade(n):
    if n >= 85:
        return "A"
    if n >= 70:
        return "B"
    return "C"

hasil = []
with open("nilai.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        n = int(row["nilai"])
        hasil.append({"nama": row["nama"], "nilai": n, "grade": grade(n)})

with open("hasil.json", "w", encoding="utf-8") as f:
    json.dump(hasil, f, indent=2)
print(hasil)

# Contoh output:
#   [{'nama': 'Ani', 'nilai': 85, 'grade': 'A'}, {'nama': 'Budi', 'nilai': 70, 'grade': 'B'}, {'nama': 'Cici', 'nilai': 92, 'grade': 'A'}]
