# Pertemuan 14 - Jawaban soal 3
# ------------------------------------------------------------
# Soal:
#   Buat class Lingkaran dengan atribut jari_jari dan property luas serta
#   keliling (hanya dibaca).
# ------------------------------------------------------------

import math

class Lingkaran:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    @property
    def luas(self):
        return math.pi * self.jari_jari ** 2

    @property
    def keliling(self):
        return 2 * math.pi * self.jari_jari

l = Lingkaran(7)
print(round(l.luas, 2), round(l.keliling, 2))

# Contoh output:
#   153.94 43.98
