# Pertemuan 18 - Jawaban soal 4
# ------------------------------------------------------------
# Soal:
#   Rapikan kode berikut sesuai PEP 8 (nama, spasi, dan baris kosong).
# ------------------------------------------------------------

import os
import sys


def hitung_luas(panjang, lebar):
    luas = panjang * lebar
    return luas


class Kotak:
    def __init__(self, sisi):
        self.sisi = sisi

# Penjelasan: Perubahan: satu impor per baris, nama fungsi snake_case, nama
# class CamelCase, nama parameter dan variabel huruf kecil dan bermakna, spasi
# di sekitar operator, dua baris kosong antar definisi, isi method di baris
# baru.
