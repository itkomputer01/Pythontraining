# Pertemuan 8 - Jawaban soal 6
# ------------------------------------------------------------
# Soal:
#   Kelompokkan daftar kata ["apel", "jeruk", "pir", "mangga", "kiwi", "anggur"]
#   berdasarkan panjang kata dalam sebuah dictionary: kunci = panjang, nilai =
#   list kata.
# ------------------------------------------------------------

kata = ["apel", "jeruk", "pir", "mangga", "kiwi", "anggur"]
grup = {}
for k in kata:
    p = len(k)
    if p not in grup:
        grup[p] = []
    grup[p].append(k)
print(grup)

# Contoh output:
#   {4: ['apel', 'kiwi'], 5: ['jeruk'], 3: ['pir'], 6: ['mangga', 'anggur']}
