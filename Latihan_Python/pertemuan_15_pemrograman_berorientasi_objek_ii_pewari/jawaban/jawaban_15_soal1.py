# Pertemuan 15 - Jawaban soal 1
# ------------------------------------------------------------
# Soal:
#   Buat class Hewan dengan method suara(), lalu subclass Sapi dan Bebek yang
#   meng-override-nya. Cetak suara dari list berisi objek keduanya.
# ------------------------------------------------------------

class Hewan:
    def suara(self):
        return "..."

class Sapi(Hewan):
    def suara(self):
        return "moo"

class Bebek(Hewan):
    def suara(self):
        return "kwek"

for h in [Sapi(), Bebek(), Hewan()]:
    print(type(h).__name__, h.suara())

# Contoh output:
#   Sapi moo
#   Bebek kwek
#   Hewan ...
