# Pertemuan 4 - Jawaban soal 2
# ------------------------------------------------------------
# Soal:
#   Minta nilai angka (0-100) dan cetak grade: A (≥ 85), B (≥ 70), C (≥ 55), D
#   (≥ 40), selain itu E. Jika nilai di luar 0-100, cetak Nilai tidak valid.
# ------------------------------------------------------------

nilai = float(input("Nilai (0-100): "))
if nilai < 0 or nilai > 100:
    print("Nilai tidak valid")
elif nilai >= 85:
    print("A")
elif nilai >= 70:
    print("B")
elif nilai >= 55:
    print("C")
elif nilai >= 40:
    print("D")
else:
    print("E")
