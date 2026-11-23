# Pertemuan 13 - Jawaban soal 4
# ------------------------------------------------------------
# Soal:
#   Buat exception UmurTidakValid dan fungsi set_umur(u) yang melemparnya bila
#   umur negatif atau lebih dari 130.
# ------------------------------------------------------------

class UmurTidakValid(Exception):
    pass

def set_umur(u):
    if u < 0 or u > 130:
        raise UmurTidakValid(f"Umur {u} tidak valid")
    return u

try:
    set_umur(-5)
except UmurTidakValid as e:
    print(e)

# Contoh output:
#   Umur -5 tidak valid
