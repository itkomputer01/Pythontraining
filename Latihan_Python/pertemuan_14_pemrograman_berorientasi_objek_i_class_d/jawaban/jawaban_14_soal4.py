# Pertemuan 14 - Jawaban soal 4
# ------------------------------------------------------------
# Soal:
#   Buat class Counter yang memiliki method tambah(), kurang(), dan reset(),
#   dengan nilai awal 0. Cetak nilainya memakai __str__.
# ------------------------------------------------------------

class Counter:
    def __init__(self):
        self.nilai = 0

    def tambah(self):
        self.nilai += 1

    def kurang(self):
        self.nilai -= 1

    def reset(self):
        self.nilai = 0

    def __str__(self):
        return f"Counter = {self.nilai}"

c = Counter()
c.tambah(); c.tambah(); c.kurang()
print(c)

# Contoh output:
#   Counter = 1
