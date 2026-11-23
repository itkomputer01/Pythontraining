# Pertemuan 18 - Jawaban soal 2
# ------------------------------------------------------------
# Soal:
#   Tulis unit test untuk fungsi is_prima(n) (dari Pertemuan 9) yang mencakup
#   bilangan prima, bukan prima, 0, 1, dan bilangan negatif.
# ------------------------------------------------------------

# test_prima.py
import unittest

def is_prima(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

class TestPrima(unittest.TestCase):
    def test_prima(self):
        for n in [2, 3, 5, 13, 97]:
            self.assertTrue(is_prima(n), n)

    def test_bukan_prima(self):
        for n in [4, 9, 25, 100]:
            self.assertFalse(is_prima(n), n)

    def test_batas(self):
        for n in [0, 1, -7]:
            self.assertFalse(is_prima(n), n)

if __name__ == "__main__":
    unittest.main()
