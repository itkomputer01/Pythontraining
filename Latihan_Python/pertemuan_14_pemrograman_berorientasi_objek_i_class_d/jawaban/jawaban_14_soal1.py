# Pertemuan 14 - Jawaban soal 1
# ------------------------------------------------------------
# Soal:
#   Buat class Mahasiswa dengan atribut nama dan nim, serta method perkenalan()
#   yang mencetak "Saya [nama], NIM [nim]". Buat dua object dan panggil
#   method-nya.
# ------------------------------------------------------------

class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def perkenalan(self):
        print(f"Saya {self.nama}, NIM {self.nim}")

Mahasiswa("Ani", "A001").perkenalan()
Mahasiswa("Budi", "A002").perkenalan()
