# Pertemuan 3 - Jawaban soal 6
# ------------------------------------------------------------
# Soal:
#   Minta pengguna memasukkan jumlah detik (bilangan bulat). Ubah menjadi format
#   jam:menit:detik dengan dua digit, misalnya 3725 detik menjadi 01:02:05.
# ------------------------------------------------------------

detik = int(input("Jumlah detik: "))
jam = detik // 3600
menit = (detik % 3600) // 60
sisa = detik % 60
print(f"{jam:02d}:{menit:02d}:{sisa:02d}")

# Contoh output:
#   Jumlah detik: 3725
#   01:02:05
