# Pertemuan 19 - Jawaban soal 6
# ------------------------------------------------------------
# Soal:
#   Dengan list comprehension, buat list pasangan (x, y) dengan 1 ≤ x < y ≤ 5
#   dan x + y genap.
# ------------------------------------------------------------

pasangan = [(x, y) for x in range(1, 6) for y in range(x + 1, 6)
            if (x + y) % 2 == 0]
print(pasangan)

# Contoh output:
#   [(1, 3), (1, 5), (2, 4), (3, 5)]
