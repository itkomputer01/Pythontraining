# Pertemuan 17 - Jawaban soal 4
# ------------------------------------------------------------
# Soal:
#   Buat fungsi valid_email(s) berbasis regex sederhana yang mengembalikan True
#   untuk nama@domain.com dan False untuk nama@domain.
# ------------------------------------------------------------

import re

def valid_email(s):
    return re.fullmatch(r"[\w.+-]+@[\w-]+(\.[\w-]+)+", s) is not None

print(valid_email("nama@domain.com"), valid_email("nama@domain"))

# Contoh output:
#   True False
