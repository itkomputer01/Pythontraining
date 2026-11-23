# Pertemuan 6 - Jawaban soal 4
# ------------------------------------------------------------
# Soal:
#   Hitung jumlah kata pada sebuah kalimat, lalu cetak kata terpanjangnya.
# ------------------------------------------------------------

kalimat = input("Kalimat: ")
kata = kalimat.split()
print("Jumlah kata:", len(kata))
terpanjang = kata[0]
for k in kata:
    if len(k) > len(terpanjang):
        terpanjang = k
print("Kata terpanjang:", terpanjang)
