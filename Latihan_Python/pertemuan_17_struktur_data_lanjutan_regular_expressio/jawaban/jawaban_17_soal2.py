# Pertemuan 17 - Jawaban soal 2
# ------------------------------------------------------------
# Soal:
#   Dengan defaultdict, kelompokkan daftar nama ["Andi", "Budi", "Anto",
#   "Citra", "Bela"] berdasarkan huruf awal.
# ------------------------------------------------------------

from collections import defaultdict
nama = ["Andi", "Budi", "Anto", "Citra", "Bela"]
grup = defaultdict(list)
for n in nama:
    grup[n[0]].append(n)
print(dict(grup))

# Contoh output:
#   {'A': ['Andi', 'Anto'], 'B': ['Budi', 'Bela'], 'C': ['Citra']}
