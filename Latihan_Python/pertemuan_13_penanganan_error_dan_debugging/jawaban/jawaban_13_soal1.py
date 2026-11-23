# Pertemuan 13 - Jawaban soal 1
# ------------------------------------------------------------
# Soal:
#   Buat program yang terus meminta bilangan bulat sampai pengguna memasukkan
#   angka valid. Tampilkan pesan bila masukan tidak valid.
# ------------------------------------------------------------

while True:
    try:
        n = int(input("Bilangan bulat: "))
        break
    except ValueError:
        print("Masukan tidak valid, coba lagi")
print("Anda memasukkan", n)
