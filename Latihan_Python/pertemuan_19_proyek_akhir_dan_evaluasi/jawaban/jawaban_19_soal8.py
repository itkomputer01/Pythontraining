# Pertemuan 19 - Jawaban soal 8
# ------------------------------------------------------------
# Soal:
#   Tulis decorator coba_ulang(kali) yang menjalankan ulang fungsi sampai kali
#   kali bila terjadi exception, lalu melempar exception terakhir bila tetap
#   gagal.
# ------------------------------------------------------------

from functools import wraps

def coba_ulang(kali):
    def dekorator(f):
        @wraps(f)
        def p(*args, **kwargs):
            for percobaan in range(1, kali + 1):
                try:
                    return f(*args, **kwargs)
                except Exception as e:
                    print(f"Percobaan {percobaan} gagal: {e}")
                    if percobaan == kali:
                        raise
        return p
    return dekorator

hitung = {"n": 0}

@coba_ulang(3)
def tidak_stabil():
    hitung["n"] += 1
    if hitung["n"] < 3:
        raise RuntimeError("gagal sementara")
    return "berhasil"

print(tidak_stabil())

# Contoh output:
#   Percobaan 1 gagal: gagal sementara
#   Percobaan 2 gagal: gagal sementara
#   berhasil
