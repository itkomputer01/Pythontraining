# Pertemuan 16 - Jawaban soal 3
# ------------------------------------------------------------
# Soal:
#   Buat decorator catat yang mencetak "Memanggil [nama fungsi] dengan argumen
#   ..." sebelum fungsi berjalan.
# ------------------------------------------------------------

from functools import wraps

def catat(f):
    @wraps(f)
    def p(*args, **kwargs):
        print(f"Memanggil {f.__name__} dengan argumen {args} {kwargs}")
        return f(*args, **kwargs)
    return p

@catat
def tambah(a, b):
    return a + b

print(tambah(2, 3))

# Contoh output:
#   Memanggil tambah dengan argumen (2, 3) {}
#   5
