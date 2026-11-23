# Pertemuan 8 - Jawaban soal 1
# ------------------------------------------------------------
# Soal:
#   Buat dictionary buku telepon dengan 3 kontak. Cetak nomor milik seorang
#   kontak yang namanya diinput; bila tidak ada cetak Kontak tidak ditemukan.
# ------------------------------------------------------------

kontak = {"Ani": "0812111", "Budi": "0813222", "Cici": "0857333"}
nama = input("Cari nama: ")
if nama in kontak:
    print(nama, kontak[nama])
else:
    print("Kontak tidak ditemukan")
