# Pertemuan 6 - Jawaban soal 3
# ------------------------------------------------------------
# Soal:
#   Periksa apakah sebuah kata merupakan palindrom (dibaca sama dari depan dan
#   belakang), misalnya "katak", dengan mengabaikan huruf besar/kecil.
# ------------------------------------------------------------

kata = input("Kata: ").lower()
if kata == kata[::-1]:
    print("Palindrom")
else:
    print("Bukan palindrom")
