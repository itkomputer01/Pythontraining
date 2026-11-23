# Pertemuan 17 - Jawaban soal 1
# ------------------------------------------------------------
# Soal:
#   Dengan Counter, tentukan tiga kata yang paling sering muncul pada teks "a b
#   a c b a d b a".
# ------------------------------------------------------------

from collections import Counter
teks = "a b a c b a d b a"
print(Counter(teks.split()).most_common(3))

# Contoh output:
#   [('a', 4), ('b', 3), ('c', 1)]
