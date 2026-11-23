# Pertemuan 12 - Jawaban soal 4
# ------------------------------------------------------------
# Soal:
#   Simpan dictionary berisi data tiga produk (nama, harga) ke produk.json, lalu
#   baca kembali dan cetak total harganya.
# ------------------------------------------------------------

import json

produk = [
    {"nama": "Pena", "harga": 3000},
    {"nama": "Buku", "harga": 12000},
    {"nama": "Tas", "harga": 150000},
]
with open("produk.json", "w", encoding="utf-8") as f:
    json.dump(produk, f, indent=2)

with open("produk.json", encoding="utf-8") as f:
    data = json.load(f)
print(sum(p["harga"] for p in data))

# Contoh output:
#   165000
