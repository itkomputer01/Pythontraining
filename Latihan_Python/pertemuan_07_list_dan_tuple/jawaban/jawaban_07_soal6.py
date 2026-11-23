# Pertemuan 7 - Jawaban soal 6
# ------------------------------------------------------------
# Soal:
#   Minta pengguna memasukkan bilangan dipisah spasi (misalnya 4 9 1 7). Ubah
#   menjadi list integer, urutkan menurun, lalu cetak tiga bilangan terbesar.
# ------------------------------------------------------------

teks = input("Bilangan: ")
angka = [int(x) for x in teks.split()]
angka.sort(reverse=True)
print(angka[:3])

# Penjelasan: Baris ke-2 memakai list comprehension yang dibahas di Pertemuan
# 10. Versi tanpa comprehension: buat list kosong, lalu append(int(x)) di
# dalam for x in teks.split().
