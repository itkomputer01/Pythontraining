# Pertemuan 13 - Jawaban soal 6
# ------------------------------------------------------------
# Soal:
#   Perbaiki logic error: fungsi berikut seharusnya menghitung rata-rata list,
#   tetapi hasilnya salah. Temukan dan perbaiki bug-nya.
# ------------------------------------------------------------

# Penjelasan: Kode bermasalah:

def rata_rata(data):
    total = 0
    for x in data:
        total += x
        return total / len(data)    # return di dalam loop

# Penjelasan: Bug: return berada di dalam perulangan sehingga fungsi berhenti
# pada elemen pertama. Perbaikan: geser return keluar dari perulangan
# (indentasi sejajar for).

def rata_rata(data):
    total = 0
    for x in data:
        total += x
    return total / len(data)

print(rata_rata([80, 90, 70]))

# Contoh output:
#   80.0
