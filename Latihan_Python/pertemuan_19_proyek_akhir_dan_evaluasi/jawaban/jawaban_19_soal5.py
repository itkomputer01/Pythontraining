# Pertemuan 19 - Jawaban soal 5
# ------------------------------------------------------------
# Soal:
#   Tulis fungsi anagram(a, b) yang mengembalikan True jika dua kata anagram
#   (huruf sama, urutan berbeda), tanpa memperhatikan huruf besar/kecil.
# ------------------------------------------------------------

def anagram(a, b):
    return sorted(a.lower()) == sorted(b.lower())

print(anagram("Listen", "Silent"), anagram("abc", "abd"))

# Contoh output:
#   True False
