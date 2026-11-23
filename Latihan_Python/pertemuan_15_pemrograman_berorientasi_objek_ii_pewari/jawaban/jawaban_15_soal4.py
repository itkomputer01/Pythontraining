# Pertemuan 15 - Jawaban soal 4
# ------------------------------------------------------------
# Soal:
#   Buat class Karyawan (nama, gaji_pokok) dengan method total_gaji(). Buat
#   subclass Manajer (tunjangan tetap 2.000.000) dan Programmer (bonus per
#   proyek 500.000). Hitung total gaji dari sebuah list karyawan.
# ------------------------------------------------------------

class Karyawan:
    def __init__(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok
    def total_gaji(self):
        return self.gaji_pokok

class Manajer(Karyawan):
    def total_gaji(self):
        return self.gaji_pokok + 2000000

class Programmer(Karyawan):
    def __init__(self, nama, gaji_pokok, proyek):
        super().__init__(nama, gaji_pokok)
        self.proyek = proyek
    def total_gaji(self):
        return self.gaji_pokok + 500000 * self.proyek

staf = [Manajer("Ani", 8000000), Programmer("Budi", 6000000, 3)]
for s in staf:
    print(s.nama, f"Rp{s.total_gaji():,}")

# Contoh output:
#   Ani Rp10,000,000
#   Budi Rp7,500,000
