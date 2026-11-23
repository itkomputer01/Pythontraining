# Pertemuan 5 - Jawaban soal 6
# ------------------------------------------------------------
# Soal:
#   Buat permainan tebak angka: program menyimpan angka rahasia 7. Pengguna
#   terus menebak sampai benar, dan program memberi petunjuk "terlalu kecil"
#   atau "terlalu besar". Cetak jumlah percobaan di akhir.
# ------------------------------------------------------------

rahasia = 7
percobaan = 0
while True:
    tebakan = int(input("Tebak angka: "))
    percobaan += 1
    if tebakan < rahasia:
        print("Terlalu kecil")
    elif tebakan > rahasia:
        print("Terlalu besar")
    else:
        print(f"Benar! Percobaan: {percobaan}")
        break
