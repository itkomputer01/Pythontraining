# Pertemuan 15 - Jawaban soal 3
# ------------------------------------------------------------
# Soal:
#   Buat class Vektor2D dengan operator +, -, dan ==, serta __str__ yang
#   menampilkan "(x, y)".
# ------------------------------------------------------------

class Vektor2D:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, o):
        return Vektor2D(self.x + o.x, self.y + o.y)
    def __sub__(self, o):
        return Vektor2D(self.x - o.x, self.y - o.y)
    def __eq__(self, o):
        return (self.x, self.y) == (o.x, o.y)
    def __str__(self):
        return f"({self.x}, {self.y})"

a, b = Vektor2D(5, 7), Vektor2D(2, 3)
print(a + b, a - b, a == b)

# Contoh output:
#   (7, 10) (3, 4) False
