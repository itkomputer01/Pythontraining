# Pertemuan 7 - Jawaban soal 4
# ------------------------------------------------------------
# Soal:
#   Diberikan nama = ["Ani", "Budi", "Cici"] dan umur = [20, 22, 19]. Cetak
#   setiap pasangan dengan format Ani berumur 20 tahun.
# ------------------------------------------------------------

nama = ["Ani", "Budi", "Cici"]
umur = [20, 22, 19]
for n, u in zip(nama, umur):
    print(f"{n} berumur {u} tahun")
