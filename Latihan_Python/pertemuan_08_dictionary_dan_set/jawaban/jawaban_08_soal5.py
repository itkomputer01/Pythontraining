# Pertemuan 8 - Jawaban soal 5
# ------------------------------------------------------------
# Soal:
#   Balik dictionary {"a": 1, "b": 2, "c": 3} sehingga menjadi {1: "a", 2: "b",
#   3: "c"}.
# ------------------------------------------------------------

d = {"a": 1, "b": 2, "c": 3}
terbalik = {}
for k, v in d.items():
    terbalik[v] = k
print(terbalik)

# Contoh output:
#   {1: 'a', 2: 'b', 3: 'c'}
