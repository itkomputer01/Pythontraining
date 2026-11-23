# Pertemuan 18 - Jawaban soal 1
# ------------------------------------------------------------
# Soal:
#   Tambahkan type hints dan docstring pada fungsi berikut.
# ------------------------------------------------------------

def hitung_diskon(harga: float, persen: float) -> float:
    """Mengembalikan harga setelah dipotong diskon.

    harga: harga awal, persen: besar diskon 0-100.
    """
    return harga - harga * persen / 100
