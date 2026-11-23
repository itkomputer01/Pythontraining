# Pertemuan 13 - Jawaban soal 3
# ------------------------------------------------------------
# Soal:
#   Buat fungsi yang membaca file bernama dari parameter dan mencetak isinya;
#   jika file tidak ada cetak File tidak ditemukan.
# ------------------------------------------------------------

def baca(nama_file):
    try:
        with open(nama_file, encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("File tidak ditemukan")

baca("tidak_ada.txt")

# Contoh output:
#   File tidak ditemukan
