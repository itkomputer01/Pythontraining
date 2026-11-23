# Pertemuan 19 - Jawaban soal 1
# ------------------------------------------------------------
# Soal:
#   Tulis fungsi hitung_kata(teks) yang mengembalikan dictionary frekuensi kata
#   (huruf kecil, tanpa tanda baca: .,!?).
# ------------------------------------------------------------

def hitung_kata(teks):
    for tanda in ".,!?":
        teks = teks.replace(tanda, "")
    frek = {}
    for kata in teks.lower().split():
        frek[kata] = frek.get(kata, 0) + 1
    return frek

print(hitung_kata("Aku suka Python. Python suka aku!"))

# Contoh output:
#   {'aku': 2, 'suka': 2, 'python': 2}
