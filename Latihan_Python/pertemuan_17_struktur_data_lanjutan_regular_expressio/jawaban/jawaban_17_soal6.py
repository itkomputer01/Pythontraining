# Pertemuan 17 - Jawaban soal 6
# ------------------------------------------------------------
# Soal:
#   Gunakan itertools.combinations untuk mencetak semua kemungkinan tim 2 orang
#   dari ["Ani", "Budi", "Cici", "Dedi"] dan hitung jumlahnya.
# ------------------------------------------------------------

from itertools import combinations

orang = ["Ani", "Budi", "Cici", "Dedi"]
tim = list(combinations(orang, 2))
for t in tim:
    print(t)
print("Jumlah:", len(tim))

# Contoh output:
#   ('Ani', 'Budi')
#   ('Ani', 'Cici')
#   ('Ani', 'Dedi')
#   ('Budi', 'Cici')
#   ('Budi', 'Dedi')
#   ('Cici', 'Dedi')
#   Jumlah: 6
