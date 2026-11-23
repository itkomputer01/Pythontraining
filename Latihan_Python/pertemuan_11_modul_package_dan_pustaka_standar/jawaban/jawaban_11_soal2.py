# Pertemuan 11 - Jawaban soal 2
# ------------------------------------------------------------
# Soal:
#   Buat fungsi buat_password(panjang) yang menghasilkan kata sandi acak dari
#   huruf besar, huruf kecil, dan angka (gunakan random dan string).
# ------------------------------------------------------------

import random
import string

def buat_password(panjang):
    karakter = string.ascii_letters + string.digits
    hasil = ""
    for _ in range(panjang):
        hasil += random.choice(karakter)
    return hasil

print(buat_password(10))

# Penjelasan: Untuk kata sandi sungguhan gunakan modul secrets yang lebih
# aman.
