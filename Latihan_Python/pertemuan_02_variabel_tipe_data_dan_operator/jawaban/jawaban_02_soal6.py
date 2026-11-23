# Pertemuan 2 - Jawaban soal 6
# ------------------------------------------------------------
# Soal:
#   Sebuah angka tiga digit disimpan dalam variabel n = 538. Dengan operator //
#   dan %, pisahkan dan cetak digit ratusan, puluhan, dan satuan.
# ------------------------------------------------------------

n = 538
ratusan = n // 100
puluhan = (n // 10) % 10
satuan = n % 10
print(ratusan, puluhan, satuan)

# Contoh output:
#   5 3 8
