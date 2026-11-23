# Pertemuan 16 - Jawaban soal 5
# ------------------------------------------------------------
# Soal:
#   Buat context manager sementara_dalam_huruf_besar memakai @contextmanager
#   yang mencetak "MULAI" dan "SELESAI" mengapit blok with.
# ------------------------------------------------------------

from contextlib import contextmanager

@contextmanager
def sementara_dalam_huruf_besar():
    print("MULAI")
    try:
        yield
    finally:
        print("SELESAI")

with sementara_dalam_huruf_besar():
    print("isi blok")

# Contoh output:
#   MULAI
#   isi blok
#   SELESAI
