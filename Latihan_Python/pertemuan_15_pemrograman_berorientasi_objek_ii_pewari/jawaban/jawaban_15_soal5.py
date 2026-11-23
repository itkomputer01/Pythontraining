# Pertemuan 15 - Jawaban soal 5
# ------------------------------------------------------------
# Soal:
#   Buat @dataclass bernama Siswa (nama, nilai). Urutkan list siswa dari nilai
#   tertinggi dan cetak peringkatnya.
# ------------------------------------------------------------

from dataclasses import dataclass

@dataclass
class Siswa:
    nama: str
    nilai: int

data = [Siswa("Ani", 85), Siswa("Budi", 92), Siswa("Cici", 78)]
urut = sorted(data, key=lambda s: s.nilai, reverse=True)
for i, s in enumerate(urut, start=1):
    print(i, s.nama, s.nilai)

# Contoh output:
#   1 Budi 92
#   2 Ani 85
#   3 Cici 78
