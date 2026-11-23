# Pertemuan 15 - Jawaban soal 2
# ------------------------------------------------------------
# Soal:
#   Buat class abstrak Bentuk dengan method abstrak luas() dan keliling().
#   Implementasikan pada PersegiPanjang dan Segitiga (segitiga siku-siku dengan
#   alas a dan tinggi t).
# ------------------------------------------------------------

from abc import ABC, abstractmethod

class Bentuk(ABC):
    @abstractmethod
    def luas(self): ...
    @abstractmethod
    def keliling(self): ...

class PersegiPanjang(Bentuk):
    def __init__(self, p, l):
        self.p, self.l = p, l
    def luas(self):
        return self.p * self.l
    def keliling(self):
        return 2 * (self.p + self.l)

class Segitiga(Bentuk):
    def __init__(self, a, t):
        self.a, self.t = a, t
    def luas(self):
        return self.a * self.t / 2
    def keliling(self):
        return self.a + self.t + (self.a ** 2 + self.t ** 2) ** 0.5

for b in [PersegiPanjang(4, 3), Segitiga(3, 4)]:
    print(type(b).__name__, b.luas(), b.keliling())

# Contoh output:
#   PersegiPanjang 12 14
#   Segitiga 6.0 12.0
