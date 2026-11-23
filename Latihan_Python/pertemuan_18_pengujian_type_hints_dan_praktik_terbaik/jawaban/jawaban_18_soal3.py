# Pertemuan 18 - Jawaban soal 3
# ------------------------------------------------------------
# Soal:
#   Tulis unit test untuk fungsi bagi_aman yang diharapkan melempar ValueError
#   ketika pembagi nol (ubah fungsinya agar melempar error tersebut).
# ------------------------------------------------------------

import unittest

def bagi_aman(a, b):
    if b == 0:
        raise ValueError("pembagi nol")
    return a / b

class TestBagi(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(bagi_aman(9, 3), 3)

    def test_nol(self):
        with self.assertRaises(ValueError):
            bagi_aman(5, 0)

if __name__ == "__main__":
    unittest.main()
