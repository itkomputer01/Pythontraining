# Pertemuan 16 - Jawaban soal 6
# ------------------------------------------------------------
# Soal:
#   Jelaskan perbedaan [x*x for x in range(5)] dan (x*x for x in range(5)),
#   serta kapan memilih yang kedua.
# ------------------------------------------------------------

# Penjelasan: Bentuk dengan kurung siku adalah list comprehension: seluruh isi
# dibuat sekaligus dan disimpan di memori. Bentuk dengan kurung bulat adalah
# generator expression: nilai dihasilkan satu per satu saat dibutuhkan. Pilih
# generator expression untuk data besar atau saat hasil hanya dipakai sekali,
# misalnya sum(x*x for x in range(107)), karena tidak menyimpan seluruh list
# di memori.
