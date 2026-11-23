# Pertemuan 6 - Jawaban soal 2
# ------------------------------------------------------------
# Soal:
#   Hitung jumlah huruf vokal pada kalimat yang diinput (tidak membedakan huruf
#   besar dan kecil).
# ------------------------------------------------------------

kalimat = input("Kalimat: ").lower()
jumlah = 0
for ch in kalimat:
    if ch in "aiueo":
        jumlah += 1
print("Jumlah vokal:", jumlah)
