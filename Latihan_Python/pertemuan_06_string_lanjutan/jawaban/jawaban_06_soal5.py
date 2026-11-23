# Pertemuan 6 - Jawaban soal 5
# ------------------------------------------------------------
# Soal:
#   Buat enkripsi Caesar dengan pergeseran 3 untuk teks huruf kecil (a→d, b→e,
#   ..., z→c). Karakter selain huruf tidak diubah.
# ------------------------------------------------------------

teks = input("Teks: ")
hasil = ""
for ch in teks:
    if "a" <= ch <= "z":
        baru = (ord(ch) - ord("a") + 3) % 26 + ord("a")
        hasil += chr(baru)
    else:
        hasil += ch
print(hasil)

# Contoh output:
#   Teks: xyz abc
#   abc def
