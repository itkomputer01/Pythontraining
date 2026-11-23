# Pertemuan 12 - Jawaban soal 1
# ------------------------------------------------------------
# Soal:
#   Tulis program yang meminta tiga catatan dari pengguna dan menyimpannya ke
#   catatan.txt, satu catatan per baris. Lalu baca dan tampilkan kembali dengan
#   nomor baris.
# ------------------------------------------------------------

with open("catatan.txt", "w", encoding="utf-8") as f:
    for i in range(3):
        f.write(input(f"Catatan {i + 1}: ") + "\n")

with open("catatan.txt", encoding="utf-8") as f:
    for no, baris in enumerate(f, start=1):
        print(no, baris.strip())
