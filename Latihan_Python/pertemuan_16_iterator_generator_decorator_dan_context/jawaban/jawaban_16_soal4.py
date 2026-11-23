# Pertemuan 16 - Jawaban soal 4
# ------------------------------------------------------------
# Soal:
#   Buat decorator harus_positif yang melempar ValueError bila argumen pertama
#   fungsi bernilai ≤ 0.
# ------------------------------------------------------------

from functools import wraps

def harus_positif(f):
    @wraps(f)
    def p(x, *args, **kwargs):
        if x <= 0:
            raise ValueError("Argumen harus positif")
        return f(x, *args, **kwargs)
    return p

@harus_positif
def akar(x):
    return x ** 0.5

print(akar(16))
# akar(-4) -> ValueError

# Contoh output:
#   4.0
