# Pertemuan 17 - Jawaban soal 5
# ------------------------------------------------------------
# Soal:
#   Buat basis data SQLite toko.db dengan tabel barang (id, nama, harga, stok).
#   Masukkan 3 barang, tampilkan barang dengan stok kurang dari 10, lalu naikkan
#   harga semua barang 10%.
# ------------------------------------------------------------

import sqlite3

con = sqlite3.connect("toko.db")
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS barang (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama TEXT, harga REAL, stok INTEGER)""")
cur.executemany("INSERT INTO barang (nama, harga, stok) VALUES (?, ?, ?)",
                [("Pena", 3000, 50), ("Buku", 12000, 8), ("Tas", 150000, 4)])
con.commit()

for b in cur.execute("SELECT nama, stok FROM barang WHERE stok < ?", (10,)):
    print(b)

cur.execute("UPDATE barang SET harga = ROUND(harga * 1.1)")
con.commit()
print(cur.execute("SELECT nama, harga FROM barang").fetchall())
con.close()

# Contoh output:
#   ('Buku', 8)
#   ('Tas', 4)
#   [('Pena', 3300.0), ('Buku', 13200.0), ('Tas', 165000.0)]
